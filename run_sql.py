import sqlite3

print("Running SQL Schema and Queries test...\n")

# Connect to database
conn = sqlite3.connect('bluestock_mf.db')
cursor = conn.cursor()

# 1. Execute schema.sql
try:
    with open('sql/schema.sql', 'r') as f:
        schema_script = f.read()
    cursor.executescript(schema_script)
    print(" schema.sql executed successfully!")
except Exception as e:
    print("X Schema Error:", e)

# 2. Execute queries.sql
try:
    with open('sql/queries.sql', 'r') as f:
        queries_script = f.read()
    
    # Run each SQL statement
    statements = queries_script.split(';')
    print("\n--- Running Queries Output ---")
    for stmt in statements:
        stmt = stmt.strip()
        if stmt and not stmt.startswith('--'):
            print(f"\nExecuting: {stmt[:40]}...")
            cursor.execute(stmt)
            results = cursor.fetchall()
            for row in results:
                print("  ", row)
                
    print("\n queries.sql executed successfully!")
except Exception as e:
    print("X Queries Error:", e)

conn.close()