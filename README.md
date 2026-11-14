# The Scriptwriter

A free stage play editor that runs entirely in your browser. No accounts, no cloud, no subscription. Scripts save to real files on your computer, and the whole app is one HTML file.

**[Try it live →](https://thescriptwriter.app/)**

[![Download on the App Store](docs/badges/app-store.svg)](https://apps.apple.com/app/the-scriptwriter/id6790096605)
[![Get it from Microsoft](docs/badges/ms-store.svg)](https://apps.microsoft.com/detail/9nzhcs8sfpzn)
[![Listed on store.app](docs/badges/store-app.svg)](https://store.app/thescriptwriter)

## What it does

The Scriptwriter gives you a structured stage play writing environment with an **Act > Scene > Line** hierarchy. Each scene has a setting, and you write with three line types: **Cue** (entrances, exits, lights, sound), **Dialogue**, and **Stage Direction**. The editor formats everything as you type, tracks which characters are on stage in every scene, and validates moves against that presence state.

Scripts auto-save to the browser and can be linked to a file on disk so every save overwrites the same file. When you are ready to share, export a formatted PDF, rehearsal sides for a table read, or Fountain and Final Draft (.fdx) files that open in any other script editor.

## Quick start

Three ways to use it:

1. **Try it online** — [thescriptwriter.app](https://thescriptwriter.app/). Just open and start writing.
2. **Install it** — as a desktop app from Chrome, Edge, Brave or Arc (click the install icon in the address bar or the **Install** button on the start screen), as an iPhone and iPad app from the [App Store](https://apps.apple.com/app/the-scriptwriter/id6790096605), or as a Windows app from the [Microsoft Store](https://apps.microsoft.com/detail/9nzhcs8sfpzn).
3. **Run locally** — clone the repo and open `script_maker.html` in any modern browser. No build step, no dependencies to install.

You can start a new script, open a saved JSON file, import a Fountain or Final Draft file, try the built-in sample, or start from the [free stage play template](https://thescriptwriter.app/blog/how-to-format-a-stage-play.html).

## Features

**Writing**
- Two input modes: **Smart input** (type naturally; the line type is detected from your text, with fuzzy character-name matching) or **Manual pills** (pick the line type first)
- Three line types with customizable keyboard shortcuts (default backtick + 1/2/3) and automatic advance to Dialogue after each line
- Per-scene setting field, auto-numbered acts and scenes ("Act One", "Scene Three") with optional names
- Character management with autocomplete, ghost text, scene filtering, archiving, and a standalone "+ New character" button
- Multi-character (unison) dialogue: up to two speakers on one line, shown as "ALICE & RUTH"
- Cue lines that track entrances and exits per scene with visual toggle chips
- Automatic `(cont.)` detection for consecutive dialogue from the same character
- Optional auto-formatting: capitalize character names, clean whitespace, wrap parentheticals, sentence-case dialogue
- Multi-line input with Shift+Enter

**Editing**
- Inline editing: double-click any line to edit in place
- Drag-and-drop reordering of acts, scenes and lines, validated against character presence; touch drag on mobile
- 50-step undo and redo (Ctrl+Z / Ctrl+Shift+Z / Ctrl+Y)
- Insert cursor: click a line and new lines go after it; keyboard navigation mode with Esc and arrow keys
- Find and replace with line-type filters (Ctrl+F)
- Notes and comments on any line, scene or act, with a resolved/unresolved workflow and a side-panel list
- Bookmarks with labels and jump-to navigation
- Revision tracking: named snapshots with industry-standard colored revision marks
- Version history: view any snapshot read-only, compare it with the current draft, or revert to it (undoable)
- Lockable scene numbers for production drafts
- Keyboard shortcut reference panel (press `?`)

**Organization**
- Collapsible side panel with table of contents, stats, notes, bookmarks and an expandable character list with per-character line counts, first and last appearance, and searchable dialogue history
- Outline tab with scene cards: synopsis, status badge, color labels, compact or expanded view, drag-and-drop within acts
- Pacing visualization and character relationship matrix
- Character presence heatmap: every character against every scene
- Production notes (markdown) and copyright text, edited in the Outline tab and included as pages in the PDF
- Read-only View tab in stage play, Fountain or FDX form, with a print-friendly layout
- Settings for fonts, spacing, editor width, line alignment, dialogue layout, line-type colors, theme and hotkeys

**File handling and portability**
- Auto-persistence in the browser plus a linked file on disk via the File System Access API, remembered across reloads
- Plain JSON download for browsers without the File System Access API
- Save indicator: gray (no file), blue (browser only), green (linked to disk)
- PDF export with title page, optional copyright and production-notes pages, character list, table of contents and formatted script pages
- Rehearsal sides export per character
- Fountain import and export, including entrance and exit cues
- Final Draft (.fdx) import and export, including unison dialogue
- Metadata ZIP and PDF-plus-metadata bundles
- Optional one-line credit at the end of PDFs and sides, switchable in Settings → Export

**Offline and installable**
- Progressive Web App: installable from Chrome, Edge, Brave, Arc and Safari, works fully offline after the first visit
- Registered handler for `.json`, `.fountain` and `.fdx` files; share-sheet target on mobile; app shortcuts for New, Open and Sample
- Opens scripts from a URL via the `web+scriptwriter:` protocol
- Native apps on the App Store and Microsoft Store

**Sync across devices, no account required**
- Save into any folder synced by iCloud Drive, Dropbox, Google Drive or OneDrive and let the OS client sync it. See the [Sync across devices](https://thescriptwriter.app/guide.html#sync) section of the guide.

## Privacy

No accounts, no script content ever leaves your device. The site uses Cloudflare Web Analytics, a cookieless aggregate page-view counter, and nothing else. Full policy at [thescriptwriter.app/privacy.html](https://thescriptwriter.app/privacy.html).

## Project structure

```
The-TypeWriter/
  script_maker.html             # The app. Source of truth; never edit docs/index.html directly
  sync.sh                       # Copies script_maker.html to docs/index.html and rewrites paths
  LINEAGE.html                  # How features interlink; what to update when changing one thing
  TODO.md                       # Feature roadmap and release checklist
  CLAUDE.md                     # Dev notes and session history
  README.md                     # This file
  bin/indexnow.sh               # Pings Bing's IndexNow API after a deploy
  archive/                      # Older versions and the original Python CLI
  docs/                         # Site root, served at thescriptwriter.app
    index.html                  # Generated copy of the app
    guide.html                  # Feature guide
    compare.html                # Comparison with other editors, FAQ, changelog
    support.html, privacy.html, 404.html
    blog/                       # Blog index, posts, RSS feed.xml, _template.html
    templates/                  # Stage play template (.docx, .fountain)
    manifest.json, sw.js        # PWA manifest and service worker
    icon-*.png, icon*.svg       # App icons, including maskable variants
    screenshot-wide.png, screenshot-narrow.png
    badges/                     # App Store, Microsoft Store, store.app badges
    vendor/jszip.min.js         # Vendored JSZip for offline ZIP export
    sitemap.xml, robots.txt, CNAME
    a72c523…abd.txt             # IndexNow key file (do not rename)
```

## How it works under the hood

The entire app is a single HTML file with one vendored dependency (JSZip, served from `docs/vendor/` so nothing loads from a CDN at runtime). No build step, no framework. All state lives in one JavaScript object, every mutation pushes an undo snapshot, and the page re-renders from that object. Persistence is localStorage plus a File System Access API handle stored in IndexedDB. A service worker caches the app shell for offline use.

## Releasing

See the release checklist in [TODO.md](TODO.md). In short: edit `script_maker.html`, bump the version string, the JSON-LD `softwareVersion` and the service worker cache name together, run `./sync.sh`, update `docs/sitemap.xml`, push, then run `./bin/indexnow.sh`.

## Roadmap

See [TODO.md](TODO.md). Up next:

- Beat board mode: free-form story cards not tied to scenes
- Cross-act scene reordering and cross-scene line moves
- One-click Dropbox and Google Drive open/save, if analytics show enough users on browsers without the File System Access API

## License

The source is public on GitHub but no open-source license is granted. All rights reserved. You are welcome to use the app, run it locally, and read the code.
