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
- [ ] **Scene cards / outline view** — Visual outlining mode where scenes appear as movable cards on a corkboard. Beat calls this "Powerful outlining" with scene cards. Also on Arc Studio and WriterSolo.
- [x] **Revision tracking** — Track script revisions with industry-standard colored revision marks (white, blue, pink, yellow, green, goldenrod). Highlight changes between revisions. Beat and Final Draft both support this. *(Session 9)*
- [ ] **Lockable scene numbers** — Lock scene numbers for production drafts so they don't change when scenes are reordered. Allow inline editing of locked numbers. Beat and Final Draft support this.

### To Do — Collaboration & Storage (Priority 3)

- [ ] **Real-time collaboration** — Multiple users editing the same script simultaneously with cursor presence and conflict resolution. Core feature of WriterDuet.
- [ ] **Notes and comments** — Attach notes or comments to specific lines, scenes, or acts for collaborative feedback or personal reminders.
- [ ] **Cloud sync / account-based storage** — Save scripts to a server with user accounts so work persists across devices.

### To Do — Statistics & Analysis (Priority 4)

- [ ] **Screenplay analytics** — Detailed statistics: average scene length, longest scene, locations, times of day, INT vs EXT breakdown, dialogue-to-action ratio. Beat offers these natively.

## Other Improvements (identified during development)

- [ ] **Keyboard shortcuts reference** — An in-app help panel listing all keyboard shortcuts (pill selection, undo/redo, submit, etc.)
- [ ] **Multi-line setting support** — Allow Shift+Enter for multi-line setting/action text in the input bar (currently Enter always submits)
- [ ] **Scene reordering across acts** — Drag-and-drop currently only works within the same act for scenes. Cross-act scene moves would be useful.
- [ ] **Line moving across scenes** — Same limitation as above for individual lines.
- [ ] **Print-friendly View tab** — Add print CSS or a dedicated print button to the View tab for quick paper output without PDF export.
- [ ] **Plugin / extension system** — Allow user scripts (JavaScript) to process the script data. Beat supports this on macOS.
- [ ] **Document styles** — Customizable page layout (fonts, margins) for the exported screenplay. Beat supports this.
