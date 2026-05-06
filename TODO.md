# The Scriptwriter — Feature Roadmap

Based on comparison with WriterDuet, Arc Studio Pro, WriterSolo (Session 1), and Beat (Session 7).

## Unique Strengths (keep and refine)

- **Direction cues** — Chip-based UI for tracking character entrances/exits per scene. No competitor does this natively.
- **Drag-and-drop validation** — Reordering lines validates against character presence state, preventing invalid cue sequences.
- **Character archiving** — Characters can be archived without deletion, preserving their lines and stats.
- **Zero install, browser-native** — Single HTML file, works offline, runs on any device with a browser. Beat requires macOS/iOS, Final Draft requires desktop install.
- **Structured character panel** — Expandable character cards with searchable dialogue history and jump-to-line.

## Feature Gaps

### Completed

- [x] **Inline editing** — Edit any line in place (double-click or Edit button). Dialogue shows character dropdown, action, and text fields. Direction routes to the full cue modal. *(Session 1)*
- [x] **Undo/Redo** — 50-entry cursor-based undo stack with Redo button and Ctrl+Z / Ctrl+Shift+Z shortcuts. *(Session 1)*
- [x] **PDF export** — Generates formatted screenplay PDF with title page, character list, table of contents, and script pages. *(Pre-existing in setup_fix)*
- [x] **Auto-numbered acts and scenes** — "Act One", "Scene Three" with optional user names after an em dash. *(Session 3)*
- [x] **Standalone character creation** — "+ New character" button in side panel, no dialogue line required. *(Session 3)*
- [x] **Find & replace** — Search across the entire script with line-type filter chips (Setting, Direction, Dialogue, Action). Replace individually or in bulk. Ctrl+F to open, Escape to close. *(Session 4)*
- [x] **Persistent save system** — localStorage auto-persistence + File System Access API for linking to a disk file that gets overwritten on each save. No more repeated downloads. *(Session 4)*
- [x] **Mobile responsive** — Full editing on mobile with touch drag-and-drop, hamburger menu, slide-over panel, bottom-sheet file menu, and virtual keyboard handling. *(Session 7)*

### To Do — Portability (Priority 1)

- [x] **Fountain export** — Export scripts to the Fountain (.fountain) plain-text screenplay format. Fountain is the open standard used by Beat, Highland, and many other editors. Makes scripts portable and future-proof. *(Session 8)*
- [x] **Fountain import** — Parse .fountain files and load them into the app's data model. Support scene headings, characters, dialogue, action, transitions, notes, and sections. *(Session 8)*
- [x] **FDX export** — Export to Final Draft (.fdx) XML format, the industry standard for screenplay interchange. WriterDuet, Arc Studio, Beat, and WriterSolo all support this. *(Session 8)*
- [x] **FDX import** — Import Final Draft (.fdx) files, mapping elements to the app's line types. Handles both screenplay and stage play templates including Act Break, DualDialogue, Parenthetical, and Cast sections. *(Session 8)*

### To Do — Writing Experience (Priority 2)

- [ ] **Auto-formatting mode** — Automatic detection of screenplay elements as you type: lines starting with INT./EXT. become scene headings, all-caps lines become character names, etc. Toggle between explicit pill mode and auto-detect mode.
- [x] **Scene cards / outline view** — Visual outlining mode where scenes appear as movable cards on a corkboard. Beat calls this "Powerful outlining" with scene cards. Also on Arc Studio and WriterSolo. *(Session 10)*
- [x] **Revision tracking** — Track script revisions with industry-standard colored revision marks (white, blue, pink, yellow, green, goldenrod). Highlight changes between revisions. Beat and Final Draft both support this. *(Session 9)*
- [x] **Lockable scene numbers** — Lock scene numbers for production drafts so they don't change when scenes are reordered. Allow inline editing of locked numbers. Beat and Final Draft support this. *(Session 10)*

### To Do — Scene Card Upgrades (Priority 2b)

- [x] **Editable synopsis on cards** — Add a synopsis/notes field per scene, editable inline on the card. Every major competitor (Scrivener, Final Draft, Arc Studio) centers their corkboard around this. *(Session 15)*
- [x] **Color coding** — Color-dot and left-border accent per scene, selectable from a palette. Provides instant visual structure mapping. *(Session 15)*
- [x] **Color labels** — Custom label names for colors (e.g., "A-Plot", "B-Plot", "Flashback"). Let users name what each color means and filter/sort by label. Turns color dots into a real structural analysis tool. *(Session 17)*
- [x] **Status markers** — Per-scene status badge (Outline / Draft / Revised / Final) for tracking progress at a glance. Inspired by Scrivener's status labels. *(Session 15)*
- [x] **Card size toggle** — Compact (title + color only) vs expanded (synopsis + stats + characters) view for the outline grid. *(Session 15)*
- [ ] **Beat board mode** — Free-form cards not tied to scenes, for brainstorming story beats before committing to script structure. Larger feature inspired by Final Draft and Arc Studio.

