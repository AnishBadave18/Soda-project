 
import duckdb
 
con = duckdb.connect("duckdb.db")
con.execute("""
    CREATE TABLE IF NOT EXISTS transactions AS
    SELECT * FROM read_csv_auto('transactions_unclean.csv')
""")
print("Table created successfully!")
print(con.execute("SELECT COUNT(*) FROM transactions").fetchall())
con.close()
 