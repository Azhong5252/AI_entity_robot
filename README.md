# AI_entity_robot
根據生成式AI生成實體機器人所需的動作，並且可以利用聲音複製的與我們對話。
#
選擇檔案dowload下來後，從兩種語音克隆選擇一種，然後根據條件把需要的資料補齊
1.VITS-fast-fine-tuning

2.GPT-SoVITS
#
1.VITS-fast-fine-tuning語音克隆

把訓練好的G_latest.pth跟finetune_speaker.json放入AI_entity_robot\VITS-fast-fine-tuning-webui-v1.1裡

最後打開Chatgpt.py把自己的apikey加進去client = OpenAI(api_key = "")
#
2.GPT-SoVITS

把Download下來的pretrained_models資料夾放入AI_entity_robot\GPT-SoVITS-main資料夾裡

然後在AI_entity_robot\GPT-SoVITS-main資料夾裡找到pre_Audio_path.txt打開輸入要克隆的聲音檔的的路徑例如C:\Users\user\Desktop\Audio

最後打開Chatgpt.py把自己的apikey加進去client = OpenAI(api_key = "")
#
開始功能

第一步執行vscode.bat
#執行完後在terminal(ctrl + j)打上cmd

第二步執行create_env.bat(創建虛擬環境)

第三步執行activate.bat(進到虛擬環境)
#要離開虛擬環境可以執行deactivate.bat

#
安裝torch

輸入指令nvidia-smi查詢自己的cuda，例如CUDA Version: 12.4，那麼可以執行以下指令

pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu124
#

第四步執行python_ext.bat(執行main.py)

#
溫馨提示!當在terminal要執行.bat可以用tab，例如要執行create_env.bat，可以打個c然後按tab找到那個.bat檔