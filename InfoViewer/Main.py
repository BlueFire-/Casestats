# This ugly workaround is just so the IDE is satisfied and autocompletion works

if __name__ == "__main__":
    from views.abstractView import AbstractView
    import ViewLoader
    import ConfigParser
else:
    from .views.abstractView import AbstractView

config = ConfigParser.getViewConfig()

ViewLoader.loadViews()

ViewLoader.validateConfig(config)

#for view in ViewLoader.classList:
#    curView = view()
#    assert isinstance(curView, AbstractView)
#    print(view.getName())


