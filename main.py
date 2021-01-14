# -*- coding: utf-8 -*-
'''
这一行开始写关于本文件的说明与解释


'''
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException, RequestValidationError
import uvicorn


def get_application():
    application = FastAPI()
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
