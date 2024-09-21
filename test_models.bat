@echo off
call curl -L -o GPT-SoVITS-main\Ayaka_sovits_models.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_test_models/Ayaka_sovits_models.zip
call curl -L -o GPT-SoVITS-main\logs.zip https://github.com/Azhong5252/AI_entity_robot/releases/download/GPT-SoVITS_test_models_log/logs.zip
call tar -xf "GPT-SoVITS-main\Ayaka_sovits_models.zip" -C "GPT-SoVITS-main"
call tar -xf "GPT-SoVITS-main\logs.zip" -C "GPT-SoVITS-main"