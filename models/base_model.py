import datetime
import uuid


class BaseModel:
    """BaseModel Class"""

    name = ""
    my_number = ""
    my_dict = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key not in ('__class__', '__weakref__'):
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.set_uuid()
            self.set_created_at()

    def set_created_at(self):
        """
        Set Created At from datetime.now() and format to iso
        """
        now = datetime.datetime.now().isoformat()
        self.created_at = now
        self.updated_at = now

    def save(self):
        self.__dict__["modified_at"] = datetime.datetime.now().isoformat()

    def to_dict(self):
        self.my_dict = self.__dict__.copy()
        self.my_dict.update(self.__class__.__dict__)
        return self.my_dict

    def set_uuid(self):
        """
        Set a uuid
        """
        self.id = str(uuid.uuid4())
        print(self.id)


if __name__ == "__main__":
    base_model = BaseModel()
    base_model.name = "tester"
    base_model.my_number = 89
    base_model.to_dict()
    print(base_model.my_dict)
