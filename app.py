# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
from whitenoise import WhiteNoise

app = Dash(__name__)

server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("https://raw.githubusercontent.com/luis-barrera/uzupio-dash/master/uzupio.csv")
# df = df.iloc[::-1]

fig = px.bar(df,
             x = "Dictamen",
             y = ["Adhieren", "No se Adhieren", "Abstienen"],
             # text = "Dictamen",
             height = 1000,
             title = "Votación de la Constitución de la República de Uzupio")

fig.update_layout(legend=dict(
    yanchor="top",
    y=1.08,
    xanchor="right",
    x=0.5
))
# fig.update_xaxes(title_text = "Votantes")
# fig.update_yaxes(showtick=False)

config = {"responsive": True}

app.layout = html.Div(children=[
    html.H1(children='Uzupio'),

    html.Div(children='''
        Por luis-barrera
    '''),
    dcc.Graph(id='example-graph',
                      figure=fig,
                      config=config)

])

if __name__ == '__main__':
    app.run_server(debug=True)
