# -*- coding: utf-8 -*-
'''
这一行开始写关于本文件的说明与解释


'''
from typing import Union
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({"code": exc.status_code, "message": exc.detail}, status_code=200)


async def http422_error_handler(
    _: Request,
    exc: Union[RequestValidationError, ValidationError],
) -> JSONResponse:
    return JSONResponse(
        {"code": status.HTTP_422_UNPROCESSABLE_ENTITY, "message": exc.errors()},
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )
