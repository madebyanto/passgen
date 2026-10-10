#!/usr/bin/env bash
set -eu

if [[ ${EUID} -ne 0 ]]; then
    echo "Requesting administrator privileges to install passgen for all users..."
    exec sudo bash "$0" "$@"
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="/usr/local/bin/passgen"
PROFILE_D="/etc/profile.d/passgen.sh"

install -m 755 "$SCRIPT_DIR/passgen.py" "$TARGET"

if ! printf '%s' "$PATH" | tr ':' '\n' | grep -Fxq "/usr/local/bin"; then
    cat > "$PROFILE_D" <<'EOF'
export PATH="/usr/local/bin:$PATH"
EOF
    chmod 644 "$PROFILE_D"
fi

echo "Installed: $TARGET"
echo "Command available to all users as: passgen"
echo "Open a new terminal or run: source /etc/profile"
