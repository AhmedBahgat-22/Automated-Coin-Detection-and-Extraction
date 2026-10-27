import os
import matplotlib.pyplot as plt
from fpdf import FPDF

print("========================================")
# تحديد مسار الفولدر اللي فيه الكود عشان PyCharm ميضيعش الملفات
current_folder = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_folder, 'arel_logo.jpeg')
result_path = os.path.join(current_folder, 'result_image.png')

print("جاري رسم المعادلات وتجهيز التقرير النهائي...")

# 1. رسم المعادلات الرياضية كصور عالية الجودة لتفادي مشاكل الفونت
def save_equation(formula, filename):
    filepath = os.path.join(current_folder, filename)
    fig = plt.figure(figsize=(6, 0.6))
    fig.text(0.01, 0.5, f'${formula}$', fontsize=14, va='center')
    plt.axis('off')
    plt.savefig(filepath, bbox_inches='tight', pad_inches=0.01, dpi=300)
    plt.close(fig)

save_equation(r'Y = 0.299R + 0.587G + 0.114B', 'eq1.png')
save_equation(r'G(x,y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}}', 'eq2.png')
save_equation(r'A \bullet B = (A \oplus B) \ominus B', 'eq3.png')
save_equation(r'MSE = \frac{1}{MN} \sum_{i=0}^{M-1} \sum_{j=0}^{N-1} [I_1(i,j) - I_2(i,j)]^2', 'eq4.png')

# 2. بناء كلاس الـ PDF بالشروط: خط Times، مسافة 1.5، وترقيم الصفحات
class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 10)
        self.cell(0, 10, f'{self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(3)

    def chapter_body(self, text):
        self.set_font('Times', '', 12)
        # مسافة 1.5 تساوي تقريباً h=8
        self.multi_cell(0, 8, text)
        self.ln(5)

pdf = PDF()
pdf.set_margins(25, 25, 25)

# =========================================================
# Page 1: COVER PAGE (الغلاف فقط)
# =========================================================
pdf.add_page()
if os.path.exists(logo_path):
    pdf.image(logo_path, x=85, y=30, w=40)
    pdf.ln(60)
    print("✅ تم العثور على لوجو الجامعة بنجاح.")
else:
    pdf.ln(40)
    print("❌ تنبيه: لم يتم العثور على صورة arel_logo.jpeg في الفولدر.")

pdf.set_font('Times', 'B', 14)
pdf.cell(0, 10, 'ISTANBUL AREL UNIVERSITY', 0, 1, 'C')
pdf.cell(0, 10, 'FACULTY OF ENGINEERING', 0, 1, 'C')
pdf.cell(0, 10, 'LEEN350 - IMAGE PROCESSING AND LAB', 0, 1, 'C')
pdf.ln(15)

pdf.set_font('Times', 'B', 16)
pdf.cell(0, 10, 'PROJECT REPORT', 0, 1, 'C')
pdf.ln(15)

pdf.set_font('Times', 'B', 12)
pdf.cell(50, 10, 'Project Title:', 0, 0)
pdf.set_font('Times', '', 12)
pdf.cell(0, 10, 'Automated Coin Detection and Extraction', 0, 1)

pdf.set_font('Times', 'B', 12)
pdf.cell(50, 10, 'Student Name:', 0, 0)
pdf.set_font('Times', '', 12)
pdf.cell(0, 10, 'Ahmed Mahmoud Bahagat Abdelmoula', 0, 1)

pdf.set_font('Times', 'B', 12)
pdf.cell(50, 10, 'Student ID:', 0, 0)
pdf.set_font('Times', '', 12)
pdf.cell(0, 10, '220303923', 0, 1)

pdf.set_font('Times', 'B', 12)
pdf.cell(50, 10, 'Presentation Week:', 0, 0)
pdf.set_font('Times', '', 12)
pdf.cell(0, 10, 'Week 6', 0, 1)

# =========================================================
# Page 2: INTRODUCTION
# =========================================================
pdf.add_page()
pdf.chapter_title('1. INTRODUCTION')
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 8, 'Objective:', 0, 1)
pdf.chapter_body('The primary objective of this project is to develop an automated image processing pipeline capable of robustly segmenting and extracting a specific object (a coin) from a highly textured background (a wooden table) under uneven illumination conditions.')
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 8, 'Motivation:', 0, 1)
pdf.chapter_body('In real-world computer vision systems, uniform lighting is rarely guaranteed. Traditional global thresholding methods fail when shadows or uneven lighting are present. Solving this problem is critical for automated systems such as industrial quality inspection, currency recognition sorting machines, and autonomous robotic picking.')

