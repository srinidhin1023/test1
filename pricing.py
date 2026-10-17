"""Reusable sales-order pricing rules from the earlier records exercise."""


def calculate_final_total(unit_price, quantity, discount_pct, tax_pct):
    """Return the total after discount, then tax; keep the numeric value unrounded."""
    subtotal = unit_price * quantity
    discount_amount = subtotal * discount_pct / 100
    discounted_subtotal = subtotal - discount_amount
    tax_amount = discounted_subtotal * tax_pct / 100
    final_total = discounted_subtotal + tax_amount
    return final_total


def classify_order(total):
    """Return the order band using the 950.0 threshold."""
    if total >= 950.0:
        return "large"
    return "standard"
