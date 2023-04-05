# from clipcrop import clipcrop
# import cv2 as cv
# image=cv.imread("nm.png")
# image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
# clipseg = clipcrop.ClipSeg("image", "black colored car")
# segmentor, clipmodel, clipprocessor = clipseg.load_models()
# result = clipseg.segment_image(segmentor, clipmodel, clipprocessor)

import cv2

# 이미지 로드
image = cv2.imread('fov.png')

# 이미지 전처리
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)

# 차량 표시판 검출
contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
        roi = image[y:y+h, x:x+w]  # 차량 표시판 ROI 추출

# 결과 이미지 출력
cv2.imshow('result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
