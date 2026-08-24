#!/usr/bin/env python3
"""Validate path-only SVG logo deliverables without third-party packages."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET


URL_REF = re.compile(r"url\(\s*#([^\s)]+)\s*\)")
PROHIBITED_BY_DEFAULT = {"text", "image", "foreignObject"}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def discover(targets: list[str]) -> list[Path]:
    found: set[Path] = set()
    for raw in targets:
        path = Path(raw)
        if path.is_dir():
            found.update(p.resolve() for p in path.rglob("*.svg"))
        elif path.suffix.lower() == ".svg" and path.is_file():
            found.add(path.resolve())
    return sorted(found)


def validate(path: Path, allow_text: bool, allow_image: bool) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    counts = {"paths": 0, "gradients": 0, "text": 0, "images": 0}
    try:
        tree = ET.parse(path)
    except (ET.ParseError, OSError) as exc:
        return [f"XML parse failed: {exc}"], counts

    root = tree.getroot()
    if local_name(root.tag) != "svg":
        errors.append("root element is not <svg>")
    if not root.get("viewBox"):
        errors.append("missing viewBox")

    ids: set[str] = set()
    duplicate_ids: set[str] = set()
    refs: set[str] = set()

    for element in root.iter():
        name = local_name(element.tag)
        if name == "path":
            counts["paths"] += 1
        elif name in {"linearGradient", "radialGradient"}:
            counts["gradients"] += 1
        elif name == "text":
            counts["text"] += 1
        elif name == "image":
            counts["images"] += 1

        element_id = element.get("id")
        if element_id:
            if element_id in ids:
                duplicate_ids.add(element_id)
            ids.add(element_id)

        if name in PROHIBITED_BY_DEFAULT:
            if name == "text" and allow_text:
                pass
            elif name == "image" and allow_image:
                pass
            else:
                errors.append(f"contains prohibited <{name}> element")

        for key, value in element.attrib.items():
            refs.update(URL_REF.findall(value))
            if local_name(key) == "href" and value and not value.startswith("#"):
                errors.append(f"contains external href: {value}")

    if counts["paths"] == 0:
        errors.append("contains no <path> elements")
    if duplicate_ids:
        errors.append("duplicate IDs: " + ", ".join(sorted(duplicate_ids)))
    missing_refs = sorted(refs - ids)
    if missing_refs:
        errors.append("unresolved local references: " + ", ".join(missing_refs))

    return errors, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="+", help="SVG files or directories to scan recursively")
    parser.add_argument("--allow-text", action="store_true", help="permit <text> elements")
    parser.add_argument("--allow-image", action="store_true", help="permit <image> elements")
    args = parser.parse_args()

    files = discover(args.targets)
    if not files:
        print("ERROR: no SVG files found", file=sys.stderr)
        return 2

    failed = 0
    for path in files:
        errors, counts = validate(path, args.allow_text, args.allow_image)
        summary = (
            f"paths={counts['paths']} gradients={counts['gradients']} "
            f"text={counts['text']} images={counts['images']}"
        )
        if errors:
            failed += 1
            print(f"FAIL {path} ({summary})")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {path} ({summary})")

    print(f"Checked {len(files)} SVG file(s); {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

