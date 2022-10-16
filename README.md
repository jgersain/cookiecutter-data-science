# Cookiecutter Conda Data Science

A simple template to start a data science project and create something awesome!

## Requirements

- Conda
- Cookiecutter Python package
  - pip install cookiecutter
  - conda install -c conda-forge

## Create a new project

```bash
cookiecutter https://github.com/jvelezmagic/cookiecutter-conda-data-science
```

## Install environment

```
conda env create --file environment.yml
conda activate <name>
```

Reference: [https://github.com/jvelezmagic/cookiecutter-conda-data-science](https://github.com/jvelezmagic/cookiecutter-conda-data-science)
