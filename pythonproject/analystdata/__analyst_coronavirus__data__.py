import inline as inline
import matplotlib
import pandas as pd
import json
import requests

import matplotlib.pyplot as plt
from matplotlib import style
plt.rcParams['figure.figsize'] = 20,8
style.use('ggplot')
#%matplotlib inline

import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.offline import download_plotlyjs,init_notebook_mode, plot, iplot
plt.rcParams['figure.figsize'] = 20,8

import cufflinks as cf

import folium
pyo.init_notebook_mode(connected = True)
cf.go_offline()

import numpy as np
from random import randint

import pycountry

import os


df_confirmed = pd.read_csv("./raw_covid_world/time_series_covid19_confirmed_global.csv")
df_deaths = pd.read_csv("./raw_covid_world/time_series_covid19_deaths_global.csv")
df_recovered = pd.read_csv("./raw_covid_world/time_series_covid19_recovered_global.csv")
