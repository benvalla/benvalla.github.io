"""Redact contact details and address from the public CV PDF (PyMuPDF)."""
import sys
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "assets" / "Benoit-Valla-CV.pdf"

# Phrases to remove (must match PDF text layer; order does not matter).
PHRASES = [
    "benoitvalla90@gmail.com",
    "+447712428270 (UK)",
    "+33680086389 (FR)",
    "+447712428270",
    "Wayside 1 Gateforth Lane",
    "Hambleton, YO8 9HP",
    "UNITED KINGDOM",
    "Address",
    "Telephone",
    "E-Mail",
]


def main() -> int:
    if not PDF_PATH.is_file():
        print(f"Missing: {PDF_PATH}", file=sys.stderr)
        return 1

    doc = fitz.open(PDF_PATH)
    for page in doc:
        for phrase in PHRASES:
            for rect in page.search_for(phrase, quads=False):
                page.add_redact_annot(rect, fill=(1, 1, 1))
        page.apply_redactions()

    out = PDF_PATH.with_suffix(".redacted.pdf")
    doc.save(out, garbage=4, deflate=True)
    doc.close()
    out.replace(PDF_PATH)
    print(f"Updated: {PDF_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
