FROM jupyter/datascience-notebook

MAINTAINER Myles Braithwaite <me@mylesbraithwaite.com>

# Install some Notebook Extensions and other libraries.
USER $NB_USER

# Install pipenv
RUN conda install -c conda-forge pipenv

# Install Facebook's Prophet Python and R library
RUN conda install --quiet --yes -c conda-forge fbprophet

# Install some Python libraries
RUN conda install --quiet --yes -c damianavila82 rise
RUN conda install --quiet --yes -c conda-forge pandas-datareader
RUN conda install --quiet --yes -c conda-forge statsmodels
RUN conda install --quiet --yes -c conda-forge beautifulsoup4
RUN conda install --quiet --yes -c conda-forge boto3

RUN pip3 install quandl

# Install Pipfile dependencies
RUN pipenv install --system --deploy
