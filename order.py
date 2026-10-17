"""One sales order's data and related behavior."""

from pricing import calculate_final_total, classify_order


class SalesOrder:
    """Represent one order, not the whole list of orders."""

    def __init__(self, order_id, unit_price, quantity, discount_pct, tax_pct):
        self.order_id = order_id
        self.unit_price = unit_price
        self.quantity = quantity
        self.discount_pct = discount_pct
        self.tax_pct = tax_pct

    def final_total(self):
        return calculate_final_total(
            self.unit_price,
            self.quantity,
            self.discount_pct,
            self.tax_pct,
        )

    def band(self):
        return classify_order(self.final_total())
