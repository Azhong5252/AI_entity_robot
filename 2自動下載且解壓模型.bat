@echo off
call curl -L -o GPT-SoVITS-main\pretrained_models.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_pretrained_models/pretrained_models.zip
call curl -L -o GPT-SoVITS-main\models.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_ASR_model/models.zip
call tar -xf "GPT-SoVITS-main\pretrained_models.zip" -C "GPT-SoVITS-main\GPT_SoVITS"
call tar -xf "GPT-SoVITS-main\models.zip" -C "GPT-SoVITS-main\tools\asr"
