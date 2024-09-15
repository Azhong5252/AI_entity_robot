import socket
from playsound import playsound
# 設置Raspberry Pi的IP地址和端口
RASPBERRY_PI_IP = '172.20.10.7'
PORT = 65432

ck = 1
path = "C:\\Users\\User\\Desktop\\2024Graduate_Topie\\VITS-fast-fine-tuning-webui-v1.1\\Audio"
while True:
    if ck <= 1:
        pa = path + str(ck) + ".wav"
        with open(pa, 'rb') as f:
            file_data = f.read()
            print(file_data)
            
        # 建立socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            # 連接到Raspberry pi
            s.connect((RASPBERRY_PI_IP, PORT))
            
            # 發送wav檔二進制資料
            s.sendall(file_data)
            
            print('已發送.wav檔案')
            ck = ck+1
    else:
        break
    
    