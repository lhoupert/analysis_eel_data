# Notes on how to hide cells when exporting from notebook .ipynb files to html


<br>
Solution found on a *stackoverflow* post [here](https://stackoverflow.com/a/48084050)

## Prerequisites
Having Jupyter installed with the packages [jupyterlab-celltags](https://github.com/jupyterlab/jupyterlab-celltags), [nbconvert](https://nbconvert.readthedocs.io/en/latest/#) and [jupyter\_contrib_nbextensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/index.html) 


## Steps
1. Add specific tags (e.g. `hide_input`, `hide_output`) to any cells that need to be hidden using the tag editor built into the notebook or JupyterLab.

2. Convert the notebook with nbconvert:

```
jupyter nbconvert file.ipynb 
--TagRemovePreprocessor.remove_input_tags='{"hide_input"}' 
--TagRemovePreprocessor.remove_all_outputs_tags='{"hide_output"}'
```


