# Football-Player-Performance-Analytics

An interactive dashboard built with Python, ClickHouse, and Dash to analyze Indian Super League (ISL) player stats using modular ETL and OLAP querying.

## 🚀 Features

- 📥 ETL pipeline to clean and load player data into ClickHouse
- 🧠 OLAP queries for team & player insights (goals, assists, cards, etc.)
- 📊 Dash + Plotly dashboard with 5 dynamic visualizations
- 🧱 Modular codebase for scalability and maintainability

## 📁 Project Structure

- `Data_Cleaning.py` – Cleans raw CSV data  
- `Clickhouse.py` – Table schema & data insertion  
- `OLAP.py` – SQL queries for analysis  
- `Graph.py` – Plotly-based visualizations  
- `main.py` – Dash app frontend  

## 📦 Setup

```bash
pip install -r requirements.txt
python Clickhouse.py
python main.py  # open http://127.0.0.1:8050
Dataset
https://lnkd.in/gsTban22
