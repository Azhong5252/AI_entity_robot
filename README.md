# AI_entity_robot
根據生成式AI生成實體機器人所需的動作，並且可以訓練微調一個聲音克隆模型，讓機器人可以發出克隆的聲音的與我們對話。
#
請先安裝Anaconda https://www.anaconda.com/download

#Anaconda有裝且路徑都有設定就可跳過這步
#
如果有外顯卡但是沒有cuda要先裝cuda https://developer.nvidia.com/cuda-downloads

#cuda有裝且路徑都有設定就可跳過這步
#
專案克隆
```
git clone https://github.com/Azhong5252/AI_entity_robot.git && cd AI_entity_robot
```
#
訓練VITS-fast-fine-tuning models  
詳情參閱[Local.md](https://github.com/Azhong5252/AI_entity_robot/blob/main/Local.md)  
#
#
訓練GPT-SoVITS models

1.下載\解壓 需要使用的模型到指定位置

#先使用curl下載models到指定位置，然後再使用tar解壓到指定位置
```
curl -L -o GPT-SoVITS-main\uvr5.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_uvr5/uvr5.zip
curl -L -o GPT-SoVITS-main\pretrained_models.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_pretrained_models/pretrained_models.zip
curl -L -o GPT-SoVITS-main\models.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_ASR_model/models.zip
tar -xf "GPT-SoVITS-main\uvr5.zip" -C "GPT-SoVITS-main\tools\uvr5\uvr5_weights"
tar -xf "GPT-SoVITS-main\pretrained_models.zip" -C "GPT-SoVITS-main\GPT_SoVITS"
tar -xf "GPT-SoVITS-main\models.zip" -C "GPT-SoVITS-main\tools\asr"
```
2.train

3.train

4.train

5.train

#若是不想訓練modles

可以到https://huggingface.co/Azhong5252/SoVITS_Ayaka_models 

把(Ayaka_test_models.zip或Azhong_sovits_models.zip)下載下來後，解壓縮在../AI_entity_robot/GPT-SoVITS-main資料夾裡

#
開始功能
#
第一步開啟cmd
```
cd /d %cd%

cd /d "VITS-fast-fine-tuning-webui-v1.1"
if not exist Audio mkdir Audio
cd ..

cd /d "GPT-SoVITS-main"
if not exist Audio mkdir Audio
cd ..

```
#
第二步創建虛擬環境
```
conda create -n project_2024 python==3.9 --yes
```
#
第三步啟動虛擬環境且安裝套件

#啟動虛擬環境
```
conda activate project_2024
```
#安裝ffmpeg套件
```
conda install -y ffmpeg
```
#安裝所需套件
```
pip install -r requirements.txt
```
#安裝Pytorch
```
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118
```
#
#
#需要離開虛擬環境的話
```
conda deactivate
```
#需要刪除這個專案的虛擬環境的話
```
conda remove -n project_2024 --all --yes
```
#
#
第五步執行

#執行前先確認..\AI_entity_robot\Chatgpt.py的apikey有key
```
python.exe main.py
```
#
請先安裝Anaconda和cuda後依照一鍵啟動包0~4即可完成本專案
溫馨提示!當在terminal要執行.bat可以用tab，例如要執行 3啟動虛擬環境(未安裝套件).bat，可以打個 3啟動 然後按tab找到那個.bat檔
#
#
參考文獻  
  特別感謝以下項目和貢獻者：  
  [VITS-fast-fine-tuning](https://github.com/Plachtaa/VITS-fast-fine-tuning/blob/main/LOCAL.md)  
  [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS?tab=readme-ov-file)  
#
