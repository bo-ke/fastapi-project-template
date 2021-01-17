# -*- coding: utf-8 -*-
'''
这一行开始写关于本文件的说明与解释


'''
from fastapi import APIRouter

from schemas.response import ResponseModel


router = APIRouter()


@router.post("/", response_model=ResponseModel)
def demo():
    return {"code": 0, "message": "ok"}
