# AI_entity_robot
根據生成式AI生成實體機器人所需的動作，並且可以訓練微調一個聲音克隆模型，讓機器人可以發出克隆的聲音的與我們對話。
#
請先安裝Anaconda https://www.anaconda.com/download

#Anaconda有裝且路徑都有設定就可跳過這步
#
如果有外顯卡但是沒有cuda要先裝cuda https://developer.nvidia.com/cuda-downloads

#cuda有裝且路徑都有設定就可跳過這步
#
開始功能
#
第一步開啟cmd
(是否我們自己建Audio資料夾放進github上可以避免這些指令owob)
'''
cd /d %cd%
cd /d "VITS-fast-fine-tuning-webui-v1.1"
mkdir Audio
cd ..
cd /d "GPT-SoVITS-main"
mkdir Audio(是否我們自己建資料夾放進github上)
cmd /k
'''
#
#
第二步創建虛擬環境
'''
conda create -n project_2024 python==3.9 --yes
'''
#
第三步自動下載且解壓模型

#會自動下載pretrained_models.zip和models.zip且會自動解壓縮，需要較久時間下載和解壓縮)
'''
curl -L -o GPT-SoVITS-main\pretrained_models.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_pretrained_models/pretrained_models.zip
curl -L -o GPT-SoVITS-main\models.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_ASR_model/models.zip
tar -xf "GPT-SoVITS-main\pretrained_models.zip" -C "GPT-SoVITS-main\GPT_SoVITS"
tar -xf "GPT-SoVITS-main\models.zip" -C "GPT-SoVITS-main\tools\asr"
'''
#若不要自己訓練GPT-SoVITS模型而想用現成的話，可以等這步下載解壓完後，接著執行test_models.bat(需要較久時間下載和解壓縮)
#
第四步執行 啟動虛擬環境安裝套件
'''
conda activate project_2024
conda install -y ffmpeg
pip install -r requirements.txt
'''
#非第一次創建這個虛擬環境但要直接進入虛擬環境的話 3啟動虛擬環境.bat

#離開虛擬環境
'''
conda deactivate
'''
#要刪除這個虛擬環境的話 999刪除虛擬環境.bat
#
第五步執行
'''
python.exe main.py
'''
#
溫馨提示!當在terminal要執行.bat可以用tab，例如要執行 3啟動虛擬環境(未安裝套件).bat，可以打個 3啟動 然後按tab找到那個.bat檔
