#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """public attributes of user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
