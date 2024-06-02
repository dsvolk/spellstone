import os
from typing import Iterable


def walk_vault(vault_dir: str) -> Iterable[str]:
    for root, dirs, files in os.walk(vault_dir):
        dirs[:] = [d for d in dirs if d not in [".trash", ".obsidian"]]
        for file in files:
            if file.endswith(".md"):
                yield os.path.join(root, file)
