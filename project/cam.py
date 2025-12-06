import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open webcam")
        return

    sigma = 1.0           # initial smoothing parameter
    current_mode = 'o'     # default mode = original

    print("Controls:")
    print("  o = Original frame")
    print("  x = Sobel in X direction")
    print("  y = Sobel in Y direction")
    print("  m = Sobel magnitude")
    print("  s = Sobel + thresholding")
    print("  l = Laplacian of Gaussian (LoG)")
    print("  + = Increase sigma")
    print("  - = Decrease sigma")
    print("  q = Quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame!")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Determine kernel size from sigma (OpenCV requires odd integer)
        ksize = int(2 * (3 * sigma) + 1)
        if ksize % 2 == 0:
            ksize += 1

        # Gaussian blur
        blurred = cv2.GaussianBlur(gray, (ksize, ksize), sigma)

        # Compute derivatives (only when needed)
        if current_mode in ['x', 'y', 'm', 's']:
            sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

        # Display based on current mode
        if current_mode == 'o':
            display = frame

        elif current_mode == 'x':
            display = cv2.convertScaleAbs(sobel_x)

        elif current_mode == 'y':
            display = cv2.convertScaleAbs(sobel_y)

        elif current_mode == 'm':
            magnitude = cv2.magnitude(sobel_x, sobel_y)
            display = cv2.convertScaleAbs(magnitude)


        elif current_mode == 's':
            magnitude = cv2.magnitude(sobel_x, sobel_y)
            mag_img = cv2.convertScaleAbs(magnitude)
            threshold_value = np.mean(mag_img)
            _, thresh = cv2.threshold(mag_img, threshold_value, 255, cv2.THRESH_BINARY)
            display = thresh

        elif current_mode == 'l':
            # Laplacian of Gaussian = blur → Laplacian
            log = cv2.Laplacian(blurred, cv2.CV_64F)
            display = cv2.convertScaleAbs(log)

        else:
            display = frame

        # Show result
        cv2.imshow("Output", display)

        # Keyboard input
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('+'):
            sigma += 0.5
            print(f"Sigma increased to {sigma}")
        elif key == ord('-'):
            sigma = max(0.5, sigma - 0.5)
            print(f"Sigma decreased to {sigma}")
        else:
            if chr(key) in ['o', 'x', 'y', 'm', 's', 'l']:
                current_mode = chr(key)
                print(f"Mode changed to {current_mode}")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
