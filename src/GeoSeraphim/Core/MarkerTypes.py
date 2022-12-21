from abc import ABC, abstractclassmethod, ABCMeta

import json
import pathlib as pl

class GeoSeraphimBaseClass(ABC):
    __metaclass__ = ABCMeta
    def __init__(self, name = None, **kwargs):
        self.__name = name if name is not None else "{}@{}".format(self.__class__.__name__, hex(id(self)))
        self.__oname = "{}: {}".format(self.__class__.__qualname__, self.__name)
        self.__state = "New spawn"
        
        for key, value in kwargs:
            setattr(self, key,  value)
    
    @property
    @abstractclassmethod
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, new_state: str):
        self.__state = new_state
        
    @state.getter
    def state(self):
        return self.__state
    
    @property
    @abstractclassmethod
    def name(self):
        return self.__name
    
    @name.getter
    def name(self):
        return self.__name
    
    @property
    @abstractclassmethod
    def object_name(self):
        return self.__oname
    
    @name.getter
    def object_name(self):
        return self.__oname 
    
    def __repr__(self):
        return "[{}]: {}".format(self.object_name, self.state)
    
class ResultType(GeoSeraphimBaseClass):
    pass
    
class ReaderType(GeoSeraphimBaseClass):
    
    def __call__(self, **kwargs) -> ResultType | None:
        try:
            return self.read(**kwargs)
        except Exception as exc:
            self.state = "Failed to read at path: {}".format(exc)
    
    @abstractclassmethod
    def read(self, path: str | pl.Path, encoding: str | pl.Path, **kwargs):
        pass

class ResultType(GeoSeraphimBaseClass):
    
    def build_from(self, buffer: str | bytes | bytearray, **kwargs):
        try:
            self = json.loads(buffer, object_hook=self.interpret, **kwargs)
            return self
        except Exception as exc:
            self.state = "Failed to build from buffer: {}".format(exc)
            return self
    
    @abstractclassmethod        
    def interpret(self, dct):
        pass
        
    @property
    @abstractclassmethod
    def recipe(self):
        return json.dumps(self)
    
    @recipe.setter
    def recipe(self, new_recipe: str | bytes | bytearray):
        self.build_from(new_recipe)
        
    @recipe.getter
    def recipe(self):
        return json.dumps(self)
