# Member 2 — Database Handling (SQLite3 + Python)
# Goal: Create the DB, schema, and reliably insert sensor rows. Offer simple queries to verify data.
# Responsibilities
# Create robot_sensors.db and table readings with columns: id, sensor_id, timestamp, distance_cm, temperature_c, battery_pct, status.
# Write a robust insert routine (bulk insert preferred) that reads readings.csv or consumes DataFrame from Member 1.
# Provide helper queries for Member 3 & 4: e.g., SELECT * FROM readings WHERE sensor_id = ? LIMIT ?.
# Optionally, add an UPDATE interface to mark status='ANOMALY'.
# Step-by-step tasks
# Use sqlite3 module (built-in). Create table using IF NOT EXISTS.
# Use conn.executemany() or pandas.to_sql() for bulk inserts.
# Provide a small API file store_to_db.py with functions:
# create_db(path)
# insert_rows_from_csv(csv_path)
# fetch_recent(sensor_id, n)
# update_status(row_id, status)
#table is already made in robot2.py
#so now dont create table again using function create_db(path)

