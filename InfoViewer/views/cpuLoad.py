from .abstractView import AbstractView


class CPULoad(AbstractView):

    def onCreate(self, screen):
        pass

    def __init__(self):
        print("Hallo Welt")

    def refresh(self) -> None:
        pass

    def getName(self=None) -> str:
        return "CPULoad"

    def getDocs(self) -> str:
        return "DocString"

    def setConfig(self, config) -> None:
        pass
