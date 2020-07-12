import glob
import os

dir_name = input("请输入目标文件夹：")
source_path = r"C:\Users\SKNP\Documents\GitHub\cdn\img"

if dir_name == 'albums':
    sub_dir = os.listdir("\\".join([source_path, dir_name]))
    glob_path = {sub: "\\".join([source_path, dir_name, sub, "*[jpg,png]"]) for sub in sub_dir}
    for sub in glob_path:
        img_list = glob.glob(glob_path[sub], recursive=True)
        with open('{}.txt'.format(sub), mode='w') as f:
            for img in img_list:
                caption = img.split("\\")[-1]
                src = "https://cdn.jsdelivr.net/gh/Sknp1006/" + '/'.join(img.split("\\")[5:])
                f.writelines("- caption: " + caption + '\n')
                f.writelines("  src: " + src + '\n')
else:
    glob_path = {dir_name: "\\".join([source_path, dir_name, "*[jpg,png]"])}
    img_list = glob.glob(glob_path[dir_name], recursive=True)
    with open('{}.txt'.format(dir_name), mode='w') as f:
        for img in img_list:
            caption = img.split("\\")[-1]
            src = "https://cdn.jsdelivr.net/gh/Sknp1006/" + '/'.join(img.split("\\")[5:])
            f.writelines("- caption: " + caption + '\n')
            f.writelines("  src: " + src + '\n')
