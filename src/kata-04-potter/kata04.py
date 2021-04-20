from __future__ import annotations

BOOK_PRICE = 8
DISCOUNTS = [0.00, 0.00, 0.05, 0.10, 0.20, 0.25]


class OrderError(Exception):
    pass


def order_total(book_counts: list[int]) -> float:

    if len(book_counts) > len(DISCOUNTS) - 1:
        raise OrderError("We don't have that many titles in stock!")
    if any([int(i) != i for i in book_counts]):
        pass  # ValueError
    if any([i < 0 for i in book_counts]):
        raise OrderError("You can not ask for a negative number of books.")

    total = 0.0
    while sum(book_counts) > 0:
        books = sum([1 for books in book_counts if books > 0])
        total += (BOOK_PRICE * books) * (1 - DISCOUNTS[books])
        book_counts = [i - 1 for i in book_counts if i > 1]

    return total
