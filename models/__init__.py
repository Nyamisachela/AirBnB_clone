from .base_model import BaseModel

my_models = {"base": BaseModel}


def get_model(name):
	"""return instance of the named model"""
	if name in my_models:
		return my_models[name]()
	else:
		raise ValueError("module {} not found!".format(name))
