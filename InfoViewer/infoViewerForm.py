import sys
import npyscreen
import time
import ViewLoader
from views.abstractView import AbstractView



# Only for initializing
class InfoViewerApp(npyscreen.NPSAppManaged):
    def __init__(self, config):
        self.config = config
        super(InfoViewerApp, self).__init__()

    def onStart(self):
        self.registerForm("MAIN", MainForm(self.config))


class MainForm(npyscreen.FormBaseNew):

    def __init__(self, config, *args, **keywords):
        # first initialize the attributes, then call super class
        self.config = config
        self.views = []
        super(MainForm, self).__init__(*args, **keywords)
        self.add_handlers({"^C": sys.exit})

    def activate(self):
        self.parentApp.setNextForm(None)
        self.edit_loop()

    def create(self):

        # Create a empty grid for the FOrm to focus so the cursor is invisible
        rely = self.nextrely
        self.add(npyscreen.SimpleGrid, rely=1, max_height=1)
        self.nextrely = rely

        assert isinstance(self.config, list)
        for curConfig in self.config:
            assert isinstance(curConfig, list)
            curView = ViewLoader.getView(curConfig[0])
            assert isinstance(curView, AbstractView)
            curView.setConfig(curConfig[1])
            curView.onCreate(self)
            self.views.append(curView)

        # refresh the screen automatically
        self.keypress_timeout = 1

    def while_waiting(self):
        for curView in self.views:
            curView.refresh()

        self.display()

    def handle_exit(self):
        self.parentApp.switchFormPrevious()