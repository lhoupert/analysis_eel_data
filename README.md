Analysis EEL data
==============================
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lhoupert/analysis_eel_data/master)
[![Build Status](https://travis-ci.com/lhoupert/analysis_eel_data.svg?branch=master)](https://travis-ci.com/lhoupert/analysis_eel_data)
[![codecov](https://codecov.io/gh/lhoupert/analysis_eel_data/branch/master/graph/badge.svg)](https://codecov.io/gh/lhoupert/analysis_eel_data)
[![License:MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flt-square)](https://opensource.org/licenses/MIT)

A repository associated with the [Extended Ellett Line (EEL)](https://projects.noc.ac.uk/ExtendedEllettLine/)  oceanographic dataset  It mostly contains [python scripts](https://github.com/lhoupert/analysis_eel_data/tree/master/notebooks)  used to analyse and visualise these oceanographic data.


This repo is a work in progress and should be updated regularly.

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

## List of current notebooks available (work in progress)


### 1. Maps

#### 1.1 Bathymetry map of the North Atlantic Ocean using *cartopy* and *matplotlib* axes functions
The notebook [01\_Plot\_map\_EEL\_data.ipynb](https://github.com/lhoupert/analysis_eel_data/blob/master/notebooks/01_Plot_map_EEL_data.ipynb) plot the bathymetry of the North Atlantic Ocean with two regional zoom and with the label of the hydrographic stations

![Bathymetry of the eastern North Atlantic with Extended Ellett Line section](https://uca0cd1a2dbea90e7cc2e17ff1f3.dl.dropboxusercontent.com/cd/0/inline/A6x41G18KkKDLypjYAM5RzDjLN7RRS4fpOqX7_wu6X31oEIeli6fC0tnx0w4ahgktao3rjF-ehxKzI-ZDAk-qz_ujaRBAiyQIuke9ZdiDUUKAbUFqAwsWdyZD2e7y42r1_k/file#)

<br/>
#### 1.2 Bathymetry map with mean current vector and mean current ellipse overlaid using *cartopy* and *xarray*

*work in progress*

<br/>

### 2. Data exploration and visualisation

#### 2.1 Exploration of EEL dataset and contour plots of mean quantities
The notebook [02\_Explore\_EEL\_meanfield.ipynb](https://github.com/lhoupert/analysis_eel_data/blob/master/notebooks/02_Explore_EEL_meanfield.ipynb) is used to explore the EEL dataset. It also generates summary figures of the mean and standard deviation of the velocity, teperature, salinity and density along the EEL section (see example below). 

*Note: this notebook has been written at early stage in my transition from Matlab to Python and is mostly based on Python Dataframe. The use of [xarray](http://xarray.pydata.org/en/stable/) would have certainly shortened and optimised this code.*

![Exemple of contour plot accross the EEL section](https://uc7aa98171c58ce3a72662dc2ad3.dl.dropboxusercontent.com/cd/0/inline/A6yBwOLWUQU30Tq2vuzKN5a7phHunpUD3brjtu8vps5v4u8SjR-htcWc_rGWXKGRFlDkifYw5aaubcOBZpWaY7sNLFnRISyr4bDjmjxYF8aahGTbFwFDs1ELi2kmFFG18bs/file#)

<br/>
#### ...

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>
