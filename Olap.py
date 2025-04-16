import clickhouse_connect
from Clickhouse import insert_data

client = clickhouse_connect.get_client(host='localhost', port=8123)

def olap_queries():
    query_1 = '''
    SELECT 
        team_name,
        SUM(events_goals) AS total_goals,
        SUM(events_assists) AS total_assists
    FROM player_stats
    GROUP BY team_name
    ORDER BY total_goals DESC
    '''
    result_1 = client.query(query_1)
    print("Total Goals and Assists by Team:")
    for row in result_1.result_set:
        print(row)

    query_2 = '''
    SELECT 
        player_foot,
        AVG(minutes_played) AS avg_minutes_played
    FROM player_stats
    GROUP BY player_foot
    ORDER BY avg_minutes_played DESC
    '''
    result_2 = client.query(query_2)
    print("\nAverage Minutes Played by Player Foot:")
    for row in result_2.result_set:
        print(row)

    query_3 = '''
    SELECT 
        name,
        MAX(events_goals) AS max_goals_in_a_match
    FROM player_stats
    GROUP BY name
    ORDER BY max_goals_in_a_match DESC
    LIMIT 10
    '''
    result_3 = client.query(query_3)
    print("\nTop 10 Players with Maximum Goals in a Match:")
    for row in result_3.result_set:
        print(row)

    query_4 = '''
    SELECT 
        name,
        SUM(events_yellow_cards) AS total_yellow_cards
    FROM player_stats
    GROUP BY name
    ORDER BY total_yellow_cards DESC
    LIMIT 10
    '''
    result_4 = client.query(query_4)
    print("\nTop 10 Players with Maximum Yellow Cards:")
    for row in result_4.result_set:
        print(row)

    query_5 = '''
    SELECT 
        team_name,
        SUM(height) AS total_height
    FROM player_stats
    GROUP BY team_name
    ORDER BY total_height DESC
    '''
    result_5 = client.query(query_5)
    print("\nTotal Height by Team:")
    for row in result_5.result_set:
        print(row)

if __name__ == "__main__":
    insert_data()
    olap_queries()
