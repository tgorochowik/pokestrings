#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup

setup(
    name="pokestrings",
    version="0.1",
    author="Tomasz Gorochowik",
    description="Extract stings from Pokemon ROMs/",
    author_email="t@gorochowik.com",
    url="https://github.com/tgorochowik/pokestrings",
    packages=["pokestrings"],
    entry_points={
        "console_scripts": [
            "pokestrings = pokestrings:main_pokestrings",
            "pokecodec = pokestrings:main_pokecodec",
        ]
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
)