### To Do — High-Impact Writing Experience (Priority 3)

- [x] **Multi-line input (Shift+Enter)** — Allow Shift+Enter for soft newlines in the input bar. *(Session 15)*
- [x] **Notes and comments** — Attach notes or comments to specific lines, scenes, or acts for collaborative feedback or personal reminders. Inline expansion + right panel list with resolved/unresolved workflow. *(Session 16)*
- [x] **Color labels for scene cards** — Extend color dots with user-defined label names and filtering. Makes the outline a structural analysis tool, not just decoration. *(Session 17)*
- [ ] **Auto-formatting mode** — True auto-format where typing `INT.` auto-converts to a scene heading, all-caps auto-converts to a character name, etc. How Highland and Beat work natively.

### To Do — Unique Differentiators (Priority 4)

No lightweight stage play editor does these. Building them would set The Scriptwriter apart from every competitor.

- [ ] **Character relationship mapping** — Visual showing which characters share scenes, or a co-appearance matrix. Leverages our existing character panel (already the best of any editor) to help playwrights track ensemble dynamics.
- [x] **Pacing visualization** — Bar chart or timeline showing scene lengths in the outline view. Writers obsess over pacing but no lightweight editor visualizes it. *(Session 17)*
- [x] **Rehearsal sides export** — Extract one character's lines + cues for table reads. Specific to stage plays and something no competitor does well. *(Session 17)*

### To Do — Collaboration & Storage (Priority 5)

- [ ] **Real-time collaboration** — Multiple users editing the same script simultaneously with cursor presence and conflict resolution. Core feature of WriterDuet. (Deprioritized — massive backend effort, not our differentiator.)
- [ ] **Cloud sync / account-based storage** — Save scripts to a server with user accounts so work persists across devices. (Deprioritized — our value is "your files, your machine, no accounts.")

### To Do — Statistics & Analysis (Priority 6)

- [ ] **Screenplay analytics** — Detailed statistics: average scene length, longest scene, locations, times of day, INT vs EXT breakdown, dialogue-to-action ratio. Beat offers these natively.

## Other Improvements (identified during development)

- [x] **Keyboard shortcuts reference** — An in-app help panel listing all keyboard shortcuts (pill selection, undo/redo, submit, etc.) *(Session 15)*
- [ ] **Multi-line setting support** — *(Promoted to Priority 3 as "Multi-line input")*
- [ ] **Scene reordering across acts** — Drag-and-drop currently only works within the same act for scenes. Cross-act scene moves would be useful.
- [ ] **Line moving across scenes** — Same limitation as above for individual lines.
- [x] **Print-friendly View tab** — Add print CSS or a dedicated print button to the View tab for quick paper output without PDF export. *(Session 15)*
- [ ] **Plugin / extension system** — Allow user scripts (JavaScript) to process the script data. Beat supports this on macOS.
- [ ] **Document styles** — Customizable page layout (fonts, margins) for the exported screenplay. Beat supports this.
- [ ] **Refactor internal type values** — Rename internal type keys from `'direction'`→`'cue'` and `'action'`→`'stage_direction'` to match display names. Requires migration logic for saved scripts in localStorage and JSON files, plus updates to Fountain/FDX export/import mappings, CSS class names, and all JS references.
- [x] **Character panel act/scene filter** — Dialogue list respects act/scene dropdowns, line/word count badges, first/last appearance, sort by name/lines/appearance. *(Session 16)*

## Standard Test Checklist (run after every new feature)

1. **Syntax validation** — Parse all JS in the file; confirm no syntax errors.
2. **Function reference check** — Verify every `onclick` handler references a defined function.
3. **ID reference check** — Verify every `$('id')` call references an ID that exists in HTML or is created dynamically.
4. **Key function existence** — Confirm core functions exist: `render`, `pushUndo`, `doUndo`, `doRedo`, `autoSave`, `buildFountain`, `buildFDXText`, `buildPDFHTML`, `parseFountain`, `parseFDX`, `renderView`, `renderOutline`, `buildFindMatches`, `renderRPNotes`, `renderRPBookmarks`.
5. **Export exclusion** — Confirm bookmarks and notes-only constructs are excluded from Fountain, FDX, and PDF exports.
6. **Customization resilience** — Toggle alignment options, dialogue format (stacked/inline), view format (stage play/fountain/fdx), and confirm new feature still renders correctly.
7. **Undo/redo** — Confirm new feature calls `pushUndo()` before mutations and that undo reverses the change cleanly.
8. **localStorage persistence** — Confirm new state is saved/restored from localStorage.
9. **Mobile rendering** — Confirm no overflow or broken layout on narrow viewports.
10. **Dead code scan** — Check for any functions defined but never called, or variables set but never read.
