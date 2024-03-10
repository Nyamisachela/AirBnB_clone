
from.base_model import BaseModel

my_models = {"base": BaseModel}


def get_model(name):
    """Return instance of named model"""
    if name in my_models:
        return my_models[name]()
    else:
        raise ValueError("Module {} not found!".format(name))
