def OHLCgraph(go, df):
    
    
    fig = go.Figure([go.Ohlc(
        x=df['date'],
        open=df['open'], high=df['high'],
        low=df['low'], close=df['close'],
        increasing_line_color= 'black', decreasing_line_color= 'red'
    )])

    return fig


def Candlegraph(go, df):
    
    
    fig = go.Figure([go.Candlestick(
        x=df['date'],
        open=df['open'], high=df['high'],
        low=df['low'], close=df['close'],
        increasing_line_color= 'black', decreasing_line_color= 'red'
    )])


    return fig


