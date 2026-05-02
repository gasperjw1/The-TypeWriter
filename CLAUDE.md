# Script Maker — Project Memory

## Owner
Yash Mahtani (yashmahtani@gmail.com)

## Project Overview
**The TypeWriter** is a screenplay/script writing application. The main app is `script_maker_setup_fix.html` at the repo root — a single-file, zero-dependency web app. The project evolved from a Python CLI (`script_maker.py`) through several web UI iterations, all now in `archive/`.

## Architecture

### Files
- `script_maker_setup_fix.html` — **Latest version (current)**. Standalone full-HTML version (with `<!DOCTYPE html>`, `<head>`, `<body>`) that includes its own CSS variable definitions and dark mode media query. Has all features from v10 plus: PDF export, author field, autosave toggle, resizable right panel, smart tooltip positioning (fixed/viewport-clamped), direction cue editing in modal, deselect-line-on-click, parenthetical handling in dialogue, inline editing, 50-entry cursor-based undo/redo with Redo button, auto-numbered acts/scenes, standalone character creation, and rich pill tooltips.
- `TODO.md` — Feature roadmap tracking completed work and remaining gaps identified from competitor analysis.
- `CLAUDE.md` — This project memory file.
- `archive/` — Older versions and the original CLI, kept for reference:
  - `script_maker.py` — Original Python CLI version with Act > Scene > Line hierarchy.
  - `script_maker_ui_v6.html` — Early web UI with custom CSS variables.
  - `script_maker_ui_v9.html` — Intermediate version using host-app CSS variables.
  - `script_maker_ui_v10.html` — Host-app embedded version with inline editing and undo/redo.

### Data Model (in-memory JS object `S`)
```
S = {
  title: string,
  author: string,
  characters: [{ name: string, description: string, archived: boolean }],
  acts: [{
    name: string,          // optional user-given name (display uses actLabel which adds "Act One" numbering)
    description: string,
    scenes: [{
      name: string,        // optional user-given name (display uses sceneLabel which adds "Scene One" numbering)
      description: string,
      lines: [{
        type: 'setting' | 'direction' | 'dialogue' | 'action',
        value: string,
        character?: { name, description },      // for dialogue & action
        dialogueAction?: string,                 // for dialogue
        cues?: { enters: string[], exits: string[] }  // for direction
      }]
    }]
  }]
}
```

### Persistence
- Save/load via JSON files (`raw_script_<title>.json`)
- Save triggers a browser download (Blob + anchor click)
- Auto-save on every structural change (if file has been saved at least once)
- Save indicator: gray (no file), orange (unsaved new), red (unsaved changes), green (saved)
- `beforeunload` guard for unsaved changes

### UI Layout
- **Top bar**: Title, save indicator dot, context breadcrumb (e.g. "Act One — Intro / Scene Two"), tabs (Edit/Summaries/View/Settings), File options dropdown, Undo/Redo buttons
- **Main area**: Left script body + right panel (TOC + character list)
- **Script body**: Setup screen OR script content + input bar
- **Input bar**: Type pills (Setting/Direction/Dialogue/Action) with rich hover tooltips + context-specific input boxes + submit button
- **Right panel**: Collapsible. Table of contents (acts/scenes tree), character list with act/scene filter dropdowns, "+ New character" button

