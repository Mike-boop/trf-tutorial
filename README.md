# TRF Tutorial

This repo will help guide you through the process of developing forward and backward models (we call the coefficients of the forward model the TRF, or temporal response function). It would be helpful for you to familiarise yourself a little with the theory of ridge regression, as well as linear system identification (i.e. understanding that the coefficients of a linear filter define the response function of the corresponding linear system.)

# Setup

- First, download the data into the data/ folder!
- Create a new virtual environment, and activate it.
- Install dependencies by running the following:

`pip install mne`

`pip install h5py`

`pip install scikit-learn`

`pip install jupyter`

`python setup.py develop`

`pip install emd`


MNE-python is a popular package for performing neuro-imaging analyses, i.e. analysing EEG, MEG, MRI data, etc... H5Py is a package for reading and writing HDF5 files (hierarchical data format files).
