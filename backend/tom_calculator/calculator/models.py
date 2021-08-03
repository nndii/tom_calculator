from decimal import Decimal

from pydantic import BaseModel, validator


class CalcValues(BaseModel):
    """Validation model for CalculatorView."""

    price: Decimal
    quantity: Decimal
    state_code: str

    @validator('*')
    def check_positive(cls, v):
        """Decimal values must be positive for calculator."""
        if isinstance(v, Decimal):
            if v < Decimal("0"):
                raise ValueError("can't be negative")

        return v


class CalcTotal(BaseModel):
    """Response model for CalculatorView."""

    total: Decimal
    discounted_total: Decimal
