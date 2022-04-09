from abc import abstractmethod
import os
from app.database import DatabaseType, Database


class BaseHandler:
    """
    The base class for Handlers.

    Attributes
    ----------
    runtime_mode : str
        The environment that the bot is running in (i.e. DEV or PRODUCTION).

    db: SQLiteDatabase
        The entry point to interact with SQLite database.

    Methods
    -------
    create_match_paterns(message: str)
        Initialize regex patterns.

    handle(message: str)
        Handle the message and return the proper response.

    parse(message: str):
        Parse the message to extract keywords.

    dispose():
        Clean up resources used by this minibot.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the ProductHandler object.
        """
        # Set the operation mode (i.e. DEV or PRODUCTION)
        self.runtime_mode = os.getenv("PYTHON_ENV", "DEV")

        # Initialize a mock database if development environment
        if self.runtime_mode == "DEV":
            self.db = Database.instance()
            self.db.connect()  # Start a connection
            self.db.init_database()  # Initialize the database
        else:
            self.db = None

    def dispose(self):
        """
        Call this methods to release any resources with this minibot (i.e. database connection).
        """
        if self.db:
            self.db.close()
