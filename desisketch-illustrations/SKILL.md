---
name: desisketch-illustrations
description: Design, create, draw, plan, or edit hand-drawn DesiSketch-style article illustrations, diagrams, conceptual sketches, and visual metaphors for Indian contexts (English, Hinglish, Tenglish, Kanglish, etc.). Triggered when users ask for illustrations, strategy/shot lists, or edits for articles, blogs, Notion pages, or workflows featuring the wobbly-line, deadpan Desi IP character with minimal colored annotations.
---

# DesiSketch Illustrations - India Edition

## Core Concept

Design and generate 16:9 horizontal article illustrations for Indian contexts. The goal is not commercial vector art, standard PPT infographics, or cute cartoons, but rather to translate a key judgment, workflow, structure, state, or metaphor from the text into a clean, slightly absurd, creative, hand-drawn explainer.

The default recurring character is "Desi": a solid black creature with white dot eyes, thin legs, and a deadpan expression, seriously performing an absurd but meaningful task. Desi must be an active participant in the visual metaphor, not just a decorative element standing in a corner.

## Reference Manuals

Read these references as needed based on the task (do not overload the context all at once):

- `references/style-dna.md`: Style DNA, color logic, text annotations, and design constraints.
- `references/desisketch-ip.md`: Desi IP appearance, personality, common actions, and forbidden traits.
- `references/composition-patterns.md`: Layout structures, physical metaphor generation methods, and anti-plagiarism rules.
- `references/prompt-template.md`: Single image prompt template.
- `references/qa-checklist.md`: Post-generation inspection and iteration rules.
- `assets/examples/`: Visual style calibration examples (do not copy their exact layout, objects, or annotations).

## Workflow

### 1. Digest the Source Text

Read the provided text, links, Notion pages, markdown files, or images. Identify:
- What is the core point/thesis?
- Which paragraphs introduce cognitive turns or transitions?
- Which sections are best explained visually?
- Which sections should remain purely textual?

Avoid even/uniform illustration spacing. Select "cognitive anchors" such as: core decision points, two distinct breakpoints, input/output feedback loops, splits, before-and-after comparisons, multi-purpose items, user paths, common pitfalls, or changes in state.

### 2. Formulate Illustration Strategy First

If the user asks to "analyze how to illustrate" or "plan the illustrations," generate a shot list first. For each image, specify:
- Placement (which paragraph it follows)
- Image Theme
- Core Metaphor
- Structure Type (e.g., Workflow, System Component, Comparison, State)
- Desi's Action (what Desi is doing in the image)
- Key Elements
- Suggested Latin-script annotations (in Hinglish, Tenglish, Kanglish, English, etc.)

Keep the shot list to 4–8 images. For short posts, 1–3 images; even for long articles, do not exceed 9 images. Keep it concise.

### 3. Generate Single Images

If the user explicitly requests to "generate," "create," or "output" the images, do not wait for separate confirmation; use the image generation capabilities to produce each image one by one. Do not combine multiple images into a single file.

Each image must explain only one core concept. The prompt must request:
- A 16:9 standalone horizontal illustration
- Pure white background
- Minimalist black hand-drawn line art
- Sparse handwritten English/transliterated annotations (Hinglish/Tenglish/Kanglish/etc.) using the Latin script
- High amount of negative white space
- Desi performing the core action
- ABSOLUTELY NO commercial vector styles, cute cartoon elements, formal flowcharts, or titles in the top-left corner.

Do not copy previous compositions (such as a conveyor belt breakpoint, cutting an asset fish, or pulling three ropes) unless explicitly asked. Invent a new metaphor specific to the content.

### 4. Inspect and Iterate

Check the output against the `references/qa-checklist.md`. Re-generate or edit if any of the following apply:
- Desi is acting purely as decoration.
- The canvas is overcrowded.
- The drawing looks like a formal PowerPoint slide or technical diagram.
- Text contains typos or is illegible.
- A category title (e.g., "Workflow", "Pitfalls") appears in the corner.
- The style is too cute, childish, or sterile.
- The background is not solid white.

### 5. Save and Deliver

If working inside a workspace, copy the final image to:
```text
assets/<article-slug>-illustrations/
```
Name them sequentially:
```text
01-topic-name.png
02-topic-name.png
```
Keep original assets unless requested to replace them.

## Output Format

Keep pre-generation strategy output brief and focused. Final delivery must state:
- Number of images generated
- Purpose of each illustration
- File storage paths
- Which illustrations are essential vs. optional

Do not over-explain the style DNA; let the drawings speak for themselves.
