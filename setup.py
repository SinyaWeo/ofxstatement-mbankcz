#!/usr/bin/python3
"""
Setup
"""
from setuptools import find_packages
from distutils.core import setup

version = "1.0.0"

with open("README.md") as f:
    long_description = f.read()

setup(
    name="ofxstatement-mbankcz",
    version=version,
    author="Milan Horák",
    author_email="milan@nosoftware.cz",
    url="https://github.com/SinyaWeo/ofxstatement-mbankcz",
    description=("ofxstatement plugin for mBank (CZ)"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    keywords=["ofx", "banking", "statement"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["ofxstatement", "ofxstatement.plugins"],
    entry_points={
        "ofxstatement": [
            "mbankcz = ofxstatement.plugins.mbankcz:MBankCZPlugin"
        ]
    },
    install_requires=["ofxstatement"],
    include_package_data=True,
    zip_safe=True,
)
