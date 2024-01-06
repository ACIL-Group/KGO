# KGO

**K**owledge **G**raphs and **O**ntologies: code and data for the paper *Transformation of Biomedical Data into Knowledge Graphs and Ontologies*.

## Table of Contents

- [KGO](#kgo)
  - [Table of Contents](#table-of-contents)
  - [Summary](#summary)
  - [Usage](#usage)
    - [Setup](#setup)
    - [Execution](#execution)

## Summary

This project implements a method of transforming biomedical gene-phenotype data into knowledge graphs and corresponding ontologies.
This is demonstrated with a single `data -> script -> output` workflow.

The project is laid out as follows:

- `main_dystonia_graph_and_ontology_method.py`: the main Python file running the experiment.
- `data/`: the data files necessary to run the experiment.
- `example_output/`: example files demonstrating the output of the experiment.

## Usage

This project contains a main Python script that processes biomedical gene-phenotype dystonia data and outputs graph files of various kinds.
This follows the pattern of creating a virtual Python environment, installing dependencies, running the main file, and exploring the output files.
Brief installation instructions can be found in [Setup](#setup), and use of the scripts can be found in [Execution](#execution).

### Setup

Create and activate a virtual Python environment with your favorite tool (e.g., `conda`, `mamba`, or `venv`).

With `conda`:

```shell
conda create -n kgo python=3.11
conda activate kgo
```

Next, install dependencies while inside this virtual environment via the `requirements.txt` file at the top of this repo:

```shell
pip install -r requirements.txt
```

### Execution

The entire experiment lives at the top of the project in a file called `main_dystonia_graph_and_ontology_method.py`.
To execute it, simply run the file through the Python interpreter while in your virtual environment as follows:

```shell
python main_dystonia_graph_and_ontology_method.py
```

Three files are generated, examples of which can be seen in the `example_output/` directory.
