# 2DHomography_hw
develop ORB + RANSAC + homography algorithm to create a panorama image from the two inputs.
<br/><br/>
## 연구 목표
ORB와 RANSAC을 사용하여 2D homography computation을 진행시켜보자.<br/>
이후 두 이미지를 올바르게 stitching 하는 것이 최종 연구 목표이다.<br/>
<br/><br/>
## 개발 기간
2023.10.23 ~ 2023.10.26 <br/>
<br/><br/>
## 알고리즘
1. ORB, BRIEF : image1 과 image2 의 key point 와 discriptor를 뽑는다.<br/>
2. BFMatcher(Brute-Force Matcher) : image1과 image2의 key point를 matching해준다. with Hamming distance<br/>
3. find Homography with RANSAC algorithm : 2번의 결과를 사용하여 homography matrix와 mask를 구한다.<br/>
4. choose best matching : 2번에서 얻은 모든 matching 에 대해서 3번의 mask를 적용하여 좋은 matching 만을 뽑아낸다.<br/>
5. stitching two images : image1 과 image2를 이어 붙인다.
<br/><br/>
## 실험 방법
1. main.py과 같은 디렉토리에 존재하는 test3_1.jpg,test3_2.jpg, test5_1.jpg,test5_2.jpg, test6_1.jpg,test6_2.jpg 을 중 한쌍을 input값으로 설정한다. <br/>
ex) image_1 = 'test5_1.jpg' ; image_2 = 'test5_2.jpg'


    <img src="https://github.com/parking-been/2DHomography_hw/assets/138093566/57794094-8faa-4590-8f83-0de1b4134c62" width="400" height="200"/>  <img src="https://github.com/parking-been/2DHomography_hw/assets/138093566/a50ee246-9a0e-4dfc-ad43-5b28178eddf9" width="400" height="200"/>
<br/>
    test6_1.jpg, test6_2.jpg
<br/><br/>
3. 이후 main.py 코드를 돌린 후, main.py 와 같은 디렉토리에 result.jpg, result2.jpg, result3.jpg 이라는 결과 이미지가 나올 것이다.<br/>
   ex) result.jpg : image1 과 image2의 matching result 를 시각화하여 보여준다.<br/>
       result2.jpg : result.jpg의 matching 중 better matching result 만을 선별하여 보여준다.<br/>
       result3.jpg : image1 과 image2의 stitching 한 이미지를 보여준다. <br/>
