# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:43:44 2021

@author: srappold
"""

import pandas as pd
import plotly.offline as py
from plotly.offline import plot
import plotly.graph_objects as go
import numpy as np

nodes = pd.read_csv('Data/Processed/nodes.csv')
links = pd.read_csv('Data/Processed/links.csv')

#print(nodes.head())
#print(links.head())

temp = pd.DataFrame(links[links.Group_Count>225])

data = dict(type='sankey',
	node = dict(
		pad=1,
		thickness=5,
		line=dict(
			color='black',
			width=.5),
		label=nodes['Systems']),
	link = dict(
		source = temp['FromSystemID'],
		target = temp['SystemID'],
		value = temp['Group_Count'])
)

layout = dict(
	title = 'System to System Element Flow',
	font = dict(
		size = 20))
fig = dict(data=[data], layout=layout)

print(links[links.Group_Count>225])
py.plot(fig, validate=True)