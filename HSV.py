import numpy as np
import cv2

# Create a 100x100 image filled with red in HSV
hsv_red = np.full((100, 100, 3), (0, 255, 255), dtype=np.uint8)  # Hue=0, Saturation=255, Value=255

# Convert HSV to BGR so we can display it
bgr_red = cv2.cvtColor(hsv_red, cv2.COLOR_HSV2BGR)

cv2.imshow("Red in HSV", bgr_red)

cv2.waitKey(0)
cv2.destroyAllWindows()
