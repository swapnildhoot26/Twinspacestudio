#!/usr/bin/env bash
# Installs a pre-commit hook that keeps sitemap.xml lastmod dates accurate and
# stamps the CSS/JS references with a content hash for cache busting.
# Run once per clone:  bash scripts/install-hooks.sh
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cat > "$ROOT/.git/hooks/pre-commit" <<'HOOK'
#!/usr/bin/env bash
set -e
ROOT="$(git rev-parse --show-toplevel)"
python3 "$ROOT/scripts/version-assets.py" >/dev/null 2>&1 || true
python3 "$ROOT/scripts/build-sitemap.py"  >/dev/null 2>&1 || true
git add "$ROOT/sitemap.xml" 2>/dev/null || true
git add "$ROOT"/*.html "$ROOT"/services/*.html "$ROOT"/areas/*.html "$ROOT"/projects/*.html 2>/dev/null || true
HOOK
chmod +x "$ROOT/.git/hooks/pre-commit"
echo "pre-commit hook installed — sitemap and asset versions stay current"
