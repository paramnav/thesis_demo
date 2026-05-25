#!/usr/bin/env python3
"""
Generate QR code PNG files for the printed thesis.

Usage:
  pip install qrcode[pil]
  python generate_qr_codes.py
  python generate_qr_codes.py --base https://YOUR_USERNAME.github.io/marine-sediment-ml-demos

Output: qr/*.png next to this script
"""

from __future__ import annotations

import argparse
from pathlib import Path

import qrcode

ROOT = Path(__file__).resolve().parent
QR_DIR = ROOT / "qr"

# (filename stem, path relative to site root, caption for LaTeX)
EXPERIMENTS = [
    ("qr_index", "", "All experiments"),
    ("qr_exp6", "exp6_cart_split.html", "CART split"),
    ("qr_exp1", "exp1_3d_surfaces.html", "3D RF vs MLP surfaces"),
    ("qr_exp2", "exp2_zoom_maps.html", "Zoomable RF vs MLP maps"),
    ("qr_exp3", "exp3_knn_slider.html", r"$k$-NN bandwidth"),
    ("qr_exp4", "exp4_rf_depth_slider.html", "Random forest depth"),
    ("qr_exp4b", "exp4b_rf_trees_slider.html", "Random forest trees"),
    ("qr_exp5", "exp5_mlp_slider.html", "MLP architecture and activation"),
]


def make_qr(url: str, out: Path, box_size: int = 8, border: int = 2) -> None:
    img = qrcode.make(url, box_size=box_size, border=border)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print(out)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base",
        default="https://paramnav.github.io/thesis_demo",
        help="GitHub Pages base URL (no trailing slash)",
    )
    args = parser.parse_args()
    base = args.base.rstrip("/")

    for stem, path, _ in EXPERIMENTS:
        url = base if not path else f"{base}/{path}"
        make_qr(url, QR_DIR / f"{stem}.png")

    print(f"\nWrote {len(EXPERIMENTS)} QR codes to {QR_DIR}/")
    print("In LaTeX, set \\DemoBaseUrl to the same base URL (see thesis_interactive.tex).")


if __name__ == "__main__":
    main()
