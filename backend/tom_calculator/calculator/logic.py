from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from typing import Dict

from tom_calculator.calculator.models import CalcTotal
from tom_calculator.exceptions import InvalidStateCode

cents = Decimal(".01")


@dataclass
class Calculator:
    """Tom's order price calculator."""

    discounts: Dict[Decimal, Decimal]
    taxes: Dict[str, Decimal]
    quantity: Decimal
    price: Decimal
    state_code: str

    def total(self) -> CalcTotal:
        """Calculate total order price.

        Returns:
            CalcTotal: total and discounted price
        """
        raw_total = self.price * self.quantity
        discount_total = raw_total - self.discount(raw_total)
        total = discount_total + self.tax(discount_total)
        return CalcTotal(
            discounted_total=discount_total.quantize(cents, ROUND_HALF_UP),
            total=total.quantize(cents, ROUND_HALF_UP),
        )

    def discount(self, o_value: Decimal) -> Decimal:
        """Calculate discount from order value.

        Args:
            o_value (Decimal): raw order price

        Returns:
            Decimal: discount value
        """
        for bound, value in sorted(self.discounts.items(), reverse=True):
            if o_value >= bound:
                return value * o_value

        return Decimal("0")

    def tax(self, o_value: Decimal) -> Decimal:
        """Calculate tax from order value.

        Args:
            o_value (Decimal): Order price after discount

        Returns:
            Decimal: tax value

        Raises:
            InvalidStateCode: If state_code doesnt exist in taxes config
        """
        try:
            return self.taxes[self.state_code] * o_value
        except KeyError as exc:
            raise InvalidStateCode(exc)
