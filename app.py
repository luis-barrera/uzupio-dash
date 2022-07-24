# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
# import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

server = app.server

df = pd.read_csv("https://storage.googleapis.com/small-projects-luis-barrera/uzupio.csv")
# df = pd.read_csv("uzupio.csv")
# df = df.iloc[::-1]

fig = px.bar(df,
             x = "Dictamen",
             y = ["Adhieren", "No se Adhieren", "Abstienen"],
             height = 1000,
             width = 1600,
             color_discrete_sequence = ["#b5e48c", "#ef476f", "#fff3b0"],
             title = "Votación de la Constitución de la República de Uzupio")

fig.update_yaxes(title_text = "Votantes")
fig.update_xaxes(tickangle = -90,
                 showticklabels = True,
                 # ticklabelmode = "period",
                 ticklabelposition = "outside right",
                 tickprefix = "      ",
                 ticklabeloverflow = "allow")

fig.update_layout(legend=dict(
    yanchor="top",
    y=1.08,
    xanchor="right",
    x=0.5
))

config = {"responsive": True}
config = {}

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
