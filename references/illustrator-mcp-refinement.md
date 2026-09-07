# Illustrator MCP refinement

Use this workflow for fragmented AI/SVG artwork, native Illustrator layer organization, or local edge repairs. Preserve the fidelity mode established in SKILL.md; Illustrator is optional for SVG-only tasks.

## Connect and inspect

Prefer an existing, verified Illustrator MCP connection when the user requests it. Discover the actual callable capabilities and perform a read-only document/status query before editing. Configuration or installation alone does not prove connectivity. If installation is necessary, follow the user's authorization and the environment's installation process; this guide does not install a server or assume a particular vendor, operating system, or tool name.

Identify the target document by its full path and keep an explicit document reference. Inventory layers, groups, paths, anchors, compound paths, raster/linked items, and text. Inspect the rendered artwork as well as its object structure: thousands of flat vector patches can still be an unclean trace, and zero raster items does not prove editability.

Record the accepted silhouette, proportions, custom letterforms, counters, spacing, stacking, and color transitions. Locate actual defects before choosing which components to rebuild. Keep a recoverable source until the saved outputs pass validation.

## Rebuild by visual component

- Retain accurate original contours. Replace fragmented or defective components with the simplest geometry that preserves their appearance.
- Use deliberate Bézier segments through meaningful extrema, with compatible tangents at smooth joins. Use circles, rounded rectangles, or repeated geometry only where supported by the source.
- Replace patchwork color bands with continuous vector gradients. Match direction, stops, opacity, clipping, and overlap to the reference.
- Give adjacent faces a single intended shared boundary. Two centered strokes along the same seam can produce a dark ridge, gap, or protruding corner.
- Preserve masks, highlight shapes, and stacking where they contribute to the appearance. Do not flatten the editable master merely to reduce object counts.

Automatic point reduction followed by spline smoothing is only a candidate reconstruction. It can retain small cusps, overshoot corners, or distort terminals. Review each changed contour; fit intentional handles where automatic smoothing fails. Round caps and joins help only when consistent with the source.

For a follow-up such as “fix the edges,” hold the accepted layout, typography, and palette stable. Compare repaired letterforms against the accepted version for width, terminals, counters, and spacing. Disclose material reconstruction or font substitution; do not present a redesign as a local repair.

## Perform a separate edge pass

Check the whole mark at its intended size, then render the vectors at enlarged scale, typically 200–400% or more for a suspect join. Enlarging an existing PNG can locate a defect but cannot establish the quality of the underlying curves.

Inspect dark fills and light backing silhouettes separately. Look for:

- Flat nicks, cusps, spikes, closure discontinuities, or mismatched tangents.
- Duplicate borders, seam gaps, and overshooting strokes.
- Small trapped background slits where close letterforms or thick backing strokes meet.
- Distorted counters, collapsed negative space, and loss of deliberate hand-drawn character.

Distinguish a true transparent counter from an intentional white sticker border. A true hole needs correct compound-path topology or fill behavior, not a white patch. A white backing is separate visible artwork and may have different topology from the foreground. Reusing the foreground's compound cutouts with a thick backing stroke can leave narrow unwanted slits.

Reconstruct the backing as a coherent silhouette where possible. Use a local join only when justified by the intended contour; avoid accumulating arbitrary patches or thickening every stroke to hide defects. Inspect on light, dark, and checkerboard backgrounds to expose unintended opacity or holes.

Small objects are not automatically debris: dots, punctuation, highlights, and legitimate details may have tiny bounds. Use size thresholds as diagnostics relative to document scale, then inspect before removing anything.

## Build native, named layers

Organize by actual visual function or component: backing, symbol parts, highlights, wordmark, and optional secondary text. Choose names and granularity useful to the user; do not enforce a fixed layer count from another logo.

SVG groups are not necessarily native Illustrator layers. After import, enumerate actual group names and parents before mapping them: importers may normalize identifiers, including spaces and underscores. Move complete component groups into native layers while preserving stacking, and verify every component was mapped before removing empty import layers.

When scripts inspect or style objects, traverse nested groups and compound-path children explicitly. A group's direct path collection may omit paths inside nested compounds. Target the intended document, not whichever document happens to be active after import.

Keep custom wordmarks as faithful outlines. Retype secondary text only when the fidelity mode permits it and the substitution is disclosed. If editable text is explicitly requested, document the font dependency and, where useful, retain a clearly labeled hidden live-text layer with a visible outlined counterpart. Do not export duplicate visible text.

## Save, crop, and reopen explicit outputs

Store explicit destination paths for AI and SVG before export. An export can change document name or path context; never infer the AI reopen target from the post-export active document. Verify the actual filename on disk, including any exporter normalization.

Save a layered AI master with appropriate compatibility settings, retaining editable paths and gradients. Use PDF compatibility when needed by the delivery workflow. Avoid indiscriminately expanding all master strokes or effects. If SVG export expands or transforms them, inspect the result.

Crop the canvas only when requested or appropriate to the delivery scope. Measure visible artwork bounds, including intended strokes and effects, while excluding hidden edit layers and any background rectangle that merely covers the canvas. Preserve the requested padding. For top/bottom-only trimming, retain the horizontal viewBox extent and update viewport dimensions consistently without scaling the artwork. Convert coordinates explicitly between SVG's downward y-axis and Illustrator's artboard coordinates.

Reopen the saved AI by its explicit path and verify the path, native layer names/order, and retained vector structure. Open the exported SVG separately and inspect it too. Restore temporary application settings, such as interaction level, in a finally block; do not hide meaningful save/export failures.

## Validate fidelity and export consistency separately

Run the bundled SVG validator:

```bash
python scripts/validate_svg.py /path/to/output.svg
```

Use its exceptions for text or images only when those are part of the agreed deliverable. For all-vector outputs, check for raster and linked items in Illustrator as well as image elements in SVG. Record path and anchor counts as supporting evidence, not quotas: a valid repair may add a few backing shapes while reducing unnecessary anchors.

Render the reopened AI and SVG at matching dimensions, background, and color/export settings. Compare them side by side or with overlays; pixel differences can help locate export drift. A low whole-image average can hide a serious local edge error, so inspect the repaired regions separately.

AI/SVG agreement proves export consistency, not fidelity to the source. Also compare the result with the reference or accepted earlier version under the agreed fidelity mode. Completion requires all three: preserved identity, clean local edges, and verified saved outputs.

Deliver the requested formats with concise notes on the repaired components and any remaining approximation or font dependency. Keep helper scripts and diagnostics separate from final artwork. Delete or archive old versions only within cleanup the user authorized; never infer blanket permission to remove unrelated originals.
