# BCSD-downscaler


To get up and running with this you're going to need both an observation and model dataset with as many overlapping time steps as possible.

```
wget http://hydrology.princeton.edu/data/pgf/v1/1.0deg/monthly/prcp_monthly_1948-2010.nc
```


```
wget https://esgf-data1.llnl.gov/thredds/fileServer/css03_data/CMIP6/CMIP/INM/INM-CM4-8/historical/r1i1p1f1/Amon/pr/gr1/v20190530/pr_Amon_INM-CM4-8_historical_r1i1p1f1_gr1_195001-199912.nc
```


## Environment setup

Most of the python packages required should be contained in the included environment.yaml file.  You can create a new conda environment from the listed packages by running:


```
conda env create -n bcsd --file environment.yml
```