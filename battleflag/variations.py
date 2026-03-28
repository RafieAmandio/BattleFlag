"""Variation engine for generating unique battle configurations."""

import random

# 5+ distinct color palette themes
COLOR_PALETTES = [
    {
        "name": "Nusantara",
        "background": (15, 15, 25),
        "colors": [
            (255, 0, 0), (0, 0, 180), (0, 156, 59),
            (255, 215, 0), (218, 37, 29), (0, 100, 200),
            (128, 0, 128), (255, 140, 0), (0, 128, 128),
            (220, 20, 60), (30, 144, 255), (50, 205, 50),
            (255, 105, 180), (0, 191, 255), (255, 69, 0),
        ],
    },
    {
        "name": "Laut Biru",
        "background": (5, 10, 35),
        "colors": [
            (0, 119, 190), (0, 180, 216), (72, 202, 228),
            (144, 224, 239), (202, 240, 248), (0, 150, 136),
            (38, 166, 154), (0, 200, 83), (100, 221, 23),
            (0, 77, 64), (0, 137, 123), (128, 203, 196),
            (178, 235, 242), (0, 172, 193), (0, 96, 100),
        ],
    },
    {
        "name": "Api Gunung",
        "background": (25, 8, 5),
        "colors": [
            (255, 87, 34), (244, 67, 54), (255, 152, 0),
            (255, 193, 7), (255, 235, 59), (183, 28, 28),
            (230, 74, 25), (245, 124, 0), (255, 160, 0),
            (249, 168, 37), (255, 61, 0), (221, 44, 0),
            (191, 54, 12), (255, 111, 0), (255, 214, 0),
        ],
    },
    {
        "name": "Hutan Tropis",
        "background": (8, 20, 10),
        "colors": [
            (27, 94, 32), (56, 142, 60), (76, 175, 80),
            (129, 199, 132), (0, 105, 92), (0, 150, 136),
            (139, 195, 74), (205, 220, 57), (255, 235, 59),
            (174, 213, 129), (67, 160, 71), (46, 125, 50),
            (51, 105, 30), (85, 139, 47), (100, 221, 23),
        ],
    },
    {
        "name": "Senja Pantai",
        "background": (20, 10, 25),
        "colors": [
            (233, 30, 99), (156, 39, 176), (103, 58, 183),
            (63, 81, 181), (255, 64, 129), (224, 64, 251),
            (179, 136, 255), (255, 128, 171), (130, 177, 255),
            (234, 128, 252), (255, 82, 82), (255, 171, 64),
            (255, 213, 79), (186, 104, 200), (149, 117, 205),
        ],
    },
    {
        "name": "Emas Kerajaan",
        "background": (18, 12, 5),
        "colors": [
            (255, 215, 0), (218, 165, 32), (184, 134, 11),
            (255, 193, 7), (255, 160, 0), (245, 127, 23),
            (230, 81, 0), (255, 111, 0), (255, 152, 0),
            (251, 192, 45), (255, 179, 0), (255, 143, 0),
            (224, 168, 0), (192, 149, 24), (255, 234, 0),
        ],
    },
]

# 20+ Indonesian-relevant team/country names
TEAM_NAMES = [
    "Indonesia", "Malaysia", "Thailand", "Filipina", "Vietnam",
    "Jepang", "Korea", "Brasil", "Jerman", "Prancis",
    "Singapura", "Brunei", "Kamboja", "Myanmar", "Laos",
    "India", "Tiongkok", "Australia", "Mesir", "Turki",
    "Argentina", "Belanda", "Portugal", "Spanyol", "Italia",
    "Inggris", "Meksiko", "Kolombia", "Maroko", "Senegal",
]

# Battle title templates in Bahasa Indonesia
BATTLE_TITLES = [
    "Pertarungan Lingkaran Epik!",
    "Perang Besar Lingkaran",
    "Duel Lingkaran Mematikan",
    "Arena Pertempuran Lingkaran",
    "Siapa yang Bertahan?",
    "Pertarungan Sengit!",
    "Clash Lingkaran Raksasa",
    "Babak Final Lingkaran",
    "Pertarungan Tak Terduga!",
    "Perang Antar Negara",
    "Lingkaran vs Lingkaran!",
    "Pertarungan Gila-Gilaan!",
    "Duel Seru Lingkaran",
    "Siapa Juaranya?",
    "Pertarungan Dahsyat!",
    "Perang Lingkaran Seru!",
    "Battle Royale Lingkaran",
    "Turnamen Lingkaran Besar",
    "Pertarungan Abadi!",
    "Lingkaran Mana Terkuat?",
]


def generate_variation(seed=None):
    """Generate a unique battle configuration.

    Returns a dict with all randomized parameters for one video.
    """
    if seed is not None:
        random.seed(seed)

    palette = random.choice(COLOR_PALETTES)
    num_circles = random.randint(6, 15)
    selected_names = random.sample(TEAM_NAMES, num_circles)
    selected_colors = random.sample(palette["colors"], min(num_circles, len(palette["colors"])))
    title = random.choice(BATTLE_TITLES)

    teams = [
        {"name": name, "color": color}
        for name, color in zip(selected_names, selected_colors)
    ]

    return {
        "num_circles": num_circles,
        "teams": teams,
        "title": title,
        "palette_name": palette["name"],
        "background_color": palette["background"],
    }
