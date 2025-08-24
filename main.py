
import argparse
from src.pipeline import run_pipeline

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", type=str, default=None, help="Path to strip image (optional).")
    ap.add_argument("--show", action="store_true", help="Visualize intermediate outputs (requires GUI env).")
    args = ap.parse_args()

    result = run_pipeline(args.image, visualize=args.show)
    print("\n=== FINAL RESULT ===")
    print(result)
