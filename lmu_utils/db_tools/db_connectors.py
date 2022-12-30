"""Class to use for DB Connection."""

from enum import Enum
import logging

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


class DBConnection():
    """Create the necessary connection."""

    def __enter__(self):
        """Open a database connection."""
        try:
            self.conn = self.engine.connect()
        except SQLAlchemyError as error:
            logging.error(f'Connection refused {error}')
            raise error
        return self

    def __exit__(self):
        """Close a database connection."""
        try:
            self.conn.close()
        except Exception:
            pass

    def get_connection(self):
        """Return a database connection."""
        try:
            self.conn = self.engine.connect()
        except SQLAlchemyError as error:
            logging.error(f'Connection refused {error}')
            raise error
        return self.conn


class ConnectionType(Enum):
    """Database type to create the connection with."""

    MYSQL = "mysql+pymysql", "?charset=utf8", "3306"
    POSTGRES = "postgresql", "", "5439"