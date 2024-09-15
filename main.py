import Chatgpt
import Mqtt_receive_message
from playsound import playsound
import os
import sys
sys.path.append(r'C:\Users\user\Desktop\2024Graduate_Topie\Project_data\ALL_action\VITS-fast-fine-tuning-webui-v1.1')
import Vits

mqttmsg = Mqtt_receive_message.Mqtt_receive() #重mqtt獲得訊息 
print(mqttmsg)

result = Chatgpt.gpt(mqttmsg) #把mqtt獲得得訊息送到gpt生成
print(result)

os.chdir(r'C:\Users\user\Desktop\2024Graduate_Topie\Project_data\ALL_action\VITS-fast-fine-tuning-webui-v1.1')#切換目錄，是用來找到finetune_speaker.json位置
Audio_text,Audio_path = Vits.vits(result) #回傳聲音的文字和音檔的路徑

print("Ayaka:",Audio_text)
playsound(Audio_path)