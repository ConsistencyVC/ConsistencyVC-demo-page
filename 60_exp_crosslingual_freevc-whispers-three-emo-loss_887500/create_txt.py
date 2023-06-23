import os
import random

# 要搜索的根目录
root_dir = 'C:/Users/32450/Desktop/guohoujian/code/PPGFreevc/FreeVC/dataset/crosslingual_emo_dataset/ESD_mul16k'

# 输出文件的路径
train_file = 'ESD_mul16k_emotrain.txt'
test_file = 'ESD_mul16k_emotest.txt'

# 创建两个空列表，用于存储找到的文件
train_files = []
test_files = []

# 使用 os.walk 遍历目录和子目录
for root, dirs, filenames in os.walk(root_dir):
    # 遍历文件名
    for filename in filenames:
        # 构造绝对路径
        filepath = os.path.join(root, filename)
        # 检查文件扩展名是否为 .wav
        if os.path.splitext(filepath)[1] == '.wav' and 'whisper10' not in filepath:
            # 生成一个随机数
            rnd = random.random()
            # 如果随机数小于 0.9，将文件放入训练集
            if rnd < 0.999:
                train_files.append(filepath)
            # 否则，将文件放入测试集
            else:
                test_files.append(filepath)
# 将训练集文件列表写入输出文件
with open(train_file, 'w') as f:
    for file in train_files:
        f.write(file + '\n')
# 将测试集文件列表写入输出文件
with open(test_file, 'w') as f:
    for file in test_files:
        f.write(file + '\n')
