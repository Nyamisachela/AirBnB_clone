#!/usr/bin/python3
import datetime
import uuid
# from models.engine.file_storage import FileStorage


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """
        Initialize Object
        if kwargs set then initialize object serialized therein
        else initialize new object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.strptime(
                        value,
                        "%Y-%m-%dT%H:%M:%S.%f")
                    )
                elif key == "__class__":
                    setattr(self, "_BaseModel__class__", value)
                else:
                    setattr(self, key, value)
        else:
            self.my_number: int
            self.name: str
            self.id: str
            self.set_uuid()
            self.timestamp()

    def timestamp(self):
        """
        Get timestamp, format it to ISO
        Initialize created_at and updated_at with timestamp
        """
        now = datetime.datetime.now()
        now.isoformat()
        self.created_at = now
        self.updated_at = now

    def save(self):
        """Update the property updated_at with the current timestamp"""
        self.updated_at = datetime.datetime.now()
        self.updated_at.isoformat()

    def to_dict(self):
        """Get object and class attributes, write them to self.my_dict"""
        self.__dict__["__class__"] = self.__class__.__name__
        self.created_at = str(self.created_at)
        self.updated_at = str(self.updated_at)
        return self.__dict__.copy()

    def set_uuid(self):
        """Get a UUID and assign its value to self.id"""
        self.id = str(uuid.uuid4())

    def __str__(self):
        """Return class name, id and __dict__ formatted as a string"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__)
        )


if __name__ == "__main__":
    base_model = BaseModel()

if __name__ == "__main__" and hasattr(__builtins__, '__interactivehook__'):
    print("Running in interactive mode.")

    base_model = BaseModel()

    print("String representation:", base_model)

    base_model.save()
    print("Modified_at timestamp after save:", base_model.updated_at)

    model_dict = base_model.to_dict()
    print("Instance converted to dictionary:", model_dict)

    rebuilt_model = BaseModel()
    rebuilt_model.rebuild(model_dict)
    print("Rebuilt instance from dictionary:", rebuilt_model)
