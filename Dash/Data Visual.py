import pandas as pd
from dash import Dash,dcc,html
import plotly.express as p
from plotly.express import line
from dash import Input,Output


source = 'Dash\Daily_sales_Data_Formatted.csv'
file = pd.read_csv(source)
file = file.sort_values(by ="Date")


app = Dash(__name__)


header = html.H1(
    "Pink Morsel Sales",
    id="header",
    style={
        'textAlign' : 'center'
        
    }
)
def createGraph(file):
    chart = line(file,x="Date",y="Sales")
    chart.update_layout(
        plot_bgcolor = "#d0e0e3",
        paper_bgcolor = "#d9ead3"

    )
    return chart

graph = dcc.Graph(
        id= "lineGraph",
        figure=createGraph(file)
    )


pick_region = dcc.RadioItems(
    ["north","south","east","west","all"],
    id= "region", inline=True,
    style={
        'color': 'DarkBlue', 'font_size': 50
    }
)
@app.callback(
    Output(graph,"figure"),
    Input(pick_region,"value")
    
    
)
def newgraph(user):
    if user == "all": 
        newdata = file
    else:
        newdata = file[file["Region"] == user]
    figure = createGraph(newdata)
    return figure


app.layout = html.Div(
    [
        header, graph, pick_region
    ]
)
if __name__ == '__main__':
    app.run_server(debug=True)
