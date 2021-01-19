# -*- coding: utf-8 -*-
'''
这一行开始写关于本文件的说明与解释


'''
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException, RequestValidationError
import uvicorn

from api.errors import http_error_handler, http422_error_handler
from api.routes.api import router as api_router
from api.responses import APIResponse


def get_application():
    application = FastAPI(default_response_class=APIResponse)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(
        RequestValidationError, http422_error_handler)
    application.include_router(api_router, prefix="/api")
    return application


app = get_application()


@app.get("/")
def check_do():
    return {"code": 0, "message": "ok"}


if __name__ == "__main__":
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=80,
                workers=1)
