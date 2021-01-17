# -*- coding: utf-8 -*-
'''
这一行开始写关于本文件的说明与解释


'''
from fastapi import HTTPException, Header, status
from jose import jwt

from config import SECRET_KEY, ALGORITHM
from models import SessionLocal
from logger import logger


def get_db():
    """ db Dependency
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def validate_token(token: str = Header(...)):
    """token validation
    """
    try:
        jwt.decode(token, SECRET_KEY, ALGORITHM)
    except jwt.JWTError as e:
        logger.error(repr(e))
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token validation failed",
        )
