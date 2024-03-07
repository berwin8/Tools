import os

# 将这个路径替换为你的文件夹路径
your_directory_path = r''
for filename in os.listdir(your_directory_path):
    if filename.startswith('OldName'):
        print(filename)
        # 构造原文件完整路径
        old_file = os.path.join(your_directory_path, filename)
        # 构造新文件名（替换 'OldName' 为 'NewName'）和完整路径
        new_filename = filename.replace('OldName', 'NewName')
        new_file = os.path.join(your_directory_path, new_filename)
        # 重命名文件
        os.rename(old_file, new_file)
        print(f'Renamed "{filename}" to "{new_filename}"')
