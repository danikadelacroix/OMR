# OMR
This project implements an Optical Mark Recognition (OMR) algorithm in Python using OpenCV. The algorithm is designed to process scanned documents, detect marked bubbles, and analyze the results, making it ideal for applications such as exam grading, surveys, and form analysis.

Features:
Image Preprocessing: Converts input images to grayscale and applies adaptive thresholding to handle varying lighting conditions.
Bubble Detection: Identifies bubbles using contour detection and morphological operations, ensuring robust recognition.
Noise Reduction: Incorporates image cleaning techniques to eliminate artifacts and improve detection accuracy.
Automated Scoring: Analyzes marked bubbles and computes scores for predefined answer keys.
Scalability: Supports real-time processing of multiple sheets with consistent accuracy.

Essential Requirements:
Python 3.7 or higher
OpenCV (cv2)

The scanned sheet is loaded as an image file. The algorithm determines which bubbles are marked based on pixel intensity. Scores or responses are generated based on the analyzed data.
