#!/usr/bin/python3
""" This module contains a class BaseModel """
import uuid
from datetime import datetime


class BaseModel:
    """Initializes a class BaseModel"""

    def __init__(self):
        """Init method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = None

    def __str__(self):
        """Prints string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Returns a dict containing all key/value pairs of the dict
        representation of the instance, including the class name of the object
        """
        dict_obj = self.__dict__
        dict_obj["__class__"] = __class__.__name__
        return dict_obj

