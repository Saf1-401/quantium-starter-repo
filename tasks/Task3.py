from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("full_daily_sales_data.csv")

fig = px.line(df, x='date', y='sales', title='Sales Over Time')

app.layout = html.Div([
    html.H1("Pink Morsel Visualisation"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)