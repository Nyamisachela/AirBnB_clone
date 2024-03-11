#!/usr/bin/python3
import datetime
import uuid


class BaseModel:
    """BaseModel Class"""

    def __init__(self):
        """
        Initialize Object
        argument: self
        returns: Null
        """
        self.my_number = 0
        self.name = ""
        self.id = ""
        self.set_uuid()
        self.timestamp()

    def timestamp(self):
        """
        Get timestamp, format it to ISO
        Initialize created_at and modified_at with timestamp
        """
        now = datetime.datetime.now().isoformat()
        self.created_at = now
        self.modified_at = now

    def save(self):
        """Update the property modified_at with current timestamp"""
        self.modified_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """Get object and class attributes, write them to self.my_dict"""
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__.copy()

    def set_uuid(self):
        """
        Set a uuid
        """
        self.id = str(uuid.uuid4())

    def rebuild(self, params):
        """"
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        neo = {
            datetime.datetime.strptime(value, date_format)
            if key == "created_at" else value
            if key == "modified_at" else value
            for key, value in params.items()
            if key != "__class__"
        }
        """
        pass

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, str(self.__dict__))



if __name__ == "__main__":
    base_model = BaseModel()
if __name__ == "__main__" and hasattr(__builtins__, '__interactivehook__'):
    # Include any interactive code or tests here
    print("Running in interactive mode.")

    # Create an instance of BaseModel
    base_model = BaseModel()

    # Print the string representation of the instance
    print("String representation:", base_model)

    # Save the instance and print the modified_at timestamp
    base_model.save()
    print("Modified_at timestamp after save:", base_model.modified_at)

    # Convert the instance to a dictionary and print it
    model_dict = base_model.to_dict()
    print("Instance converted to dictionary:", model_dict)

    # Rebuild an instance from the dictionary and print the result
    rebuilt_model = BaseModel()
    rebuilt_model.rebuild(model_dict)
    print("Rebuilt instance from dictionary:", rebuilt_model)

    # Include any other tests or checks specific to your BaseModel class

