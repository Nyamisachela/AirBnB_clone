#!/usr/bin/python3
import datetime
import uuid


class BaseModel:
    """BaseModel Class : This is the base for all functionality"""

    def __init__(self, *args, **kwargs):
        """
        Initialize Object instance
        If **kwargs is true use it to reconstruct object contained therein
        IF NOT create a new instance
        """
        if not not kwargs:
            t_keys = {"created_at", "updated_at"}
            self.__dict__ = {key:
                             (value.isoformat() if key in t_keys else value)
                             for key, value in kwargs.items()
                             if key != "__class__"}

            for key, value in kwargs.items():
                if key == "__class__":
                    setattr(self, key, value)

        else:
            self.name: str = None
            self.my_number: int = None
            self.id = str(uuid.uuid4())
            self.created_at: datetime = datetime.datetime.now()
            self.created_at.isoformat()
            self.updated_at: datetime = self.created_at

    def save(self):
        """Update the property updated_at with the current timestamp"""
        self.updated_at = datetime.datetime.now()
        self.updated_at.isoformat()

    def to_dict(self):
        """Get object and class attributes, write them to self.my_dict"""
        v_dict = self.__dict__.copy()
        v_dict["__class__"] = self.__class__.__name__
        for key, value in v_dict.items():
            if key in ["created_at", "updated_at"]:
                v_dict[key] = str(value.isoformat())
        return v_dict

    def __str__(self):
        """Return class name, id and __dict__ formatted as a string"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__)
        )


if __name__ == "__main__":
    base_model = BaseModel(params=None, dict=None)
