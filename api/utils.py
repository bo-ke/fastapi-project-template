# -*- coding: utf-8 -*-
'''
这一行开始写关于本文件的说明与解释


'''
from typing import Union, Any
from jose import jwt
from datetime import datetime, timedelta

from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_DAYS


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    """generate token

    Args:
        subject (Union[str, Any]): [description]
        expires_delta (timedelta, optional): [description]. Defaults to None.

    Returns:
        str: [description]
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode = {"exp": expire, "sub": str(subject)}
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encode_jwt
