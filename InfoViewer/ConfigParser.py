import xml.etree.ElementTree as ElementTree
from xml.etree.ElementTree import Element
import os.path

viewConfig = "ViewConfig.xml"

def getViewConfig() -> list:
    if not os.path.exists(viewConfig):
        raise FileNotFoundError(viewConfig + " not found")
    resultList = []
    parentNode = ElementTree.parse(viewConfig).getroot()
    for node in parentNode.findall('widget'):
        assert isinstance(node, Element)
        curList = [node.find("name").text, __ElementToDictionary(node.find("attributes"))]
        resultList.append(curList)
    return resultList


def __ElementToDictionary(element) -> dict:
    if element is None:
        raise ValueError("The attribute Key is missing.")
    assert isinstance(element, Element)
    resultDict = {}
    for node in list(element):
        assert isinstance(node, Element)
        resultDict[node.tag] = node.text
    return resultDict