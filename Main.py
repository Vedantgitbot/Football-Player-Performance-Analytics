from dash import Dash, html, dcc
import Graph  # or 'graph' if your file is lowercase

app = Dash(__name__)
app.title = "Football Player Performance Dashboard"

app.layout = html.Div([
    html.H1("Football Player Performance Analytics", style={'textAlign': 'center'}),

    dcc.Graph(figure=Graph.get_goals_and_assists_by_team()),
    dcc.Graph(figure=Graph.get_avg_minutes_by_foot()),
    dcc.Graph(figure=Graph.get_top_goal_scorers()),
    dcc.Graph(figure=Graph.get_top_yellow_cards()),
    dcc.Graph(figure=Graph.get_total_height_by_team())
], style={'padding': '20px'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
