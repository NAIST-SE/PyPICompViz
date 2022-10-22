#import packages
import pandas as pd
import plotly.express as px
import numpy as np

#import dataset
path = "dataset/"
df_requests = pd.read_csv('dataset_requests.csv')
df_flask = pd.read_csv('dataset_flask.csv')
df_jinja2 = pd.read_csv('dataset_jinja2.csv')
df_pytz = pd.read_csv('dataset_pytz.csv')

#visualization of Requests project
fig_contributor_requests = px.treemap(df_requests, path=[px.Constant("Requests project has 465 contributor"), 'Maintainer', 'Competency Level', 'File Name'], 
                 values='Size', color='Competency Level',
                 color_discrete_map={
                     'AB':'springgreen',
                     'A' : 'springgreen',
                     'B' : 'springgreen',
                     'C1':'MediumPurple', 
                     'C2':'orangered'})
fig_contributor_requests.data[0].textinfo = 'label+value'
fig_contributor_requests.update_layout(margin = dict(t=40, l=30, r=55, b=40))

#visualization of Flask project
fig_contributor_flask = px.treemap(df_flask, path=[px.Constant("Flask project has 363 contributor"), 'Maintainer', 'Competency Level', 'File Name'], 
                 values='Size', color='Competency Level',
                 color_discrete_map={
                     'AB':'springgreen',
                     'A' : 'springgreen',
                     'B' : 'springgreen',
                     'C1':'MediumPurple', 
                     'C2':'orangered'})
fig_contributor_flask.data[0].textinfo = 'label+value'
fig_contributor_flask.update_layout(margin = dict(t=40, l=30, r=55, b=40))

#visualization of Jinja2 project
fig_contributor_jinja2 = px.treemap(df_jinja2, path=[px.Constant("Jinja2 project has 203 contributor"), 'Maintainer', 'Competency Level', 'File Name'], 
                 values='Size', color='Competency Level',
                 color_discrete_map={
                     'AB':'springgreen',
                     'A' : 'springgreen',
                     'B' : 'springgreen',
                     'C1':'MediumPurple', 
                     'C2':'orangered'})
fig_contributor_jinja2.data[0].textinfo = 'label+value'
fig_contributor_jinja2.update_layout(margin = dict(t=40, l=30, r=55, b=40))

#visualization of Pytz project
fig_contributor_pytz = px.treemap(df_pytz, path=[px.Constant("Pytz project has 15 contributor"), 'Maintainer', 'Competency Level', 'File Name'], 
                 values='Size', color='Competency Level',
                 color_discrete_map={
                     'AB':'springgreen',
                     'A' : 'springgreen',
                     'B' : 'springgreen',
                     'C1':'MediumPurple', 
                     'C2':'orangered'})
fig_contributor_pytz.data[0].textinfo = 'label+value'
fig_contributor_pytz.update_layout(margin = dict(t=40, l=30, r=55, b=40))

# Visualization display
fig_contributor_requests.show()
fig_contributor_flask.show()
fig_contributor_jinja2.show()
fig_contributor_pytz.show()
