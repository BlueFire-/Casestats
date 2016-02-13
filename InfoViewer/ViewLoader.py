import importlib
import os
import inspect
from views.abstractView import AbstractView

viewPath = "views/"
classList = []


def getClassName(module):
    tmpClassList = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, AbstractView) and name != "AbstractView":
            tmpClassList.append(obj)
    if len(tmpClassList) == 1:
        return tmpClassList[0]
    elif len(tmpClassList) != 0:
        raise AttributeError("The Module has more than one class defined")



def loadViews():
    if not os.path.exists(viewPath):
        raise FileNotFoundError("Directory does not exist: %s" % viewPath)
    for f in os.listdir(viewPath):
        # Ignore everything that isn't a .py file
        if len(f) > 3 and f[-3:] == ".py":
            moduleName = f[:-3]
            if moduleName == "abstractView":
                continue
            module = importlib.import_module(viewPath[:-1] + "." + moduleName, viewPath[:-1])
            clazz = getClassName(module)
            if clazz is not None:
                classList.append(clazz)
