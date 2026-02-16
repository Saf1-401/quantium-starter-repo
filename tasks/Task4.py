from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("../data/full_daily_sales_data.csv")

app.layout = html.Div([
    html.H1(
      "Pink Morsel Visualisation",
      style={'textAlign': 'center'}
    ),
    dcc.Graph(id='sales-figure'),
    html.Div(
      [
        html.Label("Select Region:", style={'fontWeight': 'bold', 'margin-right': '10px'}),
        dcc.RadioItems(
          options=df['region'].unique(),
          value=df['region'].unique()[0],
          id='regions',
          inline=True
        )
      ], 
      style={
        'textAlign': 'center',
        'borderRadius': '10px',
        'border': '2px solid black'
      }
    )
])

@callback(
    Output('sales-figure', 'figure'),
    Input('regions', 'value'))
def update_graph(region):
    dff = df[df['region'] == region]
    fig = px.line(dff, x='date', y='sales', title='Sales Over Time')
    return fig


if __name__ == "__main__":
    app.run(debug=True)