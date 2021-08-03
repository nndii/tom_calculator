from aiohttp import web
from aiohttp_pydantic import PydanticView
from aiohttp_pydantic.oas.typing import r200

from tom_calculator.calculator.logic import Calculator
from tom_calculator.calculator.models import CalcTotal, CalcValues
from tom_calculator.toml_config import get_toml_config


class CalculatorView(PydanticView):  # noqa: D101

    async def post(self, values: CalcValues) -> r200[CalcTotal]:
        toml_config = get_toml_config()
        total = Calculator(
            discounts=toml_config.discounts,
            taxes=toml_config.taxes,
            quantity=values.quantity,
            price=values.price,
            state_code=values.state_code,
        ).total()
        return web.json_response(text=total.json())
