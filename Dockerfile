FROM jupyter/datascience-notebook

MAINTAINER Myles Braithwaite <me@mylesbraithwaite.com>

# Install some Notebook Extensions and other libraries.
USER $NB_USER

# Install Tensorflow
RUN conda install --quiet --yes 'tensorflow=1.0*'

# Install Facebook's Prophet Python and R library
RUN conda install --quiet --yes -c conda-forge fbprophet

# Install Sony's NNAbla library
RUN conda install --quiet --yes libgcc
RUN pip2 install nnabla

# Install some Python libraries
RUN conda install --quiet --yes -c damianavila82 rise
RUN conda install --quiet --yes -c conda-forge pandas-datareader
RUN conda install --quiet --yes -c conda-forge statsmodels
RUN conda install --quiet --yes -c conda-forge beautifulsoup4
RUN conda install --quiet --yes -c conda-forge boto3

RUN pip3 install quandl
