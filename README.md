Analysis EEL data
==============================
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lhoupert/analysis_eel_data/master)
[![Build Status](https://travis-ci.com/lhoupert/analysis_eel_data.svg?branch=master)](https://travis-ci.com/lhoupert/analysis_eel_data)
[![codecov](https://codecov.io/gh/lhoupert/analysis_eel_data/branch/master/graph/badge.svg)](https://codecov.io/gh/lhoupert/analysis_eel_data)
[![License:MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flt-square)](https://opensource.org/licenses/MIT)

A repository associated with the [Extended Ellet Line](https://projects.noc.ac.uk/ExtendedEllettLine/)  oceanographic dataset  It mostly contains [python scripts](https://github.com/lhoupert/analysis_eel_data/tree/master/notebooks)  used to analyse and visualise these oceanographic data.


This is a work in progress! This repository is going to be updated regularly.

### Requirements to run the notebooks locally
 - [Conda package manager](https://conda.io/en/latest/)



### Quickstart


- Clone or download the repository

``` 
git clone https://github.com/lhoupert/analysis_eel_data.git
```

- Create and activate the Conda environment *analysis\_eel\_data* containing the relevant libraries:

```
cd xarraytest_lh
conda env create -f environment.yml
conda activate analysis_eel_data
```

- Run the Jupyter notebooks available

```
cd notebooks
jupyter-lab
```


--

### List of current notebooks available (work in progress)


#### 1. Bathymetry map of the North Atlantic Ocean using *cartopy* and *matplotlib* axes functions: 
The notebook [others/00\_Plot\_map\_forRTpaper.ipynb](https://github.com/lhoupert/analysis_eel_data/blob/master/notebooks/other/00_Plot_map_forRTpaper.ipynb) was used to generate the Figure1 of [Houpert et al., [in review]](https://www.essoar.org/doi/10.1002/essoar.10503226.1) *-Bathymetry of the North Atlantic Ocean and of the central Rockall Trough with the location of oceanographic data-*

![Bathymetry of the North Atlantic as in Houpert et al., 2020](https://uc87135040fc932c86bfe54876c0.dl.dropboxusercontent.com/cd/0/inline/A6yFtUnJ-zFXCo4aiBL3kTtds-p9i7F0hthlm5ub8w5yY9q2voduSihjpAhvQL7LAXXAATQRSwSUvuURBOOK484IcsxRw9jeKA9wHGWTsJjRCayd8bdnoUzqALyPmjcZW6w/file#)

#### 2. ...



--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>
