import cv2
import numpy as np

# 고정된 이미지 파일 경로
image_path = 'misson/05.png'

# 이미지 읽기
image = cv2.imread(image_path)

# 이미지가 제대로 불러와졌는지 확인
if image is None:
    print("이미지를 불러올 수 없습니다.")
else:
    # 1. HSV 색 공간으로 변환
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)

    # 2. 채도(Saturation)를 증가시켜 색상을 더욱 생동감 있게
    s = np.clip(s + 30, 0, 255)  # 채도를 20만큼 증가시켜 색감을 더 풍부하게 만듬

    # 3. 수정된 HSV 이미지를 다시 병합하여 BGR로 변환
    hsv_modified = cv2.merge((h, s, v))
    final_image = cv2.cvtColor(hsv_modified, cv2.COLOR_HSV2BGR)

    # 4. 약한 샤프닝 필터 적용 (자연스럽게 최소한만 적용)
    sharpen_kernel = np.array([[0, -0.2, 0],
                               [-0.2, 1.4, -0.2],
                               [0, -0.2, 0]])
    final_image = cv2.filter2D(final_image, -1, sharpen_kernel)

    # 5. 이미지 저장
    output_image_path = 'misson_image05.png'
    cv2.imwrite(output_image_path, final_image)

    # 원본 이미지와 수정된 이미지 나란히 보여주기
    combined_image = np.hstack((image, final_image))

    cv2.imshow('Original Image vs Enhanced Image', combined_image)

    # ESC 키를 눌러 종료
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"이미지가 성공적으로 수정되었습니다: {output_image_path}")