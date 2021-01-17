# -*- coding: utf-8 -*-
'''
这一行开始写关于本文件的说明与解释


'''
from fastapi import APIRouter

from api.routes import demo

router = APIRouter()
router.include_router(demo.router, tags=["demo"], prefix="/demo")
