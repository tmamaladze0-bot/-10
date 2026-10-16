# def show_booking (movie, *seats, **extras ):
#     print(movie)
#     print(len(seats))
#     print(extras)
#
# show_booking("დიუნა", "A1", "B3", "C5", popcorn=2, cola=1)

EXTRA_PRICES = {
    "popcorn": 6,
    "cola": 3,
    "nachos": 7
}

def book_tickets(movie, *seats, discount=0, **extras):
    valid_seats = list(filter(lambda seat: seat[0] in ("A", "B", "C", "D", "E") and 1 <= int(seat[1:]) <= 10, seats))
    rejected = len(seats) - len(valid_seats)
    prices = list(map(lambda seat: 15 if seat[0] in ("A", "B") else 10 , valid_seats))
    ticket_total = sum(prices)
    discounted_total = ticket_total - ticket_total * discount / 100
    extras_total = 0
    for product, quantity in extras.items():
        extras_total += EXTRA_PRICES[product] * quantity
    total = round(discounted_total + extras_total, 2)
    return {"movie": movie, "seats": valid_seats, "rejected": rejected, "total": total}
result = book_tickets("დიუნა", "A5", "Z1", "C3", "B12", "E10")
print(result)