# Design note

TODO(you): keep this to one page. Suggested sections — cut what doesn't
earn its place:

## Architecture

One paragraph + the module list (see README) — why each pipeline stage
sits behind its own interface (document parser, model provider, standards
source, check) and what swapping one implementation for another would
involve.

## Key design decisions

e.g. how a Claim's status (documented / asserted only / contradicted /
missing) gets decided; how units are normalized; how a check becomes
"can't check" rather than silently passing or being dropped.

## What's not done / known weak points

Per the brief's deliverable list — be specific (which check types, which
file formats, OCR accuracy on which document types, etc.) rather than a
generic disclaimer.

## Model & provider

Which provider(s) you used, and — if you ran a local open-weight model —
which model, quantization, and serving config, so it can be reproduced on
other hardware, per the brief's request.
