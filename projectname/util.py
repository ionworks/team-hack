import projectname
import pathlib
import os
from dotenv import load_dotenv

load_dotenv()


def environ():
    return os.environ


def root_dir():
    """return the root directory of the install directory"""
    return str(pathlib.Path(projectname.__path__[0]).parent)
