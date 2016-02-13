# This ugly workaround is just so the IDE is satisfied and autocompletion works
import importlib
if __name__ == "__main__":
    from views.abstractView import AbstractView
    import ViewLoader
else:
    from .views.abstractView import AbstractView


ViewLoader.loadViews()

for view in ViewLoader.classList:
    curView = view()
    assert isinstance(curView, AbstractView)
    print(view.getName())


