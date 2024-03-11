import json

class FileStorage:
    """file storage class"""
    
    def __init__(self):
        """Sets the default path for the JSON file (__file_path) and initializes an empty dictionary for storing objects (__objects)."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, object in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**obj_data)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass  # Do nothing if the file doesn't exist


