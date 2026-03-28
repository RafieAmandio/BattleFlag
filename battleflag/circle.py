"""Circle entity for battle animations."""

import random
import math


class Circle:
    """A circle that participates in battles."""

    def __init__(self, name, color, x, y, radius, score=0):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.score = score
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-3, 3)

    def move(self, width, height):
        """Move the circle and bounce off walls."""
        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.vx *= -1
            self.x = max(self.radius, min(width - self.radius, self.x))

        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.vy *= -1
            self.y = max(self.radius, min(height - self.radius, self.y))

    def collides_with(self, other):
        """Check if this circle collides with another."""
        dist = math.hypot(self.x - other.x, self.y - other.y)
        return dist < (self.radius + other.radius)

    def absorb(self, other):
        """Absorb another circle, growing in size and score."""
        area_gain = math.pi * other.radius ** 2
        new_area = math.pi * self.radius ** 2 + area_gain * 0.3
        self.radius = math.sqrt(new_area / math.pi)
        self.score += 1
