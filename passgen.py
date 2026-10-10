#!/usr/bin/env python3
"""Generate a secure random password."""

import argparse
import secrets
import string

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>/?~"
AMBIGUOUS = "0OIl1|`'\"\\"
ALPHABET = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS


def generate(length, *, require_all=True, excluded_chars=""):
    """Generate a password of the specified length.

    By default, the password includes at least one lowercase letter,
    one uppercase letter, one digit, and one symbol.
    """
    if not isinstance(length, int):
        raise TypeError("length must be an integer")
    if length <= 0:
        raise ValueError("length must be positive")

    excluded = set(AMBIGUOUS) | set(excluded_chars)
    allowed = "".join(character for character in ALPHABET if character not in excluded)

    if not allowed:
        raise ValueError("no characters available after exclusions")

    if require_all:
        if length < 4:
            raise ValueError("length must be at least 4 when require_all is True")

        required = [
            secrets.choice(LOWERCASE),
            secrets.choice(UPPERCASE),
            secrets.choice(DIGITS),
            secrets.choice(SYMBOLS),
        ]
        remaining = length - len(required)
        password = required + [secrets.choice(allowed) for _ in range(remaining)]
        secrets.SystemRandom().shuffle(password)
        return "".join(password)

    return "".join(secrets.choice(allowed) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description="Generate a secure random password")
    parser.add_argument("length", type=int, nargs="?", default=16,
                        help="password length (default: 16)")
    parser.add_argument("--no-require-all", action="store_true",
                        help="disable the default requirement to include lowercase, uppercase, digit, and symbol")
    parser.add_argument("--exclude", default="",
                        help="extra characters to exclude from the generated password")
    args = parser.parse_args()

    if args.length < 1:
        parser.error("length must be at least 1")

    print(generate(args.length, require_all=not args.no_require_all,
                  excluded_chars=args.exclude))


if __name__ == "__main__":
    main()