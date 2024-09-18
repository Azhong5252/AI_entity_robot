from playsound import playsound
import os
import sys
# ====================================================================================================================
import Chatgpt #Chatgpt.py函式引入
import Mqtt_receive_message #Mqtt_receive_message.py函式引入
# ====================================================================================================================
"""
這個是VITS-fast-fine-tuning的函數引入，需要使用就把底下區域程式移動到外圍
vits_path = os.path.join(os.getcwd(), "VITS-fast-fine-tuning-webui-v1.1")
sys.path.append(vits_path)
os.chdir(vits_path)
import Vits
"""
# ====================================================================================================================
"""
這個是GPT-SoVITS的函數引入，需要使用就把底下區域程式移動到外圍
"""
gpt_so_vits_path = os.path.join(os.getcwd(), "GPT-SoVITS-main", "GPT_SoVITS")
os.chdir(os.path.join(os.getcwd(), "GPT-SoVITS-main"))  # 切換到 GPT-SoVITS-main 目錄
sys.path.append(gpt_so_vits_path)  # 將 GPT_SoVITS 目錄添加到模塊搜索路徑
import inference_webui
# ====================================================================================================================
"""
這個是mqtt接收訊息
mqttmsg = Mqtt_receive_message.Mqtt_receive() #重mqtt獲得訊息 ，需要使用就把底下區域程式移動到外圍
print(mqttmsg)
"""
# ====================================================================================================================
"""
這個是gpt文字生成
result = Chatgpt.gpt(mqttmsg) #把mqtt獲得得訊息送到gpt生成，需要使用就把底下區域程式移動到外圍
print(result)
"""
# ====================================================================================================================
"""
這個是VITS-fast-fine-tuning的執行，需要使用就把底下區域程式移動到外圍
Audio_text,Audio_path = Vits.vits("result") #回傳聲音的文字和音檔的路徑
print("Ayaka:",Audio_text)
playsound(Audio_path)
"""
# ====================================================================================================================
"""
這個是GPT-SoVITS的執行，需要使用就把底下區域程式移動到外圍
"""
Audio_text,Audio_path = inference_webui.sovits("你好")
print("Ayaka:",Audio_text)
playsound(Audio_path)
# ====================================================================================================================