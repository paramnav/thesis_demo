# thesis_demo

Interactive browser demos for the dissertation (Chapter 1).

**GitHub Pages:** enable **Settings → Pages →** branch `main`, folder **`/docs`**.

**Site URL:** https://paramnav.github.io/thesis_demo/

| Page | Description |
|------|-------------|
| [index.html](docs/index.html) | Landing page |
| [exp6_cart_split.html](docs/exp6_cart_split.html) | 1D CART split slider ($\Delta$) |
| [exp3_knn_slider.html](docs/exp3_knn_slider.html) | $k$-NN bandwidth |
| [exp4_rf_depth_slider.html](docs/exp4_rf_depth_slider.html) | RF `max_depth` |
| [exp4b_rf_trees_slider.html](docs/exp4b_rf_trees_slider.html) | RF `n_estimators` |
| [exp5_mlp_slider.html](docs/exp5_mlp_slider.html) | MLP layers / activation |

## Update from the dissertation project

```bash
cd /path/to/Dissertation/interactive-demo
bash publish_thesis_demo.sh ~/work/thesis_demo
cd ~/work/thesis_demo
git add -A && git commit -m "Update demos" && git push
```

## QR codes for the printed thesis

```bash
pip install 'qrcode[pil]'
python generate_qr_codes.py --base https://paramnav.github.io/thesis_demo
```

Copy `qr/*.png` to `Dissertation/interactive-demo/qr/` and set `\DemoBaseUrl` in `thesis_interactive.tex`.
