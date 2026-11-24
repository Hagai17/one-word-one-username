"""One Word, One Username, One Reward — a make.fun entry.

The entry is the entrant's own make.fun username, one word, nothing else.
"""

import os

# Verified against the account: this is the entrant's own make.fun handle.
LINE = "zenunderoad17"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
