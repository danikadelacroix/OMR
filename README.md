# 📝 Smart OMR Grading System

This project uses Python + OpenCV to scan and grade multiple choice OMR sheets using a webcam or image input. Results are stored in SQLite database.

## Tech Stack:
- Python, OpenCV, NumPy
- SQLite (db_utils.py)
- Webcam/Image processing

## How to Run:

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the project
```bash
python OMR_main.py
```

- If `webCamFeed = False` in the code, it will use `3.png` from `test_images/`
- You'll be prompted for a Student ID — this gets saved with the score.

### 3. View stored results
```bash
python view_results.py
```

---

## Features:
- Real-time or image-based OMR grading
- Auto-detects answers
- Calculates score
- Saves results to SQLite with timestamp
- View past scans with `view_results.py`

---

## Sample Input/Output:
- Sample image: `3.png`
- Output: Printed grade + marked answers + stored in DB
