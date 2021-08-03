from aiohttp.web import json_response, middleware

from tom_calculator.exceptions import ClientError


@middleware
async def catch_client_error(request, handler):
    try:
        resp = await handler(request)
    except ClientError as exc:
        resp = json_response(
            {
                "detail": exc.detail,
            },
            status=exc.status_code.value,
        )
    return resp
