import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. قراءة الصورة
image = cv2.imread('test_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. التنعيم (Gaussian Blur)
blurred_image = cv2.GaussianBlur(gray_image, (15, 15), 0)

# 3. المقص الذكي (Thresholding) - دي اللي هنعرضها في الخطوة التانية
thresholded_image = cv2.adaptiveThreshold(
    blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)

# 4. اللحاام (Morphology) - خطوة مخفية من ورا الكواليس
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
closed_edges = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, kernel)

# 5. عمل القناع (Mask) - دي اللي هنعرضها في الخطوة التالتة
contours, _ = cv2.findContours(closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)

mask = np.zeros_like(gray_image)
cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

# 6. استخراج الليرة الحقيقية
extracted_coin = cv2.bitwise_and(gray_image, gray_image, mask=mask)

# 7. حساب نسبة الخطأ (MSE) للتقرير
mse_value = np.mean((gray_image.astype("float") - blurred_image.astype("float")) ** 2)
print(f"=== MSE Value for Report: {mse_value:.2f} ===")

# ----------------- العرض الاحترافي بعد التعديل -----------------
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('1. Original Image')
plt.axis('off')

# عرضنا الحواف الرفيعة الجميلة بدل العك بتاع Morphology
plt.subplot(2, 2, 2)
plt.imshow(thresholded_image, cmap='gray')
plt.title('2. Detected Edges (Threshold)')
plt.axis('off')

# عرضنا القناع الأبيض السليم
plt.subplot(2, 2, 3)
plt.imshow(mask, cmap='gray')
plt.title('3. Solid Mask (Morphology)')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(extracted_coin, cmap='gray')
plt.title('4. Final Extracted Coin!')
plt.axis('off')

plt.tight_layout()
plt.savefig('result_image.png') # السطر اللي ضفناه عشان يحفظ الصورة لوحده
plt.show()