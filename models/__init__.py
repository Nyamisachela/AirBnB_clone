from .base_model import BaseModel
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

my_models = {"base": BaseModel}

def get_model(name):
    """Return an instance of the named model"""
    if name in my_models:
        return my_models[name]()
    else:
        raise ValueError("Module {} not found!".format(name))
