# KGO

**K**owledge **G**raphs and **O**ntologies: code and data for the paper *Transformation of Biomedical Data into Knowledge Graphs and Ontologies*.

| **Zenodo DOI** | **Test Status** | **Coverage** |
|:--------------:|:---------------:|:------------:|
| [![DOI][zenodo-img]][zenodo-url] | [![Build Status][ci-img]][ci-url] | [![Codecov][codecov-img]][codecov-url] |

[zenodo-img]: https://zenodo.org/badge/DOI/10.5281/zenodo.10463050.svg
[zenodo-url]: https://doi.org/10.5281/zenodo.10463050

[ci-img]: https://github.com/ACIL-Group/KGO/actions/workflows/Test.yml/badge.svg
[ci-url]: https://github.com/ACIL-Group/KGO/actions/workflows/Test.yml

[codecov-img]: https://codecov.io/gh/ACIL-Group/KGO/branch/main/graph/badge.svg
[codecov-url]: https://codecov.io/gh/ACIL-Group/KGO

## Table of Contents

- [KGO](#kgo)
  - [Table of Contents](#table-of-contents)
  - [Summary](#summary)
  - [Usage](#usage)
    - [Setup](#setup)
    - [Execution](#execution)
  - [Citation](#citation)

## Summary

This project implements a method of transforming biomedical gene-phenotype data into knowledge graphs and corresponding ontologies.
This is demonstrated with a single `data -> script -> output` workflow.

The project is laid out as follows:

- `src/main_dystonia_graph_and_ontology_method.py`: the main Python file running the experiment.
- `data/`: the data files necessary to run the experiment.
- `out/`: the destination for the generated files from the experiment.
- `example_output/`: example files demonstrating the output of the experiment.

## Usage

This project contains a main Python script that processes biomedical gene-phenotype dystonia data and outputs graph files of various kinds.
This follows the pattern of creating a virtual Python environment, installing dependencies, running the main file, and exploring the output files.
Brief installation instructions can be found in [Setup](#setup), and use of the scripts can be found in [Execution](#execution).

### Setup

Create and activate a virtual Python environment with your favorite tool (e.g., `conda`, `mamba`, or `venv`).

For example, with `conda`:

```shell
conda create -n kgo python=3.11
conda activate kgo
```

Next, install dependencies while inside this virtual environment via the `requirements.txt` file at the top of this repo:

```shell
pip install -r requirements.txt
```

### Execution

The entire experiment lives in a file called `src/main_dystonia_graph_and_ontology_method.py`.
To execute it, simply run the file through the Python interpreter while in your virtual environment as follows:

```shell
python src/main_dystonia_graph_and_ontology_method.py
```

Three files are generated and saved to the `out/` directory.
Examples of the files that should be generated can be seen in the `example_output/` directory.

## Citation

This project has a [citation file](CITATION.cff) file that generates citation information for the repository, which can be accessed at the "Cite this repository button" under the "About" section of the GitHub page.

The latest archival of the project is also at [https://doi.org/10.5281/zenodo.10463050](https://doi.org/10.5281/zenodo.10463050), which has its own tools for generating citations according to your favorite citation style.
