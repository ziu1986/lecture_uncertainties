# Lecture: Uncertainties in environmental modeling
This repository includes scripts developed for the lecture "Uncertainties in environmental modeling" at LMU (WS2122).
The scripts are inspired by results shown in the lecture developed by Ana Bastos (WS1920).

## Installation
-------------
Download and install anaconda and run:

`$ conda env create -f environment.yml`

Activate environment

`$ conda activate lecture`

Use ipython once the environment is installed.

## Release note
-------------
### v.1.0

All functions were optimized for python 3.8.8.

## Content
-------------
The Parameters of the scripts can be modified by editing the config.yml files.

- white_noise.py

## Running
-----------
You can run directly from the command line

```bash
~/lecture_uncertainties/white_noise$ python white_noise.py
```

or use the `ipython` interpreter

```bash
~/lecture_uncertainties/white_noise$ ipython

In [1]: %run 'white_noise.py'
```