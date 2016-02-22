
# This ugly workaround is just so the IDE is satisfied and autocompletion works
if __name__ == "__main__":
    from infoViewerForm import InfoViewerApp
    import ViewLoader
    import ConfigParser
else:
    from .infoViewerForm import InfoViewerApp

config = ConfigParser.getViewConfig()

ViewLoader.loadViews()

ViewLoader.validateConfig(config)

InfoApp = InfoViewerApp(config)
InfoApp.run()

