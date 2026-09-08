#!/usr/bin/env bash
# Installs a pre-commit hook that keeps sitemap.xml lastmod dates accurate.
# Run once per clone:  bash scripts/install-hooks.sh
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cat > "$ROOT/.git/hooks/pre-commit" <<'HOOK'
#!/usr/bin/env bash
# Regenerate sitemap.xml so <lastmod> reflects real commit dates, then stage it.
set -e
ROOT="$(git rev-parse --show-toplevel)"
python3 "$ROOT/scripts/build-sitemap.py" >/dev/null 2>&1 || exit 0
git add "$ROOT/sitemap.xml" 2>/dev/null || true
HOOK
chmod +x "$ROOT/.git/hooks/pre-commit"
echo "pre-commit hook installed — sitemap.xml will stay current automatically"
