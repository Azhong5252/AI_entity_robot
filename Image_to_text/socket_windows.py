# socket_window.py
import socket
import sys
import signal
import os
import time

def send_image():
    HOST = '0.0.0.0'
    PORT = 65432
    file_path = os.getcwd() + "\\image\\"
    check = True

    def signal_handler(sig, frame):
        print('中斷信號捕捉到，正在退出...')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5.0)
        s.bind((HOST, PORT))
        while check:
            try:
                s.listen()
                print("等待連接...")
                conn, addr = s.accept()

                with conn:
                    check = False
                    print('已連接到', addr)
                    file_data = b''
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        file_data += data

                    path = os.path.join(file_path, time.strftime("%Y%m%d%H%M%S") + ".jpg")

                    with open(path, 'wb') as f:
                        f.write(file_data)
                    print('已把圖片存到該存放的位置', file_path)

            except socket.timeout:
                print("等待連接超時，繼續監聽...")
            except Exception as e:
                print(f"發生錯誤: {e}")