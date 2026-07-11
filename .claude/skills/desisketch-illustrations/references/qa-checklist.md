# QA Checklist

## Mandatory Pass Criteria

- **Aspect Ratio:** Must be exactly 16:9 horizontal.
- **Background:** Must be clean, solid white.
- **Character Present:** Desi must be in the scene (one or more instances of Desi are allowed).
- **Active IP:** Desi must perform the core action(s), not just act as decoration.
- **Fresh Metaphor:** No direct replication of prior example layouts; the visual metaphor must be customized for the current article.
- **Tone:** Absurd, creative, thought-provoking, and deadpan.
- **Negative Space:** Minimalist layout; main subject occupies no more than 60% of the canvas.
- **Single Focus:** One illustration conveys exactly one core structural concept, which can use multiple wobbly elements (conveyor belts, boxes, holes, etc.) and arrows.
- **Latin Script Only:** All handwritten annotations must use the Latin alphabet (English writing). Regional Indian words (Hinglish/Tenglish/Kanglish/etc.) must be transliterated. No Indic scripts.
- **Accents & Annotations:** Text must be sparse (5-8 labels max), short, and legible.
- **Orange Usage:** Used strictly for paths, arrows, automation flows, or directions.
- **Red Usage:** Used strictly for errors, warnings, blocks, or critical outcomes.
- **Blue Usage:** Used strictly for system status, background notes, or AI assistant feedback.

## Failure Signals (Re-generate or Edit if present)

- The top-left corner features a generic category title (e.g., "Workflow", "Pitfalls", "System Architecture") or underline. A wobbly concept title centered at the top is allowed.
- Desi looks like a cute, glossy corporate mascot, emoji, or children's cartoon.
- The illustration resembles a formal PowerPoint slide, a complex BPMN flowchart, or a technical diagram.
- Too many nodes, boxes, arrows, or details crowded onto the canvas (unless they are part of a clear, connected wobbly machine structure).
- Annotations consist of long explanatory sentences rather than short labels.
- Background features gradients, shadows, noise, paper grains, or an off-white color.
- The scene displays realistic software UI screens or digital tech graphics.
- Non-Latin script characters (e.g., Devanagari, Telugu, Kannada alphabets) are rendered, or Latin text is garbled.
- The drawing feels rigid, literal, or sterile without any weird or absurd metaphor.
- The illustration represents a technical concept (e.g., RAG, API cache, vector search) as just a generic machine or a simple box, failing to map the actual architectural pipeline stages (like ingestion, chunking, embedding, vector DB, retrieval) to distinct wobbly physical metaphors.
- The layout is too similar to the calibration files in `assets/examples/`.

## Iteration Guidelines

- **Too boring:** Shift Desi to be the main driver of the action and introduce a low-tech physical metaphor.
- **Too cluttered:** Eliminate nodes or steps; limit the visual to a single action with 3–5 short annotations.
- **Too cute:** Emphasize details like "deadpan", "blank serious expression", "not cute", "not a mascot".
- **Too corporate/slide-like:** Remove geometric grids, border enclosures, and straight technical arrows; replace with loose, hand-drawn lines.
- **Typographical errors:** If the text is slightly garbled, perform an image edit/patch; if the error is major, re-generate with fewer and shorter labels.

## Final Review Standard

An effective illustration should make the viewer think "that's weird" first, and then understand the structural concept within 1 second. 

If the drawing looks like a typical textbook slide or a corporate diagram, it is a FAIL. It must look like a wobbly product sketch on a blank piece of paper.
