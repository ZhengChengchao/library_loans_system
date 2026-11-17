import pytest
from src.library_fine import calculate_fine


@pytest.mark.parametrize("days_overdue, expected_fine", [
    (0, 0),        # No overdue days
    (1, 50),       # One overdue day
    (5, 250),      # Multiple overdue days
    (10, 500),     # Ten overdue days
    (11, 550),     # More than ten days (no maximum fine)
    (20, 1000),    # Large number of overdue days
])
def test_calculate_fine_valid(days_overdue, expected_fine):
    # Act
    actual_fine = calculate_fine(days_overdue)
    # Assert
    assert actual_fine == expected_fine


@pytest.mark.parametrize("invalid_days", [
    -1,            # Negative overdue days
    -5,            # Multiple negative days
])
def test_calculate_fine_negative_days(invalid_days):
    # Act & Assert
    with pytest.raises(ValueError):
        calculate_fine(invalid_days)


@pytest.mark.parametrize("invalid_days", [
    "5",           # String instead of integer
    5.0,           # Float instead of integer
    True,          # Boolean instead of integer
    None,          # None instead of integer
])
def test_calculate_fine_invalid_type(invalid_days):
    # Act & Assert
    with pytest.raises(TypeError):
        calculate_fine(invalid_days)
