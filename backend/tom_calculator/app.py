import asyncio

from tom_calculator.factory import build_app

loop = asyncio.get_event_loop()
app = build_app(loop)
