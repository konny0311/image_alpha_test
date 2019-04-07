import cv2

img = cv2.imread('without.png', cv2.IMREAD_UNCHANGED)
cv2.imwrite('save_without_unchaned.png', img)