# Automated Coin Detection and Extraction

Image Processing and Lab (LEEN350) project using Python and OpenCV to isolate a coin from a textured background.

## Processing pipeline

1. Convert the input image to grayscale.
2. Apply Gaussian blur to smooth fine texture.
3. Apply adaptive Gaussian thresholding.
4. Use morphological closing and select the largest external contour.
5. Fill a mask and extract the coin using a bitwise operation.
6. Display and save the four-stage result.

## Requirements

Python 3.13 was used for the original project. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

Run the commands from the project folder (where `test_image.jpg` is located):

```bash
python main.py
```

The main script shows the four output stages, writes `result_image.png`, and prints the grayscale-vs-blurred MSE. Individual stage demos are `step1_original.py`, `step2_edges.py`, `step3_mask.py`, and `step4_extraction.py`.

To regenerate the included PDF report:

```bash
python generate_pdf.py
```

## Notes

The MSE calculated by the original script compares the grayscale image and its blurred version. It measures their difference, not segmentation accuracy or detection precision. The code selects the largest contour, so results may depend on the input image and lighting.

## Project files

- `main.py`: complete pipeline
- `step1_original.py` through `step4_extraction.py`: stage demos
- `generate_pdf.py`: report generator
- `test_image.jpg`: input image
- `result_image.png`: saved result
- `Final_Report_Official.pdf`: project report
