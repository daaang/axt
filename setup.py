#!/usr/bin/env python3
# Axt: automation tools for taxes in the United States
# Copyright 2017 Matt LaChance
#
# This file is part of Axt.
#
# Axt is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Axt is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with Axt. If not, see <http://www.gnu.org/licenses/>.
from setuptools import setup
from os import walk
from os.path import abspath, dirname, join
from Cython.Build import cythonize

class DevelopmentStatus:

    planning = "1 - Planning"
    pre_alpha = "2 - Pre-Alpha"
    alpha = "3 - Alpha"
    beta = "4 - Beta"
    stable = "5 - Production/Stable"
    mature = "6 - Mature"
    inactive = "7 - Inactive"

CURRENT_STATUS = DevelopmentStatus.planning

def get_path_to_base_directory():
    return abspath(dirname(__file__))

def get_file_contents(*args):
    with open(join(*args)) as the_file:
        result = the_file.read()

    return result

def get_ext_modules(base_dir):
    results = [ ]

    for root, dirs, filenames in walk(base_dir):
        for filename in filenames:
            if filename.endswith(".pyx"):
                results.append(join(root, filename))

    if results:
        return cythonize(results)

base_dir = get_path_to_base_directory()
long_desc = get_file_contents(base_dir, "README.rst")

setup(
    name="Axt",
    version="1.0.0.dev0",
    description="Automation tools for taxes in the United States",
    long_description=long_desc,
    license="GPLv3",
    author="Matt LaChance",
    author_email="mattlach@umich.edu",

    classifiers=[
        " :: ".join(("Development Status", CURRENT_STATUS)),
        " :: ".join(("License", "OSI Approved",
                     "GNU General Public License v3 (GPLv3)")),
        " :: ".join(("Natural Language", "English")),
        " :: ".join(("Programming Language", "C")),
        " :: ".join(("Programming Language", "Cython")),
        " :: ".join(("Programming Language", "Python", "3", "Only")),
        " :: ".join(("Topic", "Office/Business",
                     "Financial", "Accounting")),
    ],

    packages=["axt"],
    package_dir={"": "lib"},
    ext_modules=get_ext_modules("lib/axt"),
)
