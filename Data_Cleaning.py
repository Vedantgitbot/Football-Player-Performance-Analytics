import pandas as pd

def clean_data():
    df = pd.read_csv("/Users/vedantbrahmbhatt/Desktop/Players_OLAP/isl_player_final.csv")
    df.columns = [col.strip().lower().replace('.', '_') for col in df.columns]
    df.fillna({
        'events_goals': 0,
        'events_assists': 0,
        'events_yellow_cards': 0,
        'events_red_cards': 0,
        'minutes_played': 0,
        'height': 0,
        'player_foot': 'Unknown'
    }, inplace=True)
    df['player_foot'] = df['player_foot'].str.strip().str.lower().replace({'right': 'Right', 'left': 'Left'})
    df['height'] = pd.to_numeric(df['height'], errors='coerce').fillna(0).astype('int')
    df['minutes_played'] = pd.to_numeric(df['minutes_played'], errors='coerce').fillna(0).astype('int')
    df['events_goals'] = pd.to_numeric(df['events_goals'], errors='coerce').fillna(0).astype('int')
    df['events_assists'] = pd.to_numeric(df['events_assists'], errors='coerce').fillna(0).astype('int')
    df['events_yellow_cards'] = pd.to_numeric(df['events_yellow_cards'], errors='coerce').fillna(0).astype('int')
    df['events_red_cards'] = pd.to_numeric(df['events_red_cards'], errors='coerce').fillna(0).astype('int')
    df = df[df['id'].notnull() & df['name'].notnull()]
    selected_columns = [
        'id', 'name', 'team_name', 'events_goals', 'events_assists',
        'events_yellow_cards', 'events_red_cards', 'minutes_played',
        'player_foot', 'height'
    ]
    df = df[selected_columns]
    return df
