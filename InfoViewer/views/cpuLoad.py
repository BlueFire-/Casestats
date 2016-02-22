from .abstractView import AbstractView
from .widgets.customSlider import CustomSlider


class CPULoad(AbstractView):
    def onCreate(self, screen):
        screen.add(CustomSlider, **self.config)

    def __init__(self):
        self.config = {}

    def refresh(self) -> None:
        pass

    def getName(self=None) -> str:
        return "CPULoad"

    def getDocs(self=None) -> dict:
        return {"name": "The title of the element",
                "relx": "The x position of the element (optional)",
                "rely": "The y position of the element (optional)",
                "num": "Which CPU should be displayed. If -1, the core with most load is shown, " +
                        "if -2 the core with 2nd most load, and so on",
                }

    def setConfig(self, config) -> None:
        self.config = config
        assert isinstance(self.config, dict)
        for key, value in self.config.items():
            if key.startswith("rel"):
                self.config[key] = int(value)
