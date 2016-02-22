import xml.etree.ElementTree as ElementTree
from xml.etree.ElementTree import Element
import os.path

viewConfig = "ViewConfig.xml"
prefix = "{http://www.w3schools.com}"

def getViewConfig() -> list:
    if not os.path.exists(viewConfig):
        raise FileNotFoundError(viewConfig + " not found")
    resultList = []
    parentNode = ElementTree.parse(viewConfig).getroot()
    assert isinstance(parentNode, Element)
    ab = list(parentNode)
    for node in list(parentNode):
        assert isinstance(node, Element)
        if node.tag == prefix + 'widget':
            curList = [node.find(prefix + "name").text, __ElementToDictionary(node.find(prefix + "attributes"))]
            resultList.append(curList)
    return resultList


def __ElementToDictionary(element) -> dict:
    if element is None:
        raise ValueError("The attribute Key is missing.")
    assert isinstance(element, Element)
    resultDict = {}
    for node in list(element):
        assert isinstance(node, Element)
        resultDict[node.tag[len(prefix):]] = node.text
    return resultDict