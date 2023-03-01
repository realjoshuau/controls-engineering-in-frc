#!/usr/bin/env python3

"""Module setup."""

from datetime import date
from os.path import dirname
from os.path import exists
from os.path import join
import subprocess

from setuptools import find_packages, setup

setup_dir = dirname(__file__)
git_dir = join(setup_dir, ".git")
base_package = "bookutil"
version_file = join(setup_dir, base_package, "version.py")

# Automatically generate a version.py based on the git version
if exists(git_dir):
    proc = subprocess.run(
        [
            "git",
            "rev-list",
            "--count",
            # Includes previous year's commits in case one was merged after the
            # year incremented. Otherwise, the version wouldn't increment.
            f'--after="main@{{{date.today().year - 1}-01-01}}"',
            "main",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    # If there is no main branch, the commit count defaults to 0
    if proc.returncode:
        commit_count = "0"
    else:
        commit_count = proc.stdout.decode("utf-8").rstrip()

    # Version number: <year>.<# commits on main>
    version = f"{date.today().year}.{commit_count}"

    # Create the version.py file
    with open(version_file, "w", encoding="utf-8") as fp:
        fp.write(f'# Autogenerated by setup.py\n__version__ = "{version}"')

if exists(version_file):
    with open(version_file, "r", encoding="utf-8") as fp:
        # pragma pylint: disable=exec-used
        exec(fp.read(), globals())
else:
    __version__ = f"{date.today().year}.0"

setup(
    name="bookutil",
    version=__version__,
    description="Utility functions for controls book",
    author="Tyler Veness",
    maintainer="Tyler Veness",
    maintainer_email="calcmogul@gmail.com",
    url="https://github.com/calcmogul/controls-engineering-in-frc",
    keywords="robotics control",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=["frccontrol"],
    license="BSD License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
    ],
)
