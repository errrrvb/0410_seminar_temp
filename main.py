"""This is degree calculator for rolling stone."""
from math import pi

CONST_DEGREES = 360


def get_degree(radius: float, time: float, acceleration: float, velocity: float = 0) -> float:
    """Thing that does all the needed calculations for rolling stone.

    Args:
        radius: float - radius of our stone (that is taken as perfect sphere).
        time: folat - time that was taken by stone to roll.
        acceleration: float - acceleration for stone.
        velocity: float default 0 - velocity of stone at the beggining.

    Returns:
        float: float with rounded traveled degree count.

    """
    distance = (velocity * time) + (acceleration * (time ** 2)) / 2
    circle_length = 2 * pi * radius
    return round((distance % circle_length) / circle_length * CONST_DEGREES, 2)
