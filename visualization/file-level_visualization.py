#import packages
import pandas as pd
import plotly.express as px
import numpy as np

#import dataset
df_requests = pd.read_csv('dataset_requests.csv')
df_flask = pd.read_csv('dataset_flask.csv')
df_jinja2 = pd.read_csv('dataset_jinja2.csv')
df_pytz = pd.read_csv('dataset_pytz.csv')

#Visualization of Requests Project
fig_file_requests = px.treemap(df_requests, path=[px.Constant("Requests project has 16 files"), 'File Name', 'Competency Level', 'Maintainer'], 
                 values='Size', color='Competency Level',
                 color_discrete_map={
                     'AB':'springgreen',
                     'A' : 'springgreen',
                     'B' : 'springgreen',
                     'C1':'MediumPurple', 
                     'C2':'orangered'})
fig_file_requests.data[0].textinfo = 'label+value'
fig_file_requests.update_layout(margin = dict(t=40, l=30, r=55, b=40))

#Visualization of Flask Project
fig_file_flask = px.treemap(df_flask, path=[px.Constant("Flask project has 26 files"), 'File Name', 'Competency Level', 'Maintainer'], 
                 values='Size', color='Competency Level',
                 color_discrete_map={
                     'AB':'springgreen',
                     'A' : 'springgreen',
                     'B' : 'springgreen',
                     'C1':'MediumPurple', 
                     'C2':'orangered'})
fig_file_flask.data[0].textinfo = 'label+value'
fig_file_flask.update_layout(margin = dict(t=40, l=30, r=55, b=40))

#Visualization of Jinja2 Project
fig_file_jinja2 = px.treemap(df_jinja2, path=[px.Constant("Jinja2 project has 33 files"), 'File Name', 'Competency Level', 'Maintainer'], 
                 values='Size', color='Competency Level',
                 color_discrete_map={
                     'AB':'springgreen',
                     'A' : 'springgreen',
                     'B' : 'springgreen',
                     'C1':'MediumPurple', 
                     'C2':'orangered'})
fig_file_jinja2.data[0].textinfo = 'label+value'
fig_file_jinja2.update_layout(margin = dict(t=40, l=30, r=55, b=40))

#Visualization of Pytz Project
fig_file_pytz = px.treemap(df_pytz, path=[px.Constant("Pytz project has 9 files"), 'File Name', 'Competency Level', 'Maintainer'], 
                 values='Size', color='Competency Level',
                 color_discrete_map={
                     'AB':'springgreen',
                     'A' : 'springgreen',
                     'B' : 'springgreen',
                     'C1':'MediumPurple', 
                     'C2':'orangered'})
fig_file_pytz.data[0].textinfo = 'label+value'
fig_file_pytz.update_layout(margin = dict(t=40, l=30, r=55, b=40))

#Visualization Display
fig_file_requests.show()
fig_file_flask.show()
fig_file_jinja2.show()
fig_file_pytz.show()
