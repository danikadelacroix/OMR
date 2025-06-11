import sqlite3

def view_all_results():
    conn = sqlite3.connect("omr_results.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM results")
    rows = cursor.fetchall()
    print("Stored OMR Results:")
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    view_all_results()
