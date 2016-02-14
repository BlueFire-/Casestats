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

    def getDocs(self=None) -> dict:
        return {"relx": "The x position of the element (optional)",
                "rely": "The y position of the element (optional)",
                "num": "Which CPU should be displayed. If -1, the core with most load is shown, " +
                        "if -2 the core with 2nd most load, and so on",
                }

    def setConfig(self, config) -> None:
        pass
