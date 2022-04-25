import numpy as np
import os
import cv2 as cv
import tkinter.filedialog

pose_name = input("请输入姿势名称：")

if not os.path.exists('fitness_poses_images_in'):
    os.makedirs('fitness_poses_images_in')
if not os.path.exists(f'./fitness_poses_images_in/{pose_name}'):
    os.makedirs(f'./fitness_poses_images_in/{pose_name}')

Sample_interval = int(input("请输入采样间隔（每隔多少帧采样一次）"))
videoPath = tkinter.filedialog.askopenfilename(title='选择输入视频文件', filetypes=[('所有文件','.*'),('视频文件','.mp4')])
print("视频路径为："+ videoPath)
fileName = os.path.basename(videoPath)
cap = cv.VideoCapture(videoPath)
i = 0   #用来计数的循环

while cap.isOpened():
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', frame)

    if(i%Sample_interval==0):   #每隔若干帧保存一次图片
        cv.imwrite(f'./fitness_poses_images_in/{pose_name}/{pose_name}_{fileName}_{i}th_frame.jpg',frame)
        cv.imshow('saved', frame)
    i+=1;
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()