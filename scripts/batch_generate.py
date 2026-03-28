"""Batch video generation script with variation engine."""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from battleflag.battle import run_battle
from battleflag.renderer import render_video
from battleflag.variations import generate_variation

STOCK_DIR = os.path.join("output", "stock")
MANIFEST_PATH = os.path.join(STOCK_DIR, "stock_manifest.json")

# Bahasa Indonesia hashtags pool
HASHTAG_POOL = [
    "#pertarungan", "#lingkaran", "#battle", "#fyp", "#viral",
    "#seru", "#epik", "#animasi", "#battleflag", "#trending",
    "#perang", "#duel", "#indonesia", "#tiktokindonesia",
    "#konten", "#keren", "#gila", "#shorts", "#reels",
    "#pertempuran", "#juara", "#pemenang", "#turnamen",
]

# Bahasa Indonesia description templates
DESCRIPTION_TEMPLATES = [
    "Pertarungan sengit antara {count} lingkaran! Siapa yang menang? Tonton sampai habis!",
    "{count} lingkaran bertarung sampai tinggal satu! Pemenangnya bikin kaget!",
    "Battle royale lingkaran! {count} peserta, cuma 1 juara! Siapa jagoanmu?",
    "Duel epik {count} lingkaran dari berbagai negara! Hasil akhirnya tak terduga!",
    "Pertarungan gila-gilaan! {count} lingkaran saling serang! Tonton sampai akhir!",
    "Siapa yang paling kuat? {count} lingkaran bertarung habis-habisan!",
]


def load_manifest():
    """Load or initialize stock manifest."""
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH, "r") as f:
            return json.load(f)
    return {"videos": [], "total_generated": 0}


def save_manifest(manifest):
    """Save stock manifest."""
    os.makedirs(STOCK_DIR, exist_ok=True)
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


def get_next_stock_number(manifest):
    """Get the next sequential stock number."""
    return manifest["total_generated"] + 1


def generate_metadata(variation, winner_name, stock_number, video_filename):
    """Generate sidecar metadata for a video."""
    import random as _rnd

    count = variation["num_circles"]
    description = _rnd.choice(DESCRIPTION_TEMPLATES).format(count=count)
    hashtags = _rnd.sample(HASHTAG_POOL, min(8, len(HASHTAG_POOL)))

    return {
        "title": variation["title"],
        "description": description,
        "hashtags": hashtags,
        "language": "id",
        "generation_params": {
            "num_circles": variation["num_circles"],
            "palette": variation["palette_name"],
            "background_color": list(variation["background_color"]),
            "teams": [
                {"name": t["name"], "color": list(t["color"])}
                for t in variation["teams"]
            ],
        },
        "winner": winner_name,
        "stock_number": stock_number,
        "video_file": video_filename,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "posting_status": "pending",
    }


def batch_generate(count):
    """Generate N unique battle videos with metadata."""
    manifest = load_manifest()
    os.makedirs(STOCK_DIR, exist_ok=True)
    generated = []

    for i in range(count):
        stock_num = get_next_stock_number(manifest)
        video_name = f"battle_{stock_num:04d}"
        video_filename = f"{video_name}.mp4"

        print(f"\n[{i + 1}/{count}] Membuat video {video_filename}...")

        variation = generate_variation()
        print(f"  Tema: {variation['palette_name']} | "
              f"Lingkaran: {variation['num_circles']} | "
              f"Judul: {variation['title']}")

        frames, winner = run_battle(
            num_circles=variation["num_circles"],
            teams=variation["teams"],
        )
        winner_name = winner.name if winner else "Tidak ada"
        print(f"  Pemenang: {winner_name}")

        print("  Rendering video...")
        output_path = render_video(
            frames,
            output_name=video_name,
            title=variation["title"],
            output_dir=STOCK_DIR,
            background_color=variation["background_color"],
        )

        metadata = generate_metadata(variation, winner_name, stock_num, video_filename)
        metadata_path = os.path.join(STOCK_DIR, f"{video_name}.json")
        with open(metadata_path, "w") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

        manifest["videos"].append({
            "stock_number": stock_num,
            "video_file": video_filename,
            "metadata_file": f"{video_name}.json",
            "title": variation["title"],
            "winner": winner_name,
            "posting_status": "pending",
            "generated_at": metadata["generated_at"],
        })
        manifest["total_generated"] = stock_num
        save_manifest(manifest)

        generated.append(video_filename)
        print(f"  Selesai: {output_path}")

    print(f"\n{'=' * 50}")
    print(f"Batch selesai! {count} video dibuat di {STOCK_DIR}/")
    for vf in generated:
        print(f"  - {vf}")

    return generated


def main():
    parser = argparse.ArgumentParser(
        description="BattleFlag - Batch Video Generator"
    )
    parser.add_argument(
        "--count", type=int, required=True,
        help="Number of unique videos to generate",
    )
    args = parser.parse_args()

    if args.count < 1:
        print("Error: --count harus minimal 1")
        sys.exit(1)

    batch_generate(args.count)


if __name__ == "__main__":
    main()
