import cv2
import matplotlib.pyplot as plt

# 1. قراءة الصورة
image = cv2.imread('test_image.jpg')

# 2. تحويلها لرمادي فوراً زي الكود بتاعك
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. عرض الصورة الرمادي
plt.figure(figsize=(6, 6))
plt.imshow(gray_image, cmap='gray')
plt.title('1. Original Image')
plt.axis('off')

print("✅ الخطوة الأولى رجعت رمادي زي ما طلبت!")
plt.show()