# =========================================================
# Page 3: THEORETICAL BACKGROUND
# =========================================================
pdf.add_page()
pdf.chapter_title('2. THEORETICAL BACKGROUND')
pdf.chapter_body('The pipeline relies on several fundamental image processing theories. All mathematical representations are numbered as per the requirements.')

pdf.set_font('Times', 'B', 12)
pdf.cell(0, 8, 'Image Representation (Grayscale):', 0, 1)
pdf.chapter_body('Converting the RGB color model to grayscale reduces computational complexity. It is calculated using the weighted sum of the color channels as shown in Equation 1.')
pdf.image(os.path.join(current_folder, 'eq1.png'), x=25, h=6)
pdf.set_font('Times', 'I', 12)
pdf.cell(0, 8, '(Eq. 1)', 0, 1, 'R')
pdf.ln(5)

pdf.set_font('Times', 'B', 12)
pdf.cell(0, 8, 'Gaussian Filter (Smoothing):', 0, 1)
pdf.chapter_body('Used to reduce high-frequency noise and background textures. It convolves the image with a 2D Gaussian kernel (Equation 2).')
pdf.image(os.path.join(current_folder, 'eq2.png'), x=25, h=10)
pdf.set_font('Times', 'I', 12)
pdf.cell(0, 8, '(Eq. 2)', 0, 1, 'R')
pdf.ln(5)

pdf.set_font('Times', 'B', 12)
pdf.cell(0, 8, 'Morphological Operations (Closing):', 0, 1)
pdf.chapter_body('A morphological closing operation consists of a dilation followed by an erosion (Equation 3). This is used to close small holes inside the foreground object.')
pdf.image(os.path.join(current_folder, 'eq3.png'), x=25, h=6)
pdf.set_font('Times', 'I', 12)
pdf.cell(0, 8, '(Eq. 3)', 0, 1, 'R')
pdf.ln(5)

pdf.set_font('Times', 'B', 12)
pdf.cell(0, 8, 'Performance Metrics (MSE):', 0, 1)
pdf.chapter_body('Mean Squared Error is used to measure the difference between the original grayscale image and the smoothed image, quantifying the noise removed (Equation 4).')
pdf.image(os.path.join(current_folder, 'eq4.png'), x=25, h=12)
pdf.set_font('Times', 'I', 12)
pdf.cell(0, 8, '(Eq. 4)', 0, 1, 'R')

# =========================================================
# Page 4: SYSTEM PIPELINE & METHODOLOGY
# =========================================================
pdf.add_page()
pdf.chapter_title('3. SYSTEM / PROCESSING PIPELINE DESCRIPTION')
pdf.chapter_body('The processing pipeline is executed in the following sequential order (Figure 1).')
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 8, 'Figure 1: System Pipeline Block Diagram', 0, 1, 'C')
pdf.set_font('Times', '', 12)
pdf.cell(0, 8, 'Image -> Grayscale -> Gaussian Blur -> Adaptive Thresholding -> Morphology -> Extraction', 0, 1, 'C')
pdf.ln(5)
pdf.chapter_body('Each stage is designed to specifically handle the texture of the wooden background and the shadows cast by the coin.')

pdf.chapter_title('4. METHODOLOGY')
pdf.chapter_body('- Dataset used: A custom captured image (test_image.jpg) featuring a shiny coin placed on a textured wooden table.\n- Preprocessing steps: Color-to-grayscale conversion to reduce data dimensions.\n- Filtering methods: A Gaussian Blur filter was applied to eliminate the fine details of the wood grain.\n- Segmentation methods: Adaptive Gaussian Thresholding was utilized because the image contains shadows.\n- Morphological operations: A closing operation using an elliptical structuring element was applied.\n- Feature extraction techniques: Contour detection was used to locate the boundary of the object.')
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 8, 'Parameters used:', 0, 1)
pdf.chapter_body('- Gaussian Blur Kernel: (15, 15)\n- Adaptive Threshold Block Size: 21\n- Adaptive Threshold Constant (C): 5\n- Morphological Elliptical Kernel: (25, 25)')

# =========================================================
# Page 5: IMPLEMENTATION
# =========================================================
pdf.add_page()
pdf.chapter_title('5. IMPLEMENTATION')
pdf.chapter_body('- Programming environment: Python\n- Libraries used: OpenCV (cv2) for image processing algorithms, NumPy (np) for matrix operations and MSE calculations, and Matplotlib (plt) for visual plotting.\n- Code structure: The main script reads the image, applies filtering and adaptive thresholding. The contour function finds the maximum connected area, and bitwise operations apply the mask to extract the target.\n- Main processing steps logic: Instead of hard-coding global values, the local adaptive block scans 21x21 pixel regions to dynamically adapt to the lighting conditions.')

