import dash
from dash.html import Hr
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
import plotly.express as px
from parse import getParsedDF
from process import getCurDF
from datetime import date
from plots.plot import OHLCgraph, Candlegraph
import dash_table
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from info import getInfo

def init_dashboard(server):


    df = getParsedDF()
    symbols = df.symbol.unique()

    types = ['OLHC', 'Candlestick']

    funcs = {'OLHC':OHLCgraph, 'Candlestick':Candlegraph}

    

    vals = [ 'End Date', 'Start Date', 'Symbol', 'Type']
    prev = ''

    SIDEBAR_STYLE = {
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'bottom': 0,
        'width': '30%',
        'padding': '10px 10px',
        'background-color': '#f8f9fa',
        "overflow": "scroll"
    }

    STYLE_CELL = {
                'font_family': 'cursive',
                'font_size': '26px',
                'text_align': 'center'
            },

    CONTENT_STYLE = {
        'margin-left': '30%',
        'margin-right': '5%',
        'padding': '20px 10p'
    }

    TEXT_STYLE = {
        'textAlign': 'center',
        'color': '#191970'
    }


    controls = dbc.FormGroup(
        [
            dcc.Store(id='stored', storage_type='session'),
            html.P('Symbol', style={
                'textAlign': 'center',
                
            }),
            dcc.Dropdown(
                id="symbol",
                options=[
                    {"label": symbol, "value": symbol}
                    for symbol in symbols
                ],
                value="AAPL",
                
            ),
            html.P('Start Date', style={
                'textAlign': 'center',
                
            }),
            dcc.DatePickerRange(
                id='date_range',
                min_date_allowed=date(1995, 8, 5),
                max_date_allowed=date(2022, 9, 19),
                initial_visible_month=date(2021, 1, 4),
                end_date=date(2021, 1, 10),
                start_date=date(2021, 1, 4)
            ),

            html.P('Type', style={
                'textAlign': 'center',
                
            }),
            dcc.Dropdown(
                id="type",
                options=[
                    {"label": type1, "value": type1}
                    for type1 in types
                ],
                value="OLHC",
                
            ),

            html.Hr(),

            html.P('History', style={
                'textAlign': 'center',
                
            }),

            
            
            dash_table.DataTable(
                id='history',
                columns=[{'name': i, 'id': i} for i in vals],
                style_cell=STYLE_CELL
            )

        ]
    )

    sidebar = html.Div(
        [
            html.Hr(),
            controls
        ],
        style=SIDEBAR_STYLE,
    )




    content_Row = dbc.Row(
        [
            dbc.Col(
                dcc.Graph(id="graph"), md=12
            )

        ]
    )

    Row2 = dbc.Row(
        [
            dbc.Col(
                dash_table.DataTable(
                    id='info',
                    style_cell=STYLE_CELL
                )
            )

        ]
    )


    dash_table.DataTable(
                id='history',
                columns=[{'name': i, 'id': i} for i in vals],
                style_cell=STYLE_CELL
            )



    content = html.Div(
        [
            html.H2('Stocks Chart', style=TEXT_STYLE),
            html.Hr(),
            content_Row,
            Row2

        ],
        style=CONTENT_STYLE
    )

    app = dash.Dash(server = server, routes_pathname_prefix="/dashboard/", external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    app.layout = html.Div([content, sidebar])

    @app.callback([Output("graph", "figure"), Output('stored', 'data'), Output('history', 'data')], [Input("symbol", "value"),Input("type", "value") ,Input("date_range", "start_date"), Input('date_range', 'end_date'), Input('stored', 'data') ])
    def update(symbol, type, start_date, end_date, stored):
        
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        curDf = getCurDF(df, symbol, start_date, end_date)
        
        func = funcs[type]

        new_stored = None
        storeddf = pd.DataFrame.from_dict(stored)
        new = {'Symbol':[symbol], 'Start Date':[start_date], 'End Date':[end_date], 'Type':[type]}
        newdf = pd.DataFrame.from_dict(new)
        
        if(stored is None):
            new_stored = newdf
            
            
        
        else:
            new_stored = storeddf.append(newdf)
            
        return func(go, curDf), new_stored.to_dict('records'), storeddf.to_dict('records')



    return app.server



