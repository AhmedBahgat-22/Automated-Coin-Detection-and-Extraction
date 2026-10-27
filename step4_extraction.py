import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. قراءة الصورة وتحويلها لرمادي
image = cv2.imread('test_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. التنعيم
blurred_image = cv2.GaussianBlur(gray_image, (15, 15), 0)

# 3. المقص الذكي
thresholded_image = cv2.adaptiveThreshold(
    blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)

# 4. اللحام
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
closed_edges = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, kernel)

# 5. عمل القناع (باستخدام أكبر كونتور زي كودك القديم)
contours, _ = cv2.findContours(closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)

mask = np.zeros_like(gray_image)
cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

# 6. استخراج الليرة الحقيقية (من الصورة الرمادي)
extracted_coin = cv2.bitwise_and(gray_image, gray_image, mask=mask)

# ==========================================
# عرض الخطوة الرابعة لوحدها بنفس الستايل القديم
# ==========================================
plt.figure(figsize=(6, 6))
plt.imshow(extracted_coin, cmap='gray')
plt.title('4. Final Extracted Coin!')
plt.axis('off')

print("✅ الخطوة الرابعة اتعملت بالمللي زي الكود القديم بتاعك!")
plt.show()