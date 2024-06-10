from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

point = Point(2, 3)
print(f"Point: ({point.x}, {point.y})")
