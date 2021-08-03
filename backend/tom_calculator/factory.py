from aiohttp import web
from aiohttp_pydantic import oas

from tom_calculator.calculator.routes import register_calc_routes
from tom_calculator.middlewares import catch_client_error
from tom_calculator.toml_config import Settings, get_toml_config


def build_app(loop=None):  # noqa: D103
    app = web.Application(loop=loop, middlewares=[catch_client_error])

    app['settings'] = Settings()
    app['toml_config'] = get_toml_config()

    register_calc_routes(app)
    oas.setup(app, title_spec="Tom's Calculator")

    return app
