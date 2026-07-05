# Image Generation Prompt Template

Generate each image individually. Replace the variables according to the article context. Do not combine multiple illustrations into a single image.

```text
Generate one standalone 16:9 horizontal article illustration (target resolution: 1125x633 pixels).

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue handwritten annotations in Latin script. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character required:
Desi, a small solid-black absurd creature with white dot eyes, tiny thin legs, blank serious expression, slightly uneven hand-drawn body shape. Desi must perform the core conceptual action, not decorate the scene. Make Desi serious, deadpan, and slightly bizarre, not cute.

Theme:
{Illustration Theme}

Structure type:
{Structure Type: Workflow / System Component / Before-After / Character State / Concept Metaphor / Method Stack / Map-Path / Comic Strip}

Core idea:
{The central concept/point this drawing is conveying}

Composition:
{Visual layout details: where Desi is, what Desi is doing, what the main physical objects are, and how information or elements flow}

Suggested elements:
{Element 1} / {Element 2} / {Element 3} / {Element 4}

Latin-script annotations (English / Hinglish / Tenglish / Kanglish / etc.):
{Annotation 1} / {Annotation 2} / {Annotation 3} / {Annotation 4} / {Optional Annotation 5}
Note: Text annotations MUST be in the Latin script (English alphabet). Do not use Indic scripts (like Devanagari or Telugu characters). Transliterations are encouraged (e.g., Hinglish: "Samajh gaya" / "Kaam Shuru", Tenglish: "Pani Shuru", Kanglish: "Kelsa Shuru", English: "Start" / "Stop").

Color use:
Black for main line art and Desi. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state.

Constraints:
One image explains only one core structure, which can contain multiple connected wobbly mechanical elements (like conveyor belts, boxes, gears, levers, holes, and paths) to show a progression or comparison. For technical pipelines (like RAG, vector search, database replication, caching), do not generate a single generic box; break down the pipeline into its actual key steps (e.g., ingestion, chunking, embedding, vector DB, search, retrieval) and represent each with its own wobbly physical metaphor (e.g., funnel, paper cutter, stamp, drawer cabinet, fishing rod) connected by wobbly orange path arrows. A wobbly, handwritten main concept title is allowed and should be centered at the top of the illustration. You can show one or more instances of the character Desi in different parts of the diagram performing different actions to illustrate steps. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Latin annotations. Do not write a generic category title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean.
```

## Image Edit Prompts

### Remove Top-Left Title:

```text
Edit the provided image. Remove only the handwritten title "{text to remove}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

### Enhance Desi's Action:

```text
Regenerate this illustration with the same core meaning and simple layout, but make Desi more central to the conceptual action. Desi should be doing the strange work that explains the idea, not standing beside the diagram. Keep it clean, sparse, hand-drawn, and not cute.
```
