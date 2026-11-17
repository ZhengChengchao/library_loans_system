import pytest
from src.library_eligibility import can_borrow


@pytest.mark.parametrize("active_loans, overdue_books, expected_result", [
    (0, 0, True),     # No active loans or overdue books
    (4, 0, True),     # Below borrowing limit
    (5, 0, False),    # At borrowing limit
    (6, 0, False),    # Exceeds borrowing limit
    (0, 1, False),    # One overdue book
    (4, 2, False),    # Multiple overdue books
    (5, 1, False),    # At borrowing limit with overdue book
])
def test_can_borrow_valid(active_loans, overdue_books, expected_result):
    # Act
    actual_result = can_borrow(active_loans, overdue_books)
    # Assert
    assert actual_result is expected_result


@pytest.mark.parametrize("active_loans, overdue_books", [
    (-1, 0),          # Negative active loans
    (0, -1),          # Negative overdue books
])
def test_can_borrow_negative_values(active_loans, overdue_books):
    # Act & Assert
    with pytest.raises(ValueError):
        can_borrow(active_loans, overdue_books)


@pytest.mark.parametrize("active_loans, overdue_books", [
    ("4", 0),         # Active loans as string
    (4, "0"),        # Overdue books as string
    (True, 0),       # Active loans as Boolean
    (0, False),      # Overdue books as Boolean
    (4.0, 0),        # Active loans as float
    (0, None),       # Overdue books as None
])
def test_can_borrow_invalid_types(active_loans, overdue_books):
    # Act & Assert
    with pytest.raises(TypeError):
        can_borrow(active_loans, overdue_books)
