---
dg-publish: true
---
# Venv

```python
#create 
python3 -m venv venv

"""
command line switch -m to allow modules to be located 
using the Python module namespace for execution as scripts 
"""

#activate/deactivate
source venv/bin/activate
deactivate 

#remove 
rm -r venv

"""
typically, 'env' folder is put in .gitignore
"""
```

# Conda

```python
#create
conda create -n <venv-name>

#info
conda info --envs
conda list (to show packages installed)

#activate/deactivate
conda activate <venv-name>
conda deactivate

#install
conda install numpy

#delete
conda env remove -n ENV_NAME

#to use conda env in vscode, activate conda and install jupyter
conda install jupyter

#if conda env not showing in vscode, install this in base env
conda install nb_conda_kernels
```

## Pin Dependencies

```python
# Save the environment
conda env export > conda_env.yml

# Re-create the environment
conda env create --file conda_env.yml

# Reactivate the environment
conda activate pytorch
```