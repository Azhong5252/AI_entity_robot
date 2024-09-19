@echo off
call cd /d %cd%
call cd /d "VITS-fast-fine-tuning-webui-v1.1"
mkdir Audio
call cd ..
call cd /d "GPT-SoVITS-main"
mkdir Audio
cd ..
cmd /k
