import cv2
import numpy as np
from utils import *
from db_utils import init_db, store_result

# === CONFIGURABLE SECTION ===
QUESTIONS = 5
CHOICES = 5
CORRECT_ANSWERS = [1, 2, 0, 1, 4]  # Correct answer indices

def main():
    # Initialize DB
    init_db()

    # Get student ID
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty!")
        return

    # Load and process image
    pathImage = "1.jpg"
    img = cv2.imread(pathImage)
    img = cv2.resize(img, (700, 700))
    imgContours = img.copy()
    imgBiggestContours = img.copy()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 10, 50)

    # Find contours
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)

    rectCon = rectContour(contours)
    if len(rectCon) == 0:
        print("No rectangle contours found.")
        return

    biggestContour = getCornerPoints(rectCon[0])
    if biggestContour.size != 4:
        print("Could not detect 4 corners.")
        return

    biggestContour = reorder(biggestContour)
    cv2.drawContours(imgBiggestContours, [biggestContour], -1, (0, 255, 0), 20)

    pts1 = np.float32(biggestContour)
    pts2 = np.float32([[0, 0], [QUESTIONS * 100, 0], [0, CHOICES * 100], [QUESTIONS * 100, CHOICES * 100]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarpColored = cv2.warpPerspective(img, matrix, (QUESTIONS * 100, CHOICES * 100))

    # Thresholding
    imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
    imgThresh = cv2.threshold(imgWarpGray, 150, 255, cv2.THRESH_BINARY_INV)[1]

    boxes = splitBoxes(imgThresh)

    # Count non-zero pixels in each box
    pixelVal = np.zeros((QUESTIONS, CHOICES))
    for i in range(QUESTIONS * CHOICES):
        totalPixels = cv2.countNonZero(boxes[i])
        row = i // CHOICES
        col = i % CHOICES
        pixelVal[row][col] = totalPixels

    # Determine answers
    myIndex = [np.argmax(row) for row in pixelVal]

    # Grade answers
    grading = [1 if myIndex[i] == CORRECT_ANSWERS[i] else 0 for i in range(QUESTIONS)]
    score = grading.count(1) * (100 // QUESTIONS)

    print(f"Answers marked: {myIndex}")
    print(f"Score: {score}%")

    # Store in DB
    store_result(student_id, myIndex, CORRECT_ANSWERS, score)

    # Show result image
    imgResult = imgWarpColored.copy()
    imgResult = showAnswers(imgResult, myIndex, grading, CORRECT_ANSWERS, QUESTIONS, CHOICES)
    imgResult = drawGrid(imgResult, QUESTIONS, CHOICES)

    cv2.imshow("OMR Result", imgResult)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
