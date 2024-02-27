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
import os

def make_sankey():

	nodes = pd.read_csv(os.getcwd() + '/Data/03 Processed/nodes.csv')
	links = pd.read_csv(os.getcwd() + '/Data/03 Processed/links.csv')
	#nodes = pd.read_csv('Data/Processed/nodes.csv')
	#links = pd.read_csv('Data/Processed/links.csv')

	print(os.getcwd())

	temp = pd.DataFrame(links[(links['FromSystemID'] == 59) | (links['SystemID'] == 59)])

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

	data = dict(type='sankey',
		node = dict(
			pad=1,
			thickness=5,
			line=dict(
				color='black',
				width=.5),
			label=nodes['Systems']),
		link = dict(
			source = links['FromSystemID'],
			target = links['SystemID'],
			value = links['Group_Count'])
	)


	layout = dict(
		title = 'System to System Element Flow',
		font = dict(
			size = 20))
	fig = dict(data=[data], layout=layout)

	#print(links[links.Group_Count>225])
	
	try:
		py.plot(fig, validate=True, filename=os.path.join(os.getcwd(), 'Reports', 'Systems.html'))
		print('HTML File Generated')
	except Exception as e:
		print('Error: ', e)


	print('completed')