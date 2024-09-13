import cv2
import socket

# 设置主机连接
SERVER_HOST = '192.168.171.224'  # 服务器的 IP 地址
SERVER_PORT = 65432  # 与服务器端相同的端口号

# 要保存的图片文件路径
image_path = "/home/pi/Desktop/110進/2024Project/Images/captured_image.jpg"

# 初始化摄像头
cap = cv2.VideoCapture(0)  # 0 代表默认摄像头

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

print("请输入 'l' 来捕捉图像并发送")

while True:
    command = input()
    if command.lower() == "l":
        # 捕捉图像
        ret, frame = cap.read()
        if not ret:
            print("无法读取图像")
            continue

        # 保存图像到指定路径
        cv2.imwrite(image_path, frame)
        print(f"图像已保存到 {image_path}")

        # 建立 socket 连接并发送图像
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # 连接到服务器
            s.connect((SERVER_HOST, SERVER_PORT))

            # 读取图片文件的二进制数据
            with open(image_path, 'rb') as f:
                file_data = f.read()

            # 发送图片文件数据
            s.sendall(file_data)

            print(f'图片文件 {image_path} 已发送到 {SERVER_HOST}:{SERVER_PORT}')

    elif command.lower() == "退出":
        break

# 释放摄像头
cap.release()
cv2.destroyAllWindows()

