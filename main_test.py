import pytest
from main import get_degree

valid_test_data = (
    (2, 2, 2, 114.59),
    (2, 1, 1.25, 17.9),
    (3, 5, 3.25, 55.88),
    (12, 6, 5, 69.72),
    (15.2, 3.42, 1.29, 28.44)
)


valid_test_data_2 = (
    (2, 2, 2, 2, 229.18),
    (3, 3, 3, 3, 69.72),
    (1.25, 5.31, 9.1, 0.8, 315.2),
)


@pytest.mark.parametrize('radius, time, acceleration, expected', valid_test_data)
def test_valid_data(radius: float, time: float, acceleration: float, expected: float):
    assert get_degree(radius, time, acceleration) == expected


@pytest.mark.parametrize('radius, time, acceleration, velocity, expected', valid_test_data_2)
def test_valid_data_2(radius: float, time: float, acceleration: float, velocity: float, expected: float):
    assert get_degree(radius, time, acceleration, velocity) == expected
