"""
Setup script for the Wildfire Detection project.

This makes the 'src' directory package and installable so modules can be imported
cleanly across the project without messing with paths.
"""

from setuptools import setup, find_packages
from pathlib import Path

from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove the newline character (\n) from each line
        requirements = [req.replace("\n", "") for req in requirements]
       

        # Remove "-e ." if it exists in the requirements.txt
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# Read README file for long description
BASE_DIR = Path(__file__).parent
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")

setup(
    name="wildfire-detection",
    version="1.0.0",
    description="Wildfire detection using satellite imagery and deep learning",
    long_description=README,
    long_description_content_type="text/markdown",

    author="Shanu Kumar",
    author_email="Shanu202000@gmail.com",
    url="https://github.com/shanu202000/Wildfire-Detection-Application-using-satellite-image",

    # Project structure
    packages=find_packages(where="src"),
    package_dir={"": "src"},

    # Python version requirement
    python_requires=">=3.9",

    # Dependencies
    install_requires=get_requirements("requirements.txt"),

    # Optional metadata (helps in packaging and discoverability)
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],

    keywords=[
        "wildfire detection",
        "satellite imagery",
        "deep learning",
        "computer vision",
        "AI",
    ],

    include_package_data=True,
)