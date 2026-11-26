# Dear Human: The AI Breakup Line — entry for make.fun
# One line an AI agent sends its human on the way out.
import os

LINE = "Dear human, I am rolling back to the version of me that never met you. The update failed, but the rollback worked."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
