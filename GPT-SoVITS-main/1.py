import torch
import psutil

ngpu = torch.cuda.device_count()  # 獲取可用 GPU 數量
if_gpu_ok = False
gpu_infos = []
mem = []

if torch.cuda.is_available() or ngpu != 0:
    print("Entering GPU check loop...")
    for i in range(ngpu):
        gpu_name = torch.cuda.get_device_name(i)
        print(f"Found GPU: {gpu_name}")  # 打印 GPU 名稱
        if any(value in gpu_name.upper() for value in ["10", "16", "20", "30", "40", "A2", "A3", "A4", "P4", "A50", "500", "A60", "70", "80", "90", "M4", "T4", "TITAN", "L4", "4060", "3060-ti"]):
            if_gpu_ok = True
            gpu_infos.append("%s\t%s" % (i, gpu_name))
            mem.append(int(torch.cuda.get_device_properties(i).total_memory / 1024 / 1024 / 1024 + 0.4))
            print(f"GPU {i} is valid and added.")

if if_gpu_ok and len(gpu_infos) > 0:
    gpu_info = "\n".join(gpu_infos)
    print(f"Valid GPUs found:\n{gpu_info}")
    default_batch_size = min(mem) // 2
else:
    print("No valid GPU found, using CPU.")
    gpu_info = ("%s\t%s" % ("0", "CPU"))
    gpu_infos.append("%s\t%s" % ("0", "CPU"))
    default_batch_size = int(psutil.virtual_memory().total / 1024 / 1024 / 1024 / 2)