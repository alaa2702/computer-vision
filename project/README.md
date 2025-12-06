# Webcam Edge Detection with OpenCV

This Python project captures live video from your webcam and applies various edge detection and image processing techniques in real-time using **OpenCV** and **NumPy**.

---

## **Features**

* Display the original webcam feed.
* Apply **Sobel edge detection** in X or Y directions.
* Compute **Sobel gradient magnitude**.
* Apply **Sobel + thresholding** for binary edge maps.
* Apply **Laplacian of Gaussian (LoG)** for advanced edge detection.
* Adjust Gaussian **smoothing parameter (`sigma`)** in real-time.

---

## **Requirements**

* Python 3.8+
* OpenCV (`opencv-python`)
* NumPy

Install dependencies via pip:

```bash
pip install opencv-python numpy
```

---

## **Usage**

Run the script:

```bash
python cam.py
```

### **Controls**

| Key | Action                      |
| --- | --------------------------- |
| `o` | Show original frame         |
| `x` | Sobel in X direction        |
| `y` | Sobel in Y direction        |
| `m` | Sobel magnitude             |
| `s` | Sobel + thresholding        |
| `l` | Laplacian of Gaussian (LoG) |
| `+` | Increase Gaussian sigma     |
| `-` | Decrease Gaussian sigma     |
| `q` | Quit the program            |

---

## **How It Works**

1. **Capture frame**: The webcam frame is captured using `cv2.VideoCapture`.
2. **Grayscale conversion**: Convert the frame to grayscale for processing.
3. **Gaussian smoothing**: Apply a Gaussian blur with adjustable `sigma` to reduce noise.
4. **Edge detection**:

   * Sobel operators compute derivatives along X and Y axes.
   * Magnitude combines X and Y gradients.
   * Thresholding highlights strong edges.
   * LoG detects edges after smoothing.
5. **Display**: The processed frame is shown in a window. Keyboard input allows real-time mode and parameter changes.

