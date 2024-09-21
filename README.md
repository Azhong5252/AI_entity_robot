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
第一步點擊0啟動.bat執行

#除了第一步在資料夾點擊之外其餘都是在開啟的終端機執行
#
第二步在執行 1創建虛擬環境.bat(創建虛擬環境)
#
第三步執行 2自動下載且解壓模型.bat(會自動下載pretrained_models.zip和models.zip且會自動解壓縮，需要較久時間下載和解壓縮)
#
第四步執行 3啟動虛擬環境(未安裝套件).bat(第一次創建這個虛擬環境，進到虛擬環境)

#非第一次創建這個虛擬環境但要直接進入虛擬環境的話 3啟動虛擬環境.bat

#要離開虛擬環境可以執行 3關閉虛擬環境.bat

#要刪除這個虛擬環境的話 999刪除虛擬環境.bat
#
第五步執行 4啟動主程式.bat(執行main.py)

#執行之前先確認有沒有訓練後的models(SoVITS的)，若不想訓練到第五步時可以先點開test_models.bat，會把測試用的聲音模型自動載入，載完後就可以執行4啟動主程式.bat
#
溫馨提示!當在terminal要執行.bat可以用tab，例如要執行 3啟動虛擬環境(未安裝套件).bat，可以打個 3啟動 然後按tab找到那個.bat檔
