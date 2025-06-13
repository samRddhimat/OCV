import cv2
import sys

print("Hello, OpenCV!, Welcome","^")

print("$$$"*5)

print(cv2.__version__)

img = cv2.imread("VPN-config.PNG")

cv2.imshow("vpn settings",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(sys.executable)
