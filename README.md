Analysis EEL data
==============================
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lhoupert/analysis_eel_data/master?filepath=notebooks)
[![Build Status](https://travis-ci.com/lhoupert/analysis_eel_data.svg?branch=master)](https://travis-ci.com/lhoupert/analysis_eel_data)
[![codecov](https://codecov.io/gh/lhoupert/analysis_eel_data/branch/master/graph/badge.svg)](https://codecov.io/gh/lhoupert/analysis_eel_data)
[![License:MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flt-square)](https://opensource.org/licenses/MIT)

A repository associated with the [Extended Ellett Line (EEL)](https://projects.noc.ac.uk/ExtendedEllettLine/)  oceanographic dataset  It mostly contains [python scripts](https://mybinder.org/v2/gh/lhoupert/analysis_eel_data/master?filepath=notebooks)  used to analyse and visualise these oceanographic data.


This repository is a work in progress and should be updated regularly. This repo can also be run on [binder](https://mybinder.org/v2/gh/lhoupert/analysis_eel_data/master/notebooks).

### Requirements to run the notebooks locally
 - [Conda package manager](https://conda.io/en/latest/)



### Quickstart


- Clone or download the repository

``` 
git clone https://github.com/lhoupert/analysis_eel_data.git
```

- Create and activate the Conda environment *analysis\_eel\_data* containing the relevant libraries (the creation of the environment can take a few minutes)

```
cd analysis_eel_data
conda env create -f environment.yml
conda activate analysis_eel_data
```

- Run the Jupyter notebooks available

```
cd notebooks
jupyter-lab
```

<br/>



## List of current notebooks available (work in progress)


### 1. Maps

#### 1.1 Bathymetry map of the North Atlantic Ocean using *cartopy* and *matplotlib* axes functions
The notebook [01-lh-Plot-map-EEL-data.ipynb](https://github.com/lhoupert/analysis_eel_data/blob/master/notebooks/01_Plot_map_EEL_data.ipynb) plot the bathymetry of the North Atlantic Ocean with two regional zoom and with the label of the hydrographic stations

![Bathymetry of the eastern North Atlantic with Extended Ellett Line section](references/readme_figures/fig11.png)

<br/>

#### 1.2 Bathymetry map with mean current vector and mean current ellipse overlaid using *cartopy* and *xarray*

*work in progress*

<br/>

### 2. Data exploration and visualisation

#### 2.1 Exploration of EEL dataset and contour plots of mean quantities
The notebook [02-lh-Explore-EEL-meanfield.ipynb.ipynb](https://github.com/lhoupert/analysis_eel_data/blob/master/notebooks/02_Explore_EEL_meanfield.ipynb) is used to explore the EEL dataset. It also generates summary figures of the mean and standard deviation of the velocity, teperature, salinity and density along the EEL section (see example below). 

*Note: this notebook has been written at early stage in my transition from Matlab to Python and is mostly based on Python Dataframe. The use of [xarray](http://xarray.pydata.org/en/stable/) would have certainly shortened and optimised this code.*

![Exemple of contour plot accross the EEL section](references/readme_figures/fig22.png)

<br/>

#### ...

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>
