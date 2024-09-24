#VITS-fast-fine-tuing環境建設  
0.
　到https://visualstudio.microsoft.com/zh-hant/downloads/ 下載Visual Studio 2022並勾選CMake & C/C++ compilers
1.下載套件
```
  cd VITS-fast-fine-tuing
  pip install -r requirements.txt
```
2.安裝處理影片資料並要的套件
```
  pip install imageio==2.4.1
  pip install moviepy
```
3.建立單調對齊(訓練並要)
```
  cd /monotonic_align
  python setup.py build_ext --inplace
  cd ..
```
4.(下載訓練輔助數據)
```
  mkdir pretrained_models
```
  # download data for fine-tuning
  ```
  wget https://huggingface.co/datasets/Plachta/sampled_audio4ft/resolve/main/sampled_audio4ft_v2.zip
  unzip sampled_audio4ft_v2.zip
```
  # create necessary directories
  ```
  mkdir video_data
  mkdir raw_audio
  mkdir denoised_audio
  mkdir custom_character_voice
  mkdir segmented_character_voice
```
5.下載預訓練
  CJE: Trilingual (Chinese, Japanese, English)
  ```
  https://huggingface.co/spaces/Plachta/VITS-Umamusume-voice-synthesizer/resolve/main/pretrained_models/D_trilingual.pth 模型重新命名為D_0.pth
  https://huggingface.co/spaces/Plachta/VITS-Umamusume-voice-synthesizer/resolve/main/pretrained_models/G_trilingual.pth 模型重新命名為G_0.pth
  https://huggingface.co/spaces/Plachta/VITS-Umamusume-voice-synthesizer/resolve/main/configs/uma_trilingual.json 右鍵另存新檔並重新命名為
  finetune_speaker.json
  ```
  CJ: Dualigual (Chinese, Japanese)
  ```
  https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/D_0-p.pth 
  https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/G_0-p.pth
  https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/config.json 右鍵另存新檔並重新命名為finetune_speaker.json
  ```
  C: Chinese only
  ```
  https://huggingface.co/datasets/Plachta/sampled_audio4ft/resolve/main/VITS-Chinese/D_0.pth 
  https://huggingface.co/datasets/Plachta/sampled_audio4ft/resolve/main/VITS-Chinese/G_0.pth 
  https://huggingface.co/datasets/Plachta/sampled_audio4ft/resolve/main/VITS-Chinese/config.json 右鍵另存新檔並重新命名為finetune_speaker.json
  ```
  D_0.pth和G_0.pth放在pretrained_models目錄下  
  finetune_speaker.json放在configs目錄下  
6.將您的語音資料放在對應的目錄下，詳細的不同上傳選項請參閱DATA.MD(https://github.com/Plachtaa/VITS-fast-fine-tuning/blob/main/DATA_EN.MD)
  短音頻  
    命名規則依照DATA.MD as a single .zip file;  
    放在./custom_character_voice/目錄下;  
    ```
    run unzip ./custom_character_voice/custom_character_voice.zip -d ./custom_character_voice/
    ```
  長音頻
    命名規則依照DATA.MD;
    放在./raw_audio/目錄下
  影片
    命名規則依照DATA.MD;
    放在./video_data/目錄下
7.處理所有音頻資料
```
  python scripts/video2audio.py
  python scripts/denoise_audio.py
  python scripts/long_audio_transcribe.py --languages "{PRETRAINED_MODEL}" --whisper_size large
  python scripts/short_audio_transcribe.py --languages "{PRETRAINED_MODEL}" --whisper_size large
  python scripts/resample.py
```
  根據之前選擇的型號選擇{CJ, CJE, C}替代"{PRETRAINED_MODEL}"
  確保您的 GPU 記憶體至少為12GB則使用--whisper_size。如果不是，請將參數更改medium or small.
8.處理所有文字資料
  如果您選擇新增輔助數據，請執行
  ```
  python preprocess_v2.py --add_auxiliary_data True --languages "{PRETRAINED_MODEL}"
  ```
  如果沒有，請執行根據您先前的模型選擇
  ```
  python preprocess_v2.py --languages "{PRETRAINED_MODEL}，"替換"{PRETRAINED_MODEL}"為其中之一。{CJ, CJE, C}
  ```
9.開始訓練
  運行
  ```
  python finetune_speaker_v2.py -m ./OUTPUT_MODEL --max_epochs "{Maximum_epochs}" --drop_speaker_embed True
  ```
  請替換{Maximum_epochs}為您想要的週期數。根據經驗，建議100或更多。
  若要繼續在先前的檢查點上進行訓練，請將訓練指令改為：
  ```
  python finetune_speaker_v2.py -m ./OUTPUT_MODEL --max_epochs "{Maximum_epochs}" --drop_speaker_embed False --cont True
  ```
  在執行此操作之前，請確保您有 previousG_latest.pth和D_latest.pthunder./OUTPUT_MODEL/在目錄下。
  若要查看訓練進度，請開啟新終端並cd進入專案根目錄，運行tensorboard --logdir=./OUTPUT_MODEL，然後localhost:6006使用 Web 瀏覽器存取。
10.訓練完成後，您可以透過執行以下命令來使用您的模型：
  ```
  python VC_inference.py --model_dir ./OUTPUT_MODEL/G_latest.pth --share True
  ```
