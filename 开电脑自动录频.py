import cv2
import os
import time

# 设置摄像头参数和保存路径
save_path = 'D:/cyz'
os.makedirs(save_path, exist_ok=True)
frame_width, frame_height = 640, 480  # 默认分辨率

def create_video_writer():
    timestamp = int(time.time())
    video_file = os.path.join(save_path, f'output_{timestamp}.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    return cv2.VideoWriter(video_file, fourcc, 20.0, (frame_width, frame_height)), video_file

# 初始化摄像头
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建视频写入对象
out, current_file = create_video_writer()
print(f"录制开始... 视频保存到: {current_file}")

start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)

    if time.time() - start_time >= 60:  # 1分钟后停止录制
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
print("录制结束")
