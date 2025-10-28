import os

folder = r"C:\Users\21005\PycharmProjects\PythonProject\images"  # 修改为你的 images 文件夹路径
files = os.listdir(folder)
files = sorted(files)  # 按名称顺序排序

for i, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1]  # 获取扩展名（.jpg）
    new_name = f"p{i}{ext}"
    os.rename(
        os.path.join(folder, filename),
        os.path.join(folder, new_name)
    )

print("批量改名完成！")
