from http import HTTPStatus


class ClientError(Exception):
    """This exception is going to be catched by middleware."""

    detail = ""
    status_code = HTTPStatus.BAD_REQUEST


class InvalidStateCode(ClientError):  # noqa: D101
    detail = "Invalid State Code"
    status_code = HTTPStatus.BAD_REQUEST
