import os
path = r'D:/Project/Root_Diction/'
file_path = []
for filename in os.listdir(path):  # 获取path下所有文件的路径
    file_path.append((os.path.join(path, filename)))
print(file_path[1])

def read():
    for i in range(len(file_path)):
        print(str("'"+"r"+file_path[i])+"'")
read()