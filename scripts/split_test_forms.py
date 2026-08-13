#!/usr/bin/env python3
"""Split test forms into student copies (no answers) + teacher answer keys."""
import re
import os

TESTS_DIR = os.path.join(os.path.dirname(__file__), "..", "tests")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "tests")

FORMS = [
    "GRAMMAR_TEST_FORM_A.md",
    "GRAMMAR_TEST_FORM_B.md",
    "GRAMMAR_TEST_FORM_C.md",
    "VOCABULARY_TEST_FORM_A.md",
    "VOCABULARY_TEST_FORM_B.md",
    "VOCABULARY_TEST_FORM_C.md",
]


def strip_checkmarks(line: str) -> str:
    """Remove ✓ marks from MCQ option lines."""
    return re.sub(r"\s*✓", "", line)


def split_form(content: str):
    """Split content into student part and answer key part."""
    # Find the answer key section marker
    answer_markers = [
        "## 📝 Answer Key",
        "## Answer Key",
        "## Answer key",
        "## ANSWER KEY",
    ]
    split_idx = len(content)
    for marker in answer_markers:
        idx = content.find(marker)
        if idx != -1:
            split_idx = idx
            break

    student_part = content[:split_idx].rstrip()
    answer_part = content[split_idx:].rstrip() if split_idx < len(content) else ""

    return student_part, answer_part


def process_form(filename: str):
    filepath = os.path.join(TESTS_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into student + answer key
    student_raw, answer_key = split_form(content)

    # Strip ✓ marks from student copy
    student_lines = []
    for line in student_raw.split("\n"):
        # Only strip ✓ from MCQ option lines (lines starting with A) B) C) D) or similar)
        if re.match(r"^\s*[A-D][\)\.]\s", line):
            student_lines.append(strip_checkmarks(line))
        else:
            student_lines.append(line)
    student_clean = "\n".join(student_lines)

    # Add note at top of student copy
    student_clean = student_clean.replace(
        "---\n\n## Instructions",
        "---\n\n> **Teacher copy with answer key available separately.**\n\n## Instructions",
        1,
    )

    # Generate output filenames
    base = filename.replace(".md", "")
    student_file = os.path.join(OUTPUT_DIR, f"{base}_STUDENT.md")
    answer_file = os.path.join(OUTPUT_DIR, f"{base}_ANSWER_KEY.md")

    # Write student copy
    with open(student_file, "w", encoding="utf-8") as f:
        f.write(student_clean + "\n")
    print(f"  [+] Student: {os.path.basename(student_file)}")

    # Write answer key
    if answer_key:
        # Add header to answer key
        form_label = base.replace("_TEST_FORM", " Test Form").replace("_", " ")
        answer_header = f"# 📝 Answer Key — {form_label}\n\n"
        if "Answer Key" not in answer_key[:100]:
            answer_key = answer_header + answer_key
        with open(answer_file, "w", encoding="utf-8") as f:
            f.write(answer_key + "\n")
        print(f"  [+] Answer key: {os.path.basename(answer_file)}")


def main():
    print("=== Splitting test forms into student + teacher copies ===\n")
    for form in FORMS:
        print(f"Processing {form}...")
        process_form(form)
        print()
    print("Done! Student copies have no ✓ marks. Answer keys are separate files.")


if __name__ == "__main__":
    main()
