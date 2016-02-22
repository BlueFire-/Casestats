import importlib
import os
import inspect
from views.abstractView import AbstractView

viewPath = "views/"
classList = []


def getClass(module) -> object:
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
            clazz = getClass(module)
            if clazz is not None:
                classList.append(clazz)


def validateConfig(config) -> bool:
    assert isinstance(config, list)

    if len(classList) == 0:
        loadViews()
    for configElement in config:
        name = configElement[0]
        attributeDict = configElement[1]
        assert isinstance(attributeDict, dict)

        # Check if class exists
        clazz = None
        for curClazz in classList:
            assert issubclass(curClazz, AbstractView)
            if curClazz.getName() == name:
                clazz = curClazz
                break
        if clazz is None:
            raise ValueError("The Widget '" + name + "' is unknown.")

        # Check if all used attributes are existent
        for curKey in attributeDict.keys():
            keyExists = False
            for curParam in clazz.getDocs().keys():
                if curKey == curParam:
                    keyExists = True
                    break
            if not keyExists:
                raise ValueError("The Attribute '" + curKey + "' is unknown in Widget '" + name + "'")


def getView(name) -> AbstractView:
    clazz = None
    for curClazz in classList:
        if curClazz.getName() == name:
            return curClazz()

    return None
