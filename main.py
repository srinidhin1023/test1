"""Run the sales-order project from its project folder."""

import csv
import sys
from pathlib import Path

import pricing
from order import SalesOrder


DATA_FILE = Path("data") / "S09_orders.csv"


def show_import_demo():
    """Show an imported pricing function without constructing an order."""
    total = pricing.calculate_final_total(250.0, 4, 10.0, 5.0)
    print("Imported pricing.calculate_final_total from pricing.py")
    print(f"Example total: {total:.2f}")
    print("Example band:", pricing.classify_order(total))


def show_two_orders():
    """Try two independent objects before processing the CSV file."""
    first = SalesOrder("ORD-1001", 250.0, 4, 10.0, 5.0)
    second = SalesOrder("ORD-1002", 250.0, 5, 10.0, 5.0)

    for order in (first, second):
        print(order.order_id, "quantity:", order.quantity,
              "total:", f"{order.final_total():.2f}", "band:", order.band())

    # This changes one object in memory only. It does not edit the CSV file.
    first.quantity = 5
    print("After changing the first object's quantity to 5:")
    print(first.order_id, "total:", f"{first.final_total():.2f}", "band:", first.band())
    print(second.order_id, "quantity remains:", second.quantity)


def load_orders():
    """Convert CSV text to numbers, then make one object per row."""
    if not DATA_FILE.is_file():
        raise FileNotFoundError(
            f"Cannot find {DATA_FILE}. Open a terminal in sales-order-project "
            "and run main.py from there."
        )

    orders = []
    with DATA_FILE.open(mode="r", encoding="utf-8", newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            order = SalesOrder(
                row["order_id"],
                float(row["unit_price"]),
                int(row["quantity"]),
                float(row["discount_pct"]),
                float(row["tax_pct"]),
            )
            orders.append(order)

    if not orders:
        raise ValueError(f"No order records found in {DATA_FILE}")
    return orders


def show_all_orders():
    """Report every order and summarize the two bands."""
    orders = load_orders()
    large_count = 0
    standard_count = 0

    for order in orders:
        total = order.final_total()
        band = order.band()
        print(f"{order.order_id}: {order.unit_price:.2f} x {order.quantity} "
              f"-> {total:.2f} ({band})")
        if band == "large":
            large_count += 1
        elif band == "standard":
            standard_count += 1

    print(f"Orders: {len(orders)} | Large: {large_count} | Standard: {standard_count}")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--orientation":
        show_import_demo()
    elif len(sys.argv) == 2 and sys.argv[1] == "--two":
        show_two_orders()
    elif len(sys.argv) == 1:
        show_all_orders()
    else:
        print("Run: python main.py [--orientation | --two]")
        raise SystemExit(2)