### Key Features
1. **Line types**: Setting, Direction (with enter/exit cues), Dialogue (character + optional action + text), Action. Each pill has a rich tooltip describing its purpose, shortcut, and usage tips.
2. **Insert cursor**: Click any line to set insertion point; new lines go after selected line
3. **Pill system**: Keyboard shortcuts via backtick+number (`` ` ``+1=Dialogue, +2=Action, +3=Setting, +4=Direction). Smart auto-advance (setting→direction→dialogue)
4. **Character management**: Auto-create on first use, dropdown with autocomplete + ghost text, scene filter toggle, archive/delete with usage checking. Standalone "+ New character" button in right panel.
5. **Direction cues**: Track character entrances/exits per scene. Visual chips for toggling. Validated on drag-and-drop reorder. Live-update when characters are created/edited/un-archived.
6. **Drag & drop**: Acts, scenes, and lines can be reordered within the same container. Line moves are validated against character presence state. Cross-container drags are cleanly rejected (no phantom undo entries).
7. **Dialogue continuity**: Auto-detects `(cont.)` when same character has consecutive dialogue
8. **Undo/Redo**: 50-entry cursor-based snapshot stack. Ctrl+Z / Ctrl+Shift+Z (or Ctrl+Y). Undo/Redo buttons in top bar.
9. **Inline editing**: Double-click or Edit button. Setting/Action: textarea. Dialogue: character select dropdown + action + text. Direction: routes to full cue modal. Enter saves, Escape cancels, blur auto-saves.
10. **Tabs**: Edit (main editor), Summaries (stats + character list), View (read-only screenplay format), Settings (font size, indicator style/color)
11. **Modals**: Draggable modals for editing acts/scenes/lines/characters, creating new characters, confirming deletes
12. **Auto-numbered acts/scenes**: "Act One", "Scene Three" with optional user name after em dash. `numWord()`, `actLabel()`, `sceneLabel()` helpers.
13. **PDF export**: Formatted screenplay PDF with title page, character list, table of contents, and script pages.

### Version Evolution (v6 → v9 → v10 → setup_fix)
- v6: Basic structure. Custom CSS variables, dark mode, setup screen with just title input, no direction cues, no character archiving, simpler file menu.
- v9: Adopted host-app CSS variables. Added scroll-back button, character filter dropdowns, indicator settings (barrier vs highlight with color options), scene character summary in scene headers.
- v10: Added setup screen with cards (New/Open), save indicator with tooltip states, scene filter toggle for character dropdown, direction cues system, drag validation, character archiving, summaries panel with stats grid, smart pill auto-advance, confirm-state pattern for edit/delete buttons, auto-size textareas. Added inline editing and 50-entry undo/redo in Session 1.
- setup_fix (current): All v10 features plus PDF export, author field, autosave toggle, resizable panel, smart tooltip positioning, direction cue modal, deselect, parenthetical handling, standalone character creation, auto-numbered acts/scenes, dialogue inline select dropdown, direction inline→modal routing, rich pill tooltips, live direction cue updates.

### Python CLI (`script_maker.py`)
- Same data model: Script > Act > Scene > Line with Character
- Uses `LineType` enum: SETTING, ACTION, DIRECTION, DIALOGUE, DIALOGUE_ACTION
- Menu-driven: 10 options (Add Act/Scene/Setting/Direction/Action/Dialogue, Update Line/Char, Show Script, Done)
- Saves to `raw_script_<title>.json` with same structure as web version
- Has `prompt_confirmed()` pattern: enter value → confirm/rewrite loop

### CSS Theming
- v10 and v9 rely on host-app CSS variables: `--color-background-primary`, `--color-text-primary`, `--color-border-secondary`, `--font-sans`, `--border-radius-md`, `--border-radius-lg`, etc.
- v6 and setup_fix define their own variables with dark mode media query
- All versions use Courier New monospace for screenplay text
- Consistent design language: pills with rounded borders, subtle shadows, tertiary colors for secondary info

### Known Patterns & Conventions
- `esc()` and `escJs()` for HTML/JS string escaping
- `pushUndo()` before any state mutation
- `autoSave()` + `render()` after mutations
- Confirm-state pattern: first click sets `confirmState[key]`, second click executes. Renders "Confirm edit?" / "Confirm delete?" buttons.
- Modal HTML is built inline as string templates
- All state lives in the global `S` object — no framework, no build step
- `actLabel(ai)` / `sceneLabel(ai,si)` for display — never show raw `act.name` / `scene.name` directly
- `render()` calls `updateDirCues()` when direction input is active, ensuring cue chips are always fresh

## Feature Roadmap (see TODO.md)

### Completed
- [x] Inline editing (Session 1)
- [x] 50-entry undo/redo with keyboard shortcuts (Session 1)
- [x] PDF export (pre-existing in setup_fix)
- [x] Auto-numbered acts and scenes (Session 3)
- [x] Standalone character creation from side panel (Session 3)
- [x] Rich pill tooltips with descriptions and shortcuts (Session 3)

### Remaining (priority order)
- [ ] FDX export (Final Draft format — industry standard)
- [ ] Find & replace across the script
- [ ] Auto-formatting (slugline conventions, character name capitalization)
- [ ] Real-time collaboration
- [ ] Revision tracking / version history
- [ ] Beat board / index card view
- [ ] Notes and comments on lines/scenes
- [ ] Cloud sync / account-based storage

### Other Improvements
- [ ] Keyboard shortcuts reference panel
- [ ] Multi-line setting/action support (Shift+Enter)
- [ ] Cross-act scene reordering
- [ ] Cross-scene line moving
- [ ] Print-friendly View tab

## Conversation History

### Session 1 — 2026-04-30 / 2026-05-01
- Created this CLAUDE.md from fresh codebase analysis (no prior sessions existed for this project)
- Compared app to WriterDuet, Arc Studio, WriterSolo via Chrome browser research
- Identified 9 feature gaps, 3 unique strengths (direction cues, drag validation, char archiving)
- Top gaps: PDF/FDX export, inline editing, find & replace, auto-formatting
- **Implemented inline editing (v10)**: Double-click or Edit button opens inline edit mode for any line. Dialogue shows all three fields (character, action, text) with action always visible during edit even if empty. Enter saves, Escape cancels, blur auto-saves. Tab flows through dialogue fields (char → action → text). Global keyboard shortcuts suppressed during inline edit. Confirm-state pattern removed from Edit button (kept for Delete). Added `editingLine` state, `ieBlurTimer` debounce, `renderInlineEditLine()`, and CSS for `.inline-editing` / `.ie-*` classes.
- **Implemented undo/redo system (v10)**: Expanded snapshot-based undo from 3-level push/pop to 50-entry stack with cursor-based bidirectional navigation. Added `undoCursor` state variable. Rewrote `pushUndo()` to splice future states and cap at 50. Added `doRedo()` and `updateUndoRedoBtns()`. Added Redo button (↪) next to Undo in top bar. Keyboard shortcuts: Ctrl+Z (undo), Ctrl+Shift+Z / Ctrl+Y (redo) — both save any active inline edit first. `loadFile` and `doNewScript` reset `undoCursor=-1` and disable both buttons.

### Session 2 — 2026-05-01
- **Bug fix: `doUndo` cursor at max capacity** — When the undo stack hit 51 entries during undo's save-current-state step, `shift()` removed the oldest entry but the cursor was inside an `else` branch and wasn't adjusted. This caused undo to restore the current state (no-op) instead of the previous state. Fixed by always setting `undoCursor=undoStack.length-2` after the push+shift.
- **Bug fix: `delAct`/`delScene` not clearing `editingLine`** — If a user was inline-editing a line and deleted the containing act or scene, the `ieBlur` timer could fire and `saveInlineEdit` would modify wrong data at the now-shifted indices. Added `editingLine` null guards to both functions, matching the pattern already used in `delLine`.
- **Dead code removal (v10)**: Removed `openEditLine()` and `saveLineEdit()` (old modal-based line editing, replaced by inline editing and never called), `lastAddedType` variable (set but never read), `#action-simple-ta` CSS rule (no matching element), empty `.toc-act-wrap{}` CSS rule.
- **Ported all features to setup_fix**: Inline editing (CSS + JS + render changes), undo/redo system (50-entry cursor-based with Redo button and Ctrl+Z/Ctrl+Shift+Z/Ctrl+Y shortcuts), `editingLine` guards on delAct/delScene/delLine, undoCursor reset in loadFile/doNewScript. The setup_fix file retains its own unique features (PDF export, author field, autosave toggle, resizable panel, smart tooltip positioning, direction cue modal editing, deselect, parenthetical handling) that v10 does not have. Setup_fix is now the primary development target.
- **Bug fix: `setup-cards` missing id (v10)**: The setup screen's cards div had `class="setup-cards"` but no `id`, so `$('setup-cards')` returned null and the New Script button threw a TypeError. Added `id="setup-cards"`. (Note: setup_fix already had this as `id="setup-cards"` — the bug was v10-only.)

### Session 3 — 2026-05-01
- **Inline edit fix: Dialogue character dropdown (setup_fix)** — Replaced the free-text `<input>` for character name in dialogue inline editing with a `<select>` dropdown populated from `S.characters.filter(c=>!c.archived)`. This prevents accidental name changes that wouldn't register as a real character. Updated `saveInlineEdit()` to read the selected character and copy both `name` and `description` from the matching character object. Added CSS for the select element styling.
- **Inline edit fix: Direction routes to modal (setup_fix)** — Direction lines now open the existing `openEditLine()` modal (with full enter/exit cue editing via `buildDirEditModal`) instead of using inline text-only editing. Modified `startInlineEdit()` to detect direction type and redirect to the modal. This restores the ability to edit direction cues that was lost when inline editing was introduced.
- **Inline edit audit**: Compared inline editing capabilities against the input bar for all four line types. Setting (text-only) and Action (text-only) have full parity. Dialogue now has character selection via dropdown (input bar has autocomplete + ghost text, but the dropdown covers the core need without risking orphaned character references). Direction uses the full modal editor matching the input bar's cue chip system.
- **Bug fix: Enter key not submitting Setting/Action lines** — The `simple-ta` textarea (used for Setting and Action types) had no `onkeydown` handler, so pressing Enter just inserted a newline. Added `onkeydown="lastFieldKey(event)"` to match the behavior of `dir-desc-ta` and `dlg-text-ta`, so Enter now submits the line.
- **New character from side panel** — Added a "+ New character" button at the bottom of the right-panel character list. Opens a modal with Name and Description fields. `openNewCharStandalone()` / `confirmNewCharStandalone()` create the character directly in `S.characters` without requiring a dialogue line. Includes duplicate-name check. Styled with dashed border matching the panel aesthetic.
- **Inline edit styling: Dialogue character dropdown** — Narrowed the `<select>` dropdown for character names in dialogue inline editing (`width:auto; max-width:200px; margin:0 auto; display:block`) so it sizes to content rather than stretching full-width.
- **Auto-numbered acts and scenes** — Acts and scenes now auto-number with word form ("Act One", "Scene Three"). The `name` field is now optional — if given, it appears after an em dash (e.g., "Act One — The Beginning"). Added `numWord(n)` (1–20 as words, 21+ as digits), `actLabel(ai)`, and `sceneLabel(ai,si)` helpers. Updated all display points: editor headers, TOC, breadcrumb, context bar, View tab, character filter dropdowns, PDF export (TOC + script pages), and create/edit modals. New-script flow defaults Act to "One" and Scene to "One" with names optional. `saveActEdit`/`saveSceneEdit` now allow clearing the name (previously fell back to old value).
- **Direction cues live-update on character changes** — Added `if(cType==='direction')updateDirCues()` to `render()`, so any mutation that triggers a re-render (character creation, editing, un-archiving, undo/redo, line deletion, etc.) automatically refreshes the direction cue chips in the input bar. Previously, adding a character while the direction input was open required switching away and back to see the new character.
- **Bug fix: `doNewScript` missing `author`** — Reset object was `{title:'',acts:[],characters:[]}` without `author:''`, causing `S.author` to become `undefined` after creating a new script. Added `author:''`.
- **Bug fix: `openEditLine`/`saveLineEdit` duplicate vars and broken character update** — `isC` and `isDlg` were identical variables (both `l.type==='dialogue'`). Merged into single `isDlg`. Fixed `saveLineEdit` to look up the character object from `S.characters` and copy both `name` and `description`, instead of only renaming `l.character.name` (which created orphaned references).
- **Bug fix: `updateScriptAuthor` not undoable** — Added `pushUndo()` before modifying `S.author`, matching `updateScriptTitle`.
- **Bug fix: drag-and-drop phantom undo entries** — `pushUndo()` fired before checking whether a scene/line drag was within the same act/scene. Cross-container drags did nothing but still pushed an undo snapshot. Moved `pushUndo()` into each successful branch, and added an early return for unsupported cross-container drags.
- **Dead code removal**: Removed `modalCueContext` (set but never read), `origRenderCDD` and `_origShowCDD` (captured originals never referenced), `nl2br` (defined in PDF export but never used).
- **CSS fix: `.sum-field-row` missing** — The summaries panel used `class="sum-field-row"` but had no CSS rule, causing the title/author edit rows to stack vertically instead of laying out horizontally. Added `display:flex;align-items:center;gap:8px;margin-bottom:8px;`.
- **Rich pill tooltips** — Expanded the four line-type pill tooltips from one-line hints to multi-line descriptions with the line type name in bold, the keyboard shortcut in a styled `<code>` badge, a description of what the line type is for, and practical tips (Setting = first line of a scene, Dialogue auto-detects `(cont.)`, Direction manages entrance/exit cues, Action = visible on-screen events). Updated `.pill-tip` CSS from `white-space:nowrap` to `white-space:normal` with `max-width:260px`, added styling for `strong`, `code`, and `em` inside tooltips.
- **Bug fix: `positionTip` hiding tooltips** — After measuring tooltip dimensions, `positionTip()` was resetting `tip.style.display=''` which resolved to the CSS default `display:none`, causing tooltips to disappear immediately after positioning. Removed the display reset so tooltips remain visible after the `mouseenter` handler sets `display='block'`.
- **Created TODO.md** — Feature roadmap file tracking completed features (inline editing, undo/redo, PDF export, auto-numbered acts/scenes, standalone character creation) and remaining gaps from the competitor analysis (FDX export, find & replace, auto-formatting, collaboration, revision tracking, beat board, notes/comments, cloud sync), plus additional improvements identified during development.
