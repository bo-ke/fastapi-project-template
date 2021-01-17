# -*- coding: utf-8 -*-
'''
这一行开始写关于本文件的说明与解释


'''
from typing import Optional, Union, Dict, List
from pydantic import BaseModel


class ResponseModel(BaseModel):
    code: Optional[int] = 0
    message: Optional[str] = "ok"
    data: Optional[Union[Dict, List]] = {}
