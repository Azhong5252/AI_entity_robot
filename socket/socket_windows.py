import socket

# 設定主機連線
HOST = '0.0.0.0'  # 0.0.0.0 可以接受任何連線
PORT = 65432

# 從 window 接受到的圖片檔要存放的位置
file_path = "/Users/User/Desktop/2024Project/Images/"

# 圖片檔名動態規劃
image_num = 1

# 建立 socket 连接
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 固定設定的主機和 port
    s.bind((HOST, PORT))

    while True:
        # 開始監聽是否有連接上
        s.listen()
        print("等待連接...")
        conn, addr = s.accept()

        with conn:
            # window 的 IP
            print('已連接到', addr)
            # 接收圖片檔的二進制,直到圖片檔的全部數據都接收到才會終止
            file_data = b''  # 儲存 window 端圖片檔的二進制
            while True:
                data = conn.recv(1024)  # 每次最多接收 1KB 的數據
                if not data:
                    break  # 接收完毕
                file_data += data  # 將收到的 1KB 數據加到用來儲存二進制的變數裡

            # 動態圖片位址
            path = file_path + str(image_num) + ".jpg"  # 假設圖片是 JPG 格式

            # 將剛剛所儲存圖片檔二進制的變數裡的資料存到要存的位置
            with open(path, 'wb') as f:
                f.write(file_data)

            image_num += 1
            print('已把圖片存到該存放的位置', file_path)
