"""Rename this pack: python rename.py <new-id> ["<New name>"]

Replaces the template's id `my-pack` (and the name "My pack") in every file that carries it, renames
`commands/my-pack.md` to `commands/<new-id>.md`, then deletes itself. Run it once, right after you take the template.
The id must match ^[a-z][a-z0-9-]*$ (the rule `halo pack inspect` checks)."""
import re
import sys
from pathlib import Path

OLD_ID, OLD_NAME = "my-pack", "My pack"
SKIP_DIRS = {".git", "__pycache__", "node_modules"}


def main() -> int:
    if len(sys.argv) < 2 or not re.fullmatch(r"[a-z][a-z0-9-]*", sys.argv[1]):
        print(__doc__)
        return 2
    new_id = sys.argv[1]
    new_name = sys.argv[2] if len(sys.argv) > 2 else new_id.replace("-", " ").capitalize()
    root = Path(__file__).resolve().parent
    changed = 0
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.name == "rename.py" or SKIP_DIRS & set(p.relative_to(root).parts):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new = text.replace(OLD_ID, new_id).replace(OLD_NAME, new_name)
        if new != text:
            p.write_text(new, encoding="utf-8", newline="\n")
            changed += 1
    entry = root / "commands" / f"{OLD_ID}.md"
    if entry.exists():
        entry.rename(root / "commands" / f"{new_id}.md")
    print(f"renamed {OLD_ID} -> {new_id} ({new_name}) in {changed} file(s); entry command /{new_id}")
    print("next: halo pack test .   then commit")
    Path(__file__).unlink()
    return 0


if __name__ == "__main__":
    sys.exit(main())
