import cv2
import matplotlib.pyplot as plt

image = cv2.imread('test_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# التنعيم واكتشاف الحواف
blur = cv2.GaussianBlur(gray, (15, 15), 0)
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)

# عرض النتيجة (الحواف)
plt.figure(figsize=(6, 6))
plt.imshow(thresh, cmap='gray')
plt.title('2. Detected Edges')
plt.axis('off')
plt.show()