
# Illumination-Invariant Color Analytics Pipeline (Python Skeleton)

This project provides a modular pipeline implementing:

Input → Capture → Linearization → Color Constancy → ROI Detection → Interference Handling → Kinetic Modeling → Calibration & ML → QC & Uncertainty → Final Result

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py --image sample_strip.png
```

If you don't provide `--image`, a synthetic strip image will be generated so you can see the pipeline run end‑to‑end.

## Project Structure

```
src/
  capture.py           # Step 1
  linearization.py     # Step 2
  color_constancy.py   # Step 3
  roi.py               # Step 4
  interference.py      # Step 5
  kinetics.py          # Step 6
  features.py          # feature extraction shared utilities
  calibration.py       # Step 7
  qc.py                # Step 8
  pipeline.py          # Orchestrates the steps
  config.py            # Tunables
main.py                # Entry point
requirements.txt
```

## Notes

- All steps are **minimal, safe defaults**. Replace stubs with your lab/device logic.
- Models are persisted in-memory for demo; swap with your storage or training pipeline.
- Uses simple bootstrapping for CI and basic QC checks.
