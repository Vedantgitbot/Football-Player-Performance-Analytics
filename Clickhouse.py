import clickhouse_connect
from Data_Cleaning import clean_data

import os

client = clickhouse_connect.get_client(
    host=os.getenv('CLICKHOUSE_HOST'),
    port=int(os.getenv('CLICKHOUSE_PORT', 8443)),
    username=os.getenv('CLICKHOUSE_USERNAME'),
    password=os.getenv('CLICKHOUSE_PASSWORD'),
    secure=True
)

def create_table():
    client.command('DROP TABLE IF EXISTS player_stats')
    client.command('''
        CREATE TABLE IF NOT EXISTS player_stats (
            id UInt32,
            name String,
            team_name String,
            events_goals UInt8,
            events_assists UInt8,
            events_yellow_cards UInt8,
            events_red_cards UInt8,
            minutes_played UInt16,
            player_foot String,
            height UInt16
        ) ENGINE = MergeTree()
        ORDER BY id
    ''')
    result = client.query('DESCRIBE TABLE player_stats')
    print(result.result_set)

def insert_data():
    df = clean_data()
    print("First few rows of cleaned data:")
    print(df.head())

    df = df.fillna({
        'id': 0,
        'name': '',
        'team_name': '',
        'events_goals': 0,
        'events_assists': 0,
        'events_yellow_cards': 0,
        'events_red_cards': 0,
        'minutes_played': 0,
        'player_foot': 'Unknown',
        'height': 0
    })


    df.columns = [col.lower() for col in df.columns]

    df = df.astype({
        'id': int,
        'name': str,
        'team_name': str,
        'events_goals': int,
        'events_assists': int,
        'events_yellow_cards': int,
        'events_red_cards': int,
        'minutes_played': int,
        'player_foot': str,
        'height': int
    })


    data = df[
    ['id', 'name', 'team_name', 'events_goals', 'events_assists',
     'events_yellow_cards', 'events_red_cards', 'minutes_played',
     'player_foot', 'height']
].values.tolist()


    try:
        client.insert(
            table='player_stats',
            data=data,
            column_names=[
                'id', 'name', 'team_name', 'events_goals', 'events_assists',
                'events_yellow_cards', 'events_red_cards', 'minutes_played',
                'player_foot', 'height'
            ]
        )
        print("Data inserted successfully!")
    except Exception as e:
        print("Error inserting data:")
        import traceback
        traceback.print_exc()



if __name__ == "__main__":
    create_table()
    insert_data()
