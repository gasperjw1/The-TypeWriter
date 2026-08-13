// Service Worker for The Scriptwriter PWA
const CACHE_NAME = 'scriptwriter-v1.46';
const SHARED_FILES_CACHE = 'scriptwriter-shared-files';
const ASSETS = [
  './',
  './index.html',
  './icon-192.png',
  './icon-512.png',
  './icon-1024.png',
  './icon-maskable-192.png',
  './icon-maskable-512.png',
  './icon-maskable-1024.png',
  './vendor/jszip.min.js'
];

// Install: cache core assets
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

// Activate: clean up old caches (keep app-shell + shared-files caches)
self.addEventListener('activate', e => {
  const keep = new Set([CACHE_NAME, SHARED_FILES_CACHE]);
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => !keep.has(k)).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// Share Target: handle POSTed files from other apps' Share menus.
// Stashes files in SHARED_FILES_CACHE and redirects the user to
// `./?action=share`, which the app consumes on load.
async function handleSharedFiles(request) {
  try {
    const formData = await request.formData();
    const files = formData.getAll('file');
    const cache = await caches.open(SHARED_FILES_CACHE);
    // Clear any leftovers from a previous share
    const oldKeys = await cache.keys();
    await Promise.all(oldKeys.map(k => cache.delete(k)));
    let stored = 0;
    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      if (!file || typeof file === 'string') continue;
      const name = file.name || ('shared-' + i);
      const cacheUrl = './_shared/' + i + '/' + encodeURIComponent(name);
      const response = new Response(file, {
        status: 200,
        headers: {
          'Content-Type': file.type || 'application/octet-stream',
          'X-Shared-Filename': name
        }
      });
      await cache.put(cacheUrl, response);
      stored++;
    }
    const dest = stored > 0 ? './?action=share' : './';
    return Response.redirect(dest, 303);
  } catch (err) {
    console.error('Share target handler failed:', err);
    return Response.redirect('./', 303);
  }
}

// Fetch: route POSTs (share target) through the handler; everything
// else uses cache-first with background network refresh.
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  const scopePath = new URL(self.registration.scope).pathname;

  // Share target POST landing on the scope root
  if (e.request.method === 'POST' && url.pathname === scopePath) {
    e.respondWith(handleSharedFiles(e.request));
    return;
  }

  // Only cache GETs from here on
  if (e.request.method !== 'GET') return;

  // Never intercept the SW-owned shared-files cache URLs — they're
  // consumed directly by the app via caches.open(), not by fetch().
  if (url.pathname.includes('/_shared/')) return;

  // Navigation requests (the HTML document for any page): cache, then
  // network (caching the result), then fall back to the cached app shell.
  // This guarantees a navigation ALWAYS resolves to something offline —
  // even a page that was never visited returns the editor instead of the
  // browser's error page. (This is also the pattern PWA Builder's offline
  // check looks for.)
  if (e.request.mode === 'navigate') {
    e.respondWith(
      caches.match(e.request).then(cached =>
        cached || fetch(e.request).then(response => {
          if (response && response.status === 200) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(e.request, clone));
          }
          return response;
        }).catch(() => caches.match('./index.html'))
      )
    );
    return;
  }

  // Everything else (assets, JSON, etc.): cache-first with background
  // network refresh.
  e.respondWith(
    caches.match(e.request).then(cached => {
      const fetchPromise = fetch(e.request).then(response => {
        if (response && response.status === 200) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(e.request, clone));
        }
        return response;
      }).catch(() => {
        // Network failed — cached version (if any) was already returned
      });
      return cached || fetchPromise;
    })
  );
});
