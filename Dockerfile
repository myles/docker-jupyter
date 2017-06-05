FROM jupyter/datascience-notebook

MAINTAINER Myles Braithwaite <me@mylesbraithwaite.com>

# Install some Notebook Extensions and other libraries.
USER $NB_USER

# Install Tensorflow in Python 3 and 2
RUN conda install --quiet --yes 'tensorflow=1.0*'
RUN conda install --quiet --yes -n python2 'tensorflow=1.0*'

# Install Facebook's Prophet Python and R library
RUN conda install -c conda-forge fbprophet

