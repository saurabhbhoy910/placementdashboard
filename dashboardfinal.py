import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go



branch = pd.DataFrame(None, None)
branch = branch.fillna(0) 

app = dash.Dash()

colors = {
    'background': '#19EEC7',
    'text': '#EE6619'
}

df = pd.read_csv(
    '../placement_final.csv')

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Placement Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

html.Div(style={'backgroundColor': colors['background']}, children=[

html.H4(
        children='Eligible vs Non-Eligible',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }   
    ),

dcc.Graph(
   figure=go.Figure(
       data=[
          go.Bar(
          x=df['Branch'],
          y=df['Percent Eligible'],
          name='Eligible'
        ),
          go.Bar(
          x=df['Branch'],
          y=df['Percent_Placed'],
          name='Placed'
      )
]),
  style={'height': 300},
   id='bar'
 ),

html.H4(
        children='Sector-Wise Placement Data',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }   
    ),

dcc.Graph(
   figure=go.Figure(
       data=[
          go.Bar(
          x=df['Branch'],
          y=df['Core'],
          name='Core'
        ),
          go.Bar(
          x=df['Branch'],
          y=df['Education'],
          name='Education'
      ),
       go.Bar(
          x=df['Branch'],
          y=df['Consulting'],
          name='Consulting'
        ),
          go.Bar(
          x=df['Branch'],
          y=df['Finance'],
          name='Finance'
      ),
       go.Bar(
          x=df['Branch'],
          y=df['FMCG'],
          name='FMCG'
        ),
          go.Bar(
          x=df['Branch'],
          y=df['IT / Software'],
          name='IT / Software'
      ),
       go.Bar(
          x=df['Branch'],
          y=df['Research and Development'],
          name='Research and Development'
      ),
       go.Bar(
          x=df['Branch'],
          y=df['Public Sector Undertaking'],
          name='Public Sector Undertaking'
        ),
          go.Bar(
          x=df['Branch'],
          y=df['Others'],
          name='Others'
      )


]),
  style={'height': 800},
   id='sector_wise'
 ),

html.H4(
        children='Eligible Student Who are not plcaced',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }   
    ),



dcc.Graph(
   figure=go.Figure(
       data=[
          go.Bar(
          x=df['Branch'],
          y=(100-df['Percent_Placed']/df['Percent Eligible']*100),
          name = 'Not_Placed_Average_Student'
        ),  
]),
  style={'height': 300},
   id='Eligible_Not_Placed'
 ),

html.H4(
        children='UG vs PG Percentage Placed',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }   
    ),

dcc.Graph(
   figure=go.Figure(
       data=[
          go.Bar(
          x=df['UG/PG'],
          y=df['Percent_Placed'],
          name = 'UG vs PG Percetage Placed'
        ),  
]),
  style={'height': 300},
   id='UG/PG Percentage Placed'
 ),

html.H4(
        children='Percent Placed vs Avg salary',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }   
    ),



dcc.Graph(
        id='placed-avg_sal',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['Branch'] == i]['Percent_Placed'],
                    y=df[df['Branch'] == i]['Avg_Sal'],
                    text=df[df['Branch'] == i]['Branch'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 20,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.Branch.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Placed student'},
                yaxis={'title': 'Avg Sal'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
)

])
])

if __name__ == '__main__':
    app.run_server()
