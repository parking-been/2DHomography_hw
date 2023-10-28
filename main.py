import cv2
import numpy as np

img_1 = cv2.imread('test6_1.jpg')
img_2 = cv2.imread('test6_2.jpg')
#이미지를 흑백으로 변환 
gray_1 = cv2.cvtColor( img_1 , cv2.COLOR_BGR2GRAY )
gray_2 = cv2.cvtColor( img_2 , cv2.COLOR_BGR2GRAY )

#ORB 추출기 생성
orb = cv2.ORB_create()
# keypoint 와 descriptor 생성
keyp_1 , descrip_1 = orb.detectAndCompute(gray_1,None)
keyp_2 , descrip_2 = orb.detectAndCompute(gray_2,None)

#BFMatcher로 point 이어주기. with Hamming distance 
bfmatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#knn match로 확실한 포인트들만 추출하도록 설계 :
# knn match 대신 homography의 mask 사용해보자 어차피 Ransac이기 때문에..!?
matching = bfmatcher.match(descrip_1,descrip_2)

# 두 matching distance 비율이 0.75이하인 것만 추출한다. 
'''
ratio_test = 0.75

best_matches = []

for m1, m2 in matching:
    if m1.distance < 0.75 * m2.distance:
        best_matches.append([m1])

#for debugging (나중에 delete 할 것)
print('matches: %d %d'%(len(best_matches),len(matching)))
print(type(best_matches))
'''
start_points = np.float32([keyp_1[x.queryIdx].pt for x in matching])
end_points = np.float32([keyp_2[x.trainIdx].pt for x in matching])

#find homography using RANSAC with threshold : 5.0
# 5.0 은 RANSAC에서 사용될 threshold
matrixH, maskH = cv2. findHomography(start_points, end_points, cv2.RANSAC, 5.0)
H, W = img_1.shape[:2]
img_1_points = np.float32([ [[0,0]],[[0, H-1]],[[W-1, H-1]],[[W-1, 0]] ])

print('matrixH.shape: ', matrixH.shape) #3x3
print('start_points.shape: ', start_points.shape) #171x2
print('img_1_points.shape: ', img_1_points.shape) 

dst_points = cv2.perspectiveTransform(img_1_points,matrixH)
#new_img2 = cv2.polylines(img_2, [np.int32(dst_points)], True, 255, 3, cv2.LINE_AA)

#maskH에서 남은 괜찮은 matching만 남긴다. 
best_matching = maskH.ravel().tolist()



#draw result with best_matches
img_r= cv2.drawMatches(img_1, keyp_1, img_2, keyp_2, matching, None)
img_r2 = cv2.drawMatches(img_1, keyp_1, img_2, keyp_2, matching, None, matchesMask=best_matching)

# warp two images to the panorama image using the homography matrix 
#image 2를 이동시키고 image 1을 상대적으로 이동시키지 말아보자

H_2, W_2 = img_2.shape[:2]
H_1, W_1 = img_1.shape[:2]
edge_pts1 = np.float32([[0,0], [0,H_2],[W_2,H_2],[W_2,0]]).reshape(-1,1,2)
edge_pts2 = np.float32([[0,0], [0,H_1],[W_1,H_1],[W_1,0]]).reshape(-1,1,2)
edge_pts2_ = cv2.perspectiveTransform(edge_pts2, matrixH)
edge_pts = np.concatenate((edge_pts1, edge_pts2_), axis = 0)

#파노라마 된 그림의 크기를 찾기 위해 
[min_x, min_y] = np.int32(edge_pts.min(axis=0).ravel()) #- 0.5
[max_x, max_y] = np.int32(edge_pts.max(axis=0).ravel()) # + 0.5
t_p = [-min_x, -min_y]

matrixT = np.array([[1,0,t_p[0]], [0,1,t_p[1]], [0,0,1]])
result3 = cv2.warpPerspective(img_1,matrixT.dot(matrixH), (max_x-min_x, max_y-min_y))
result3[t_p[1]:t_p[1]+H_2, t_p[0]:t_p[0]+W_2] = img_2

cv2.imwrite('result3.jpg', result3)

cv2.imwrite('result.jpg', img_r)
cv2.imwrite('result2.jpg', img_r2)
cv2.waitKey(0)
cv2.destroyAllWindows()

