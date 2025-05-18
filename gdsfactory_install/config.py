"""Store configuration.

This module provides path configuration for the gdsfactory_install package.
It defines common paths used throughout the application.
"""

__all__ = ["PATH"]

import pathlib

home = pathlib.Path.home()
cwd = pathlib.Path.cwd()

module_path = pathlib.Path(__file__).parent.absolute()
repo_path = module_path.parent


class Path:
    """Path configuration for gdsfactory_install.
    
    Provides access to commonly used paths in the application.
    """
    
    module = module_path  # Path to the module directory
    repo = repo_path  # Path to the repository root
    cells = module / "cells"  # Path to the cells directory


PATH = Path()

