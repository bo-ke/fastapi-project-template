# -*- coding: utf-8 -*-
'''
这一行开始写关于本文件的说明与解释


'''
import typing
from fastapi.responses import JSONResponse

from logger import logger


class APIResponse(JSONResponse):
    def render(self, content: typing.Any) -> bytes:
        logger.info(f"[服务返回结果]--[{content}]")
        return super().render(content)
