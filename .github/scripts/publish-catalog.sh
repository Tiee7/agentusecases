#!/usr/bin/env bash
# Only run in this workflow's clean, disposable checkout. Never force-push.
set -euo pipefail
[ "${GITHUB_ACTIONS:-}" = true ] || { echo 'Requires an isolated Actions checkout'; exit 1; }
[ -z "$(git status --porcelain)" ] || { echo 'Checkout is not clean'; exit 1; }
git config user.name Tiee
git config user.email tieetheai@gmail.com
for attempt in 1 2 3; do
  git fetch origin main
  base=$(git rev-parse origin/main)
  git switch --detach "$base"
  python -m agentwatch.catalog_refresh
  python -m unittest discover -s tests -q
  npm --prefix site ci --ignore-scripts
  npm --prefix site test
  ASTRO_TELEMETRY_DISABLED=1 npm --prefix site run build
  npm --prefix site run check:output
  git diff --check
  git add registry INDEX.md
  if git diff --cached --quiet; then exit 0; fi
  git commit -m 'Refresh catalog from independent daily crawl'
  candidate=$(git rev-parse HEAD)
  if git push origin HEAD:main; then exit 0; fi
  # Resolve an ambiguous push outcome before retrying. Rebuild against new main,
  # rather than rebasing stale generated indexes over a completed research case.
  git fetch origin main
  if git merge-base --is-ancestor "$candidate" origin/main; then exit 0; fi
  if [ "$(git rev-parse origin/main)" = "$base" ]; then
    echo 'Push failed without a competing main update; stop for review'
    exit 1
  fi
  echo "Main changed during publication; regenerate from its current research state (attempt $attempt)"
done
echo 'Main kept changing; leave the crawl artifact for the next publication'
exit 1
