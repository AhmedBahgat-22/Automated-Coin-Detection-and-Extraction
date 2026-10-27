import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('test_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (15, 15), 0)

thresholded_image = cv2.adaptiveThreshold(
    blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
closed_edges = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, kernel)

# السطور دي هي اللي بتعمل الماسك الأبيض النضيف زي كودك الأصلي
contours, _ = cv2.findContours(closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)

mask = np.zeros_like(gray_image)
cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

plt.figure(figsize=(6, 6))
plt.imshow(mask, cmap='gray')
plt.title('3. Solid Mask (Morphology)')
plt.axis('off')

print("✅ الخطوة التالتة اتحدثت وبقت زي كود الـ Main بالظبط!")
plt.show()