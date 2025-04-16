
import plotly.express as px
import pandas as pd
import clickhouse_connect

client = clickhouse_connect.get_client(host='localhost', port=8123)

def get_goals_and_assists_by_team():
    query = '''
    SELECT 
        team_name,
        SUM(events_goals) AS total_goals,
        SUM(events_assists) AS total_assists
    FROM player_stats
    GROUP BY team_name
    ORDER BY total_goals DESC
    '''
    result = client.query(query).result_set
    df = pd.DataFrame(result, columns=['team_name', 'total_goals', 'total_assists'])
    fig = px.bar(df, x='team_name', y=['total_goals', 'total_assists'], barmode='group',
                 title='Total Goals and Assists by Team')
    return fig

def get_avg_minutes_by_foot():
    query = '''
    SELECT 
        player_foot,
        AVG(minutes_played) AS avg_minutes_played
    FROM player_stats
    GROUP BY player_foot
    ORDER BY avg_minutes_played DESC
    '''
    result = client.query(query).result_set
    df = pd.DataFrame(result, columns=['player_foot', 'avg_minutes_played'])
    fig = px.bar(df, x='player_foot', y='avg_minutes_played',
                 title='Average Minutes Played by Player Foot')
    return fig

def get_top_goal_scorers():
    query = '''
    SELECT 
        name,
        MAX(events_goals) AS max_goals_in_a_match
    FROM player_stats
    GROUP BY name
    ORDER BY max_goals_in_a_match DESC
    LIMIT 10
    '''
    result = client.query(query).result_set
    df = pd.DataFrame(result, columns=['name', 'max_goals_in_a_match'])
    fig = px.bar(df, x='name', y='max_goals_in_a_match', color='max_goals_in_a_match',
                 title='Top 10 Players with Maximum Goals in a Match')
    return fig

def get_top_yellow_cards():
    query = '''
    SELECT 
        name,
        SUM(events_yellow_cards) AS total_yellow_cards
    FROM player_stats
    GROUP BY name
    ORDER BY total_yellow_cards DESC
    LIMIT 10
    '''
    result = client.query(query).result_set
    df = pd.DataFrame(result, columns=['name', 'total_yellow_cards'])
    fig = px.bar(df, x='name', y='total_yellow_cards', color='total_yellow_cards',
                 title='Top 10 Players with Maximum Yellow Cards')
    return fig

def get_total_height_by_team():
    query = '''
    SELECT 
        team_name,
        SUM(height) AS total_height
    FROM player_stats
    GROUP BY team_name
    ORDER BY total_height DESC
    '''
    result = client.query(query).result_set
    df = pd.DataFrame(result, columns=['team_name', 'total_height'])
    fig = px.bar(df, x='team_name', y='total_height',
                 title='Total Height by Team')
    return fig
