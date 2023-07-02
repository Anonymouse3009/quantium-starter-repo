import pandas as pd
from dash import Dash,dcc,html
import plotly.express as p

app = Dash(__name__)

source = 'Daily_sales_Data_Formatted.csv'
file = pd.read_csv(source)
file = file.sort_values(by ="Date")

header = html.H1(
    "Pink Morsel Sales",
    id="header"
)

fig = p.line(file,x="Date",y="Sales")
visual = dcc.Graph(
    id = "graph",
    figure= fig
)
app.layout = html.Div(
    [
        header, visual
    ]
)
if __name__ == '__main__':
    app.run_server(debug=True)
