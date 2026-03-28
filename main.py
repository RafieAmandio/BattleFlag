"""Main entry point for BattleFlag video generation."""

import argparse
import sys

from battleflag.battle import run_battle
from battleflag.renderer import render_video


def main():
    parser = argparse.ArgumentParser(description="BattleFlag - Battling Circles Video Generator")
    parser.add_argument("--circles", type=int, default=8, help="Number of circles in the battle (default: 8)")
    parser.add_argument("--output", type=str, default="battle", help="Output filename without extension (default: battle)")
    parser.add_argument("--title", type=str, default="Pertarungan Lingkaran", help="Video title text overlay")
    args = parser.parse_args()

    print(f"Simulasi pertarungan dengan {args.circles} lingkaran...")
    frames, winner = run_battle(num_circles=args.circles)

    if winner:
        print(f"Pemenang: {winner.name} (skor: {winner.score})")
    else:
        print("Tidak ada pemenang!")

    print("Rendering video...")
    output_path = render_video(frames, output_name=args.output, title=args.title)
    print(f"Video tersimpan di: {output_path}")


if __name__ == "__main__":
    main()
