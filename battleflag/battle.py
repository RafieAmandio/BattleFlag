"""Battle simulation engine."""

import random

from battleflag.circle import Circle
from config import (
    VIDEO_WIDTH,
    VIDEO_HEIGHT,
    CIRCLE_MIN_RADIUS,
    CIRCLE_MAX_RADIUS,
    FPS,
    BATTLE_DURATION_SEC,
)

# Country/flag themes for battles
TEAMS = [
    {"name": "Indonesia", "color": (255, 0, 0)},
    {"name": "Malaysia", "color": (0, 0, 180)},
    {"name": "Thailand", "color": (0, 100, 200)},
    {"name": "Filipina", "color": (0, 56, 168)},
    {"name": "Vietnam", "color": (218, 37, 29)},
    {"name": "Jepang", "color": (188, 0, 45)},
    {"name": "Korea", "color": (0, 71, 160)},
    {"name": "Brasil", "color": (0, 156, 59)},
    {"name": "Jerman", "color": (0, 0, 0)},
    {"name": "Prancis", "color": (0, 35, 149)},
]


def create_battle(num_circles=10, teams=None):
    """Create a new battle with randomized circles.

    If teams is provided, use those instead of the default TEAMS list.
    """
    circles = []
    if teams is None:
        teams = random.sample(TEAMS, min(num_circles, len(TEAMS)))
    else:
        teams = teams[:num_circles]

    for team in teams:
        x = random.randint(100, VIDEO_WIDTH - 100)
        y = random.randint(300, VIDEO_HEIGHT - 100)
        radius = random.randint(CIRCLE_MIN_RADIUS, CIRCLE_MAX_RADIUS)
        circles.append(Circle(team["name"], team["color"], x, y, radius))

    return circles


def simulate_frame(circles):
    """Simulate one frame of the battle."""
    for circle in circles:
        circle.move(VIDEO_WIDTH, VIDEO_HEIGHT)

    # Check collisions
    to_remove = []
    for i, c1 in enumerate(circles):
        for j, c2 in enumerate(circles):
            if i >= j or c1 in to_remove or c2 in to_remove:
                continue
            if c1.collides_with(c2):
                if c1.radius >= c2.radius:
                    c1.absorb(c2)
                    to_remove.append(c2)
                else:
                    c2.absorb(c1)
                    to_remove.append(c1)

    for c in to_remove:
        circles.remove(c)

    return circles


def run_battle(num_circles=10, teams=None):
    """Run a full battle simulation, returning frame data."""
    circles = create_battle(num_circles, teams=teams)
    total_frames = FPS * BATTLE_DURATION_SEC
    frames = []

    for _ in range(total_frames):
        simulate_frame(circles)
        frame_data = [
            {
                "name": c.name,
                "color": c.color,
                "x": c.x,
                "y": c.y,
                "radius": c.radius,
                "score": c.score,
            }
            for c in circles
        ]
        frames.append(frame_data)

        if len(circles) <= 1:
            break

    winner = circles[0] if circles else None
    return frames, winner
