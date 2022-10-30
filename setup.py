from setuptools import setup

setup(
   name='weatherPredict',
   version='0.1.0',
   description='A package that reads weather data from the visual crossing API and build time series models',
   author='Josie Park',
   author_email='josiepark92@hotmail.co.uk',
   packages=['weatherPredict'],
   install_requires=[
      'numpy',
      'pandas',
      'jupyter',
      'notebook',
      'scikit-learn',
      'statsmodels',
      'matplotlib',
      'neuralprophet',
      'pmdarima'
   ]
)