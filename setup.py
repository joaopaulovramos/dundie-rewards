# setuptools

# pyproject

<<<<<<< HEAD
=======
from importlib.metadata import entry_points
>>>>>>> 07a2836 (turned to installable binary)
from setuptools import setup, find_packages


setup(
  name="dundie",
  version="0.1.0",
  description="Reward Point system for Dunder Mifflin",
  author="Joao Paulo",
  packages=find_packages(),
<<<<<<< HEAD
=======
  entry_points={
    "console_scripts": [
      "dundie = dundie.__main__:main"
    ]
  }
>>>>>>> 07a2836 (turned to installable binary)
)
