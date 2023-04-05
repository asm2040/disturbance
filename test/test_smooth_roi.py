import cv2
import numpy as np

# 시작점, 제어점1, 제어점2, 끝점
pts = np.array([[20, 30], [60, 20], [90, 120], [30, 110]])

# 3차 베지어 곡선 그리기
curve = np.array([pts], dtype=np.int32)
img = np.zeros((150, 150, 3), np.uint8)
cv2.polylines(img, curve, False, (255, 255, 255), 2)

# 결과 출력
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
