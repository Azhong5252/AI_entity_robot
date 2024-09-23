@echo off
curl -L -o GPT-SoVITS-main\uvr5.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_uvr5/uvr5.zip
curl -L -o GPT-SoVITS-main\pretrained_models.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_pretrained_models/pretrained_models.zip
curl -L -o GPT-SoVITS-main\models.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_ASR_model/models.zip
tar -xf "GPT-SoVITS-main\uvr5.zip" -C "GPT-SoVITS-main\tools\uvr5\uvr5_weights"
tar -xf "GPT-SoVITS-main\pretrained_models.zip" -C "GPT-SoVITS-main\GPT_SoVITS"
tar -xf "GPT-SoVITS-main\models.zip" -C "GPT-SoVITS-main\tools\asr"
