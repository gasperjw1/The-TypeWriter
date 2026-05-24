# The Scriptwriter

A free, open-source stage play editor that runs entirely in your browser. No accounts, no installs, no cloud — just open the HTML file and start writing.

**[Try it live →](https://thescriptwriter.app/)**  ·  [Listed on store.app](https://store.app/thescriptwriter)

[![Listed on store.app](docs/badges/store-app.svg)](https://store.app/thescriptwriter)

## What it does

The Scriptwriter gives you a structured stage play writing environment with an **Act > Scene > Line** hierarchy. You write using four line types — Setting, Cue, Dialogue, and Stage Direction — and the app handles formatting, numbering, and continuity for you.

Scripts auto-save to your browser's localStorage and can be linked to a file on disk via the File System Access API. When you're ready to share, export to a formatted script PDF or download a metadata ZIP containing the raw JSON for later editing.

## Quick start

Three ways to use it:

1. **Try it online** — [thescriptwriter.app](https://thescriptwriter.app/). Just open and start writing.
2. **Install as a desktop app** — visit the site in Chrome, Edge, Brave, or Arc and click the install icon in the address bar (or use the one-click **Install** button on the start screen). On Safari, use **File → Add to Dock**. The installed app runs in its own window, works fully offline, and registers itself to open `.json`, `.fountain`, and `.fdx` files by double-click.
3. **Run locally** — clone the repo and open `script_maker.html` in any modern browser. No build step, no dependencies to install.

You can start a new script, open a saved JSON file, import a Fountain or Final Draft (.fdx) file, or try the built-in sample script.

## Features

**Writing**
- Two input modes: **Smart input** (type naturally, line type auto-detected from your text with fuzzy character name matching) or **Manual pills** (select a line type pill before typing). Choose at script creation, switch any time in Settings
- Four line types (Setting, Cue, Dialogue, Stage Direction) with customizable keyboard shortcuts (default: backtick + 1/2/3) and smart auto-advance between types
- Character management with autocomplete, ghost text, scene filtering, and archiving
- Cue lines that track character entrances and exits per scene with visual toggle chips
- Automatic `(cont.)` detection for consecutive dialogue from the same character
- Auto-numbered acts and scenes ("Act One", "Scene Three") with optional custom names
- Lockable scene numbers for production drafts — lock to freeze numbering, edit locked numbers inline, numbers persist through reordering

**Editing**
- Inline editing — double-click any line to edit in place, or use the Edit button
- Drag-and-drop reordering for acts, scenes, and lines with validation against character presence
- 50-level undo/redo (Ctrl+Z / Ctrl+Shift+Z) with full state snapshots
- Insert cursor — click a line to insert new content after it
- Find and replace across the script with line-type filter chips (Ctrl+F)
- Revision tracking — create named snapshots, changed lines highlighted with industry-standard colored marks (white, blue, pink, yellow, green, goldenrod) and margin asterisks

**Organization**
- Collapsible side panel with table of contents and expandable character list
- Click a character to see their full description and searchable dialogue history; click any dialogue line to jump to it in the editor
- Summaries tab with script statistics
- Outline tab with scene cards — visual corkboard showing each scene as a card with stats (line count, dialogue count, characters), drag-and-drop reordering within acts, click to jump to scene in editor
- Read-only View tab with act/scene separators for distraction-free reading
- Settings tab for font size, indicator styles, line-type colors, theme override, and pill hotkey customization

**File handling & portability**
- localStorage auto-persistence — your work is saved in the browser automatically
- File System Access API — link to a file on disk and overwrite on each save (no repeated downloads)
- Fallback JSON download for browsers without File System Access API
- Visual save indicator: gray (no file), blue (browser-only), green (linked to disk file)
- PDF export with title page, character list, table of contents, and formatted script pages
- Fountain export/import — the open plain-text script format used by Highland, Beat, and others
- Final Draft (FDX) export/import — the industry-standard XML format for script interchange
- Full round-trip fidelity across formats: FDX → Fountain → FDX preserves all content
- Metadata ZIP download — exports the raw JSON and a manifest for re-importing later
- PDF + metadata export — bundles the print-ready PDF with metadata in a single ZIP

**Navigation**
- Click the app title in the top bar to return to the home screen (prompts to save unsaved work)
- In-app Guide tab with a full feature reference you can read without leaving the editor
- [Compare page](https://thescriptwriter.app/compare.html) showing how The Scriptwriter stacks up against Final Draft, Arc Studio Pro, WriterDuet, and others

**Offline & installable**
- Progressive Web App (PWA) — installable on Chrome, Edge, Brave, Arc, and Safari (macOS 14+ / iOS) with one click
- Runs in its own standalone window once installed — no tabs, no address bar, no browser distractions
- Works fully offline after first visit, including all editing, saving, and exporting
- File-handler registration — installed app opens `.json`, `.fountain`, and `.fdx` files when you double-click them in Finder or Explorer
- Service worker caches the app shell and the (locally vendored) JSZip dependency for true zero-network operation
- App shortcuts — right-click the installed app icon in your dock/taskbar for **New Script** and **Open File**

**Sync across devices (no account required)**
- Save your script into any folder synced by iCloud Drive, Dropbox, Google Drive, or OneDrive — the OS sync client handles cross-device sync for free
- No tokens, no cloud account on our side, no API setup — your files stay your files
- See the [Sync across devices](https://thescriptwriter.app/guide.html#sync) section of the guide for details

**Appearance**
- Dark mode follows your system preference, or override with light/dark in Settings
- Customizable line-type accent colors with per-type enable/disable toggles
- Configurable selected-line indicator (barrier or highlight) with color options

## Project structure

```
The-TypeWriter/
  script_maker.html             # The app (open this)
  sync.sh                       # Syncs docs/index.html from script_maker.html
  docs/
    index.html                  # GitHub Pages copy (generated by sync.sh)
    guide.html                  # Feature guide / manual
    compare.html                # Competitor comparison + changelog landing page
    manifest.json               # PWA web app manifest
    sw.js                       # Service worker for offline support
    icon-192.png / icon-512.png # PWA app icons
    screenshot-wide.png         # PWA install dialog (desktop)
    screenshot-narrow.png       # PWA install dialog (mobile)
    vendor/jszip.min.js         # Vendored JSZip for offline ZIP export
    sitemap.xml                 # SEO sitemap
    robots.txt                  # Crawler directives
  TODO.md                       # Feature roadmap
  CLAUDE.md                     # Dev notes and project memory
  README.md                     # This file
  archive/                      # Older versions kept for reference
```

## How it works under the hood

The entire app is a single HTML file with one vendored dependency (JSZip, served from `docs/vendor/` for true offline operation — no CDN at runtime). No build step, no framework. All state lives in a global JavaScript object (`S`) that maps directly to the JSON save format. The UI re-renders from that object on every change, with undo snapshots captured before each mutation.

## Roadmap

See [TODO.md](TODO.md) for the full list. Up next:

- One-click cloud save/load via Dropbox Chooser/Saver and Google Drive Picker (no account on our side)
- Beat board mode — free-form story cards not tied to scenes
- Cross-act scene reordering and cross-scene line moves

## License

This project is provided as-is for personal and educational use.