# =========================================================
# Page 6: RESULTS AND ANALYSIS
# =========================================================
pdf.add_page()
pdf.chapter_title('6. RESULTS AND ANALYSIS')
pdf.chapter_body('The output of the automated pipeline is presented in Figure 2 below, showing the progression from the original image to the completely extracted object.')

# إضافة الصورة المجمعة
if os.path.exists(result_path):
    pdf.image(result_path, x=20, w=170)
    pdf.ln(5)
    pdf.set_font('Times', 'B', 11)
    pdf.cell(0, 8, 'Figure 2: Four-step Visual Result of the Extraction Pipeline', 0, 1, 'C')
    pdf.ln(5)
    print("✅ تم العثور على صورة النتيجة وإضافتها للتقرير.")
else:
    pdf.set_fill_color(220, 220, 220)
    pdf.cell(0, 30, 'STUDENT NOTE: PLEASE SAVE YOUR IMAGE AS result_image.png', 1, 1, 'C', fill=True)
    pdf.ln(5)
    print("❌ تنبيه: لم يتم العثور على صورة النتيجة result_image.png")

pdf.set_font('Times', 'B', 12)
pdf.cell(0, 8, 'Visual Analysis:', 0, 1)
pdf.chapter_body('1. Original Image: Shows the coin with visible shadows and a distracting wooden background.\n2. Detected Edges: The adaptive threshold successfully isolated the circular shape of the coin.\n3. Solid Mask: By combining morphological closing and contour filling, a flawless white mask was generated.\n4. Final Extracted Coin: The bitwise operation perfectly extracted the coin.')

# =========================================================
# Page 7: Quantitative Analysis & DISCUSSION
# =========================================================
pdf.add_page()
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 8, 'Quantitative Analysis:', 0, 1)
pdf.chapter_body('The calculated MSE (Mean Squared Error) between the grayscale image and the blurred image is 21.10. This indicates that the Gaussian filter successfully removed the background high-frequency noise without destroying the structural integrity of the coin.')

pdf.chapter_title('7. DISCUSSION')
pdf.chapter_body('- Strengths: The pipeline is exceptionally robust to varying illumination. The combination of adaptive thresholding and largest-contour extraction ensures that the coin is found even with shadows.\n- Weaknesses / Limitations: The parameters are hardcoded based on the current distance of the camera. If the camera moves much further away, these kernel sizes might distort the coin.\n- Sensitivity to parameters: Changing the block size from 21 to a lower number causes the shadows to break the contour.\n- Observed trade-offs: Using a large kernel for Gaussian blur effectively erased the wood background but also softened the engraving details inside the coin.')

# =========================================================
# Page 8: CONCLUSION & FUTURE WORK & REFERENCES
# =========================================================
pdf.add_page()
pdf.chapter_title('8. CONCLUSION')
pdf.chapter_body('The project successfully implemented a highly accurate automated extraction pipeline. The combination of Adaptive Gaussian Thresholding and Morphological contour filling proved to be a superior approach compared to global thresholding methods for dealing with uneven lighting and textured backgrounds. The main findings show that local processing outperforms global processing in real-world scenarios.')

pdf.chapter_title('9. FUTURE WORK')
pdf.chapter_body('- Possible improvements: Implementing a dynamic algorithm to automatically calculate kernel sizes based on the image resolution.\n- Alternative methods: Integrating Machine Learning models (like YOLO) for object detection, bypassing manual parameter tuning.\n- Real-world deployment considerations: This pipeline can be optimized in C++ to run in real-time on a fast conveyor belt system for automated coin sorting.')

pdf.chapter_title('10. REFERENCES')
pdf.chapter_body('1. Bradski, G. (2000). The OpenCV Library. Dr. Dobb\'s Journal of Software Tools.\n2. Gonzalez, R. C., & Woods, R. E. (2018). Digital Image Processing (4th ed.). Pearson.\n3. OpenCV Documentation: Adaptive Thresholding and Morphological Transformations.')

# حفظ الملف النهائي
pdf_out = os.path.join(current_folder, 'Final_Report_Official.pdf')
pdf.output(pdf_out)
print(f"========================================")
print(f"✅ تم إنشاء التقرير بنجاح! هتلاقيه في المسار ده:")
print(f"{pdf_out}")
print(f"========================================")