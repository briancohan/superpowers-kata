from __future__ import annotations

BOOK_PRICE = 8
DISCOUNTS = {
    1: 0.00,
    2: 0.05,
    3: 0.10,
    4: 0.20,
    5: 0.25,
}


def order_total(book_counts: list[int]) -> float:

    total = 0.0
    while sum(book_counts) > 0:
        books = sum([1 for books in book_counts if books > 0])
        total += (BOOK_PRICE * books) * (1 - DISCOUNTS[books])
        book_counts = [max(0, i - 1) for i in book_counts]

    return total
