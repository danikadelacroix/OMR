import sqlite3

def store_result(student_id, answers, correct_answers, score):
    conn = sqlite3.connect("omr_results.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO results (student_id, answers, correct_answers, score)
        VALUES (?, ?, ?, ?)
    ''', (student_id, ",".join(map(str, answers)), ",".join(map(str, correct_answers)), int(score)))
    
    conn.commit()
    conn.close()
