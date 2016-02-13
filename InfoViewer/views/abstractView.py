import abc


class AbstractView(object):

    @abc.abstractmethod
    def getDocs(self) -> str:
        """
        :rtype: str
        :return: The documentation of possible config parameter
        """
        return

    @abc.abstractmethod
    def setConfig(self, config) -> None:
        """
        The class should safe the config in a safe way and start to create the view
        :param config: All config params read by the program
        :return: None
        """
        return

    @abc.abstractmethod
    def refresh(self) -> None:
        """
        Should fill the view with new data
        :return: None
        """
        return

    @abc.abstractmethod
    def onCreate(self, screen):
        """
        This method should add the configured element to the screen
        :param screen:The current screen object
        :return:
        """
        return

    @abc.abstractstaticmethod
    def getName(self=None) -> str:
        """
        :rtype: str
        :return: The name of the view
        """
        return

