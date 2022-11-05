# `vanipy`

A tool for very superficial Algorand addresses.

:bangbang: THIS TOOL IS MEANT FOR DEVELOPMENT PURPOSES ONLY, DO NOT USE ADDRESSES GENERATED WITH THIS TOOL ON ALGORAND'S MAIN NET :bangbang:

[![asciicast](https://asciinema.org/a/ij9MKpSwFVU5SkQwyMXOEPPZv.svg)](https://asciinema.org/a/ij9MKpSwFVU5SkQwyMXOEPPZv)

(Sped up video, the brute force approach used in this tool takes **exponential time** in the number of bits of information constrained by the query pattern.) 

## Install and configure [Poetry](https://python-poetry.org/)

You can find all the details on how to install Poetry [here](https://python-poetry.org/docs/#installation)

When you are done with the installation, we advise you to configure poetry to save its virtual environments in the
present folder.

```bash
poetry config virtualenvs.in-project true
```

## Install dependencies

```bash
poetry install
```

## Run `vanipy`

Run the following command to get all the information about `vanipy` usage:

```bash
poetry run vanipy --help
```
