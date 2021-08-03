from aiohttp.web_app import Application

from tom_calculator.calculator.views import CalculatorView


def register_calc_routes(app: Application):
    app.router.add_view("/calculator", CalculatorView)
