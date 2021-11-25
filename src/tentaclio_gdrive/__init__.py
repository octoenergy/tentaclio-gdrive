"""This package implements the tentaclio gdrive client """
from tentaclio import *  # noqa

from .clients.gdrive_client import ClientClassName


# Add DB registry
DB_REGISTRY.register("gdrive", ClientClassName)  # type: ignore
