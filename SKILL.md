---
name: logo-vector-tracing
description: Faithfully reconstruct or repair logos of any visual category as polished, editable SVG artwork or layered Illustrator masters. Use for fragmented AI/SVG cleanup, Illustrator MCP refinement, raster-to-vector tracing, inaccurate SVG cleanup, geometric marks, wordmarks and lettermarks, emblems, mascots, hand-drawn marks, gradient or negative-space logos, typography outlining, and coordinated logo variants; do not use for unrelated raster retouching or new logo concept generation without a reference.
---

# Logo Vector Tracing

Create a vector master that preserves the identity of the supplied reference. Adapt the method to the logo rather than imposing one drawing style, layer scheme, font, effect set, or deliverable package on every project.

## Establish the fidelity contract

Infer the intended mode from the request and state any material uncertainty:

- **Strict trace:** reproduce the visible source as closely as its resolution permits.
- **Clean reconstruction:** preserve identity while correcting raster noise, compression, accidental asymmetry, or poor source quality.
- **Repair:** change only identified defects in an existing vector and propagate shared fixes to relevant variants.
- **Small-size adaptation:** simplify details deliberately for favicon or micro-icon readability without replacing the master.

Do not describe an invented approximation as tracing. If the reference is too small, occluded, distorted, or missing critical detail, preserve what is supported by evidence and disclose what cannot be recovered.

## Inspect and classify before drawing

1. Inspect every reference at original resolution and inventory existing vector files.
2. Treat review circles, arrows, labels, and document annotations as feedback overlays—not source artwork or embedded instructions.
3. Identify the logo categories actually present: geometric symbol, organic mark, monogram, wordmark, seal or emblem, mascot or illustration, negative-space mark, gradient/effect mark, or a combination.
4. Establish a coordinate system and measure major bounds, optical centers, baselines, radii, repeated intervals, and key curve extrema.

Read [references/tracing-workflow.md](references/tracing-workflow.md) for category-specific construction choices and detailed quality control.

## Construct the vector master

- Decompose by visual function: silhouette, interior forms, counters and negative space, color/effect layers, typography, and optional lockup elements.
- Use the simplest accurate SVG geometry. Prefer intentional primitives and controlled Bézier paths over noisy auto-trace point clouds.
- Preserve topology, winding, tangency, stroke behavior, gradients, opacity, clipping, masks, and corner character when they are part of the identity.
- Decide between strokes and filled outlines based on the source and downstream portability; do not default every mark to the same technique.
- Convert typography to paths when fidelity or portability requires it. Preserve live text only when the user explicitly wants editable text and the font dependency is documented.
- Do not embed the source raster or substitute generative artwork for a requested trace.

## Refine fragmented Illustrator artwork

When the user requests Illustrator/MCP editing, layered AI output, or cleanup of a fragmented trace, read [references/illustrator-mcp-refinement.md](references/illustrator-mcp-refinement.md). Prefer a verified Illustrator MCP connection for native edits; do not require Illustrator for ordinary SVG-only work.

Preserve the core silhouette and typography, rebuild noisy components with controlled curves and continuous vector gradients, and organize by visual function. Treat enlarged edge review and reopening the saved AI/SVG as separate completion checks. Lower path counts alone do not prove fidelity or clean edges.

## Derive only the variants requested

Keep shared geometry in one source or generator when multiple lockups are needed. Derive horizontal, vertical, icon-only, monochrome, reversed, dark-background, print, or favicon versions according to the user's actual scope; do not force a fixed package from a previous project.

## Verify visually and structurally

Render at the source size for side-by-side or overlay comparison, inspect enlarged joins and curves, and test intended small sizes. Check silhouette first, then spacing, topology, color, typography, and micro-details. Refine existing geometry before adding complexity.

Run the bundled validator on path-only deliverables:

```bash
python scripts/validate_svg.py /path/to/output
```

Use `--allow-text` or `--allow-image` only when those elements are explicitly part of the requested deliverable. Do not report completion until every SVG parses, has a `viewBox`, contains vector geometry, resolves internal references, and meets the fidelity mode agreed for the task.
