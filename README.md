# 2DHomography_hw
develop ORB + RANSAC + homography algorithm to create a panorama image from the two inputs.

## 연구 목표
ORB와 RANSAC을 사용하여 2D homography computation을 진행시켜보자. 
이후 두 이미지를 올바르게 stitching 하는 것이 최종 연구 목표이다.

## 개발 기간
2023.10.23 ~ 2023.10.26

## 알고리즘
1. ORB, BRIEF : image1 과 image2 의 key point 와 discriptor를 뽑는다.
2. BFMatcher(Brute-Force Matcher) : image1과 image2의 key point를 matching해준다. with Hamming distance
3. find Homography with RANSAC algorithm : 2번의 결과를 사용하여 homography matrix와 mask를 구한다.
4. choose best matching : 2번에서 얻은 모든 matching 에 대해서 3번의 mask를 적용하여 좋은 matching 만을 뽑아낸다.
5. stitching two images : image1 과 image2를 이어 붙인다.

## 실험 방법
1. main.py과 같은 디렉토리에 존재하는 test3_1.jpg,test3_2.jpg, test5_1.jpg,test5_2.jpg, test6_1.jpg,test6_2.jpg 을 중 한쌍을 input값으로 설정한다.
ex) image_1 = 'test5_1.jpg' ; image_2 = 'test5_2.jpg'
2. 이후 main.py 코드를 돌린 후, main.py 와 같은 디렉토리에 result.jpg, result2.jpg, result3.jpg 이라는 결과 이미지가 나올 것이다.
   ex) result.jpg : image1 과 image2의 matching result 를 시각화하여 보여준다.
       result2.jpg : result.jpg의 matching 중 better matching result 만을 선별하여 보여준다.
       result3.jpg : image1 과 image2의 stitching 한 이미지를 보여준다. 
