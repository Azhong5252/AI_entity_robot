import chatgpt_img
import socket_windows
import time
while True:
    socket_windows.send_image()
    reply = chatgpt_img.img_to_text()
    print(reply)    