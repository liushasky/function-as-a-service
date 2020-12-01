
from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

setup(
    name="faas-nltk",
    version="1.0.0",
    description="An FaaS takes URL as input and output the histogram of doc length.",
    url="https://github.com/liushaskymm",
    author="Sha Liu",
    author_email="liu226@indiana.edu",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.5",
    install_requires=[
        "flask>=1.0,<2.0",
        "cloudevents>=1.2.0,<2.0.0",
        "click>=7.0,<8.0",
        "gunicorn>=19.2.0,<21.0; platform_system!='Windows'",
        "watchdog>=0.10.0",
    ],
    entry_points={
        "console_scripts": [
            "faas-start=faas._cli:_cli",
        ]
    },
)
