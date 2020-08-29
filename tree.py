from pathlib import Path
from setting import cdn_url, source_path

exclude_dir = ['.git', '.idea', '.txt']
exclude_file = ['txt', 'py', 'gitignore']  # 以"."开头的文件先去掉"."


def is_not_txt(file):
    sp = file.split(".")
    if sp[-1] not in exclude_file:
        return 1


def write(file_list, path, pic_type):
    name = '&'.join(str(file_list[0]).split('\\')[-3:-1])
    if pic_type == 'albums':
        print(name)
        with open('{}.txt'.format(name), mode='w') as f:
            for img in file_list:
                caption = str(img).split("\\")[-1]
                src = "/".join([cdn_url, str(path).replace('\\', '/'), caption])
                f.writelines("  - caption: " + caption + '\n')
                f.writelines("    src: " + src + '\n')
    elif pic_type == 'ordinary':
        with open('{}.txt'.format(name), mode='w') as f:
            for img in file_list:
                caption = str(img).split("\\")[-1]
                src = "/".join([cdn_url, str(path).replace('\\', '/'), caption])
                f.writelines(src + '\n')
    elif pic_type == 'likes':
        pass


def tree(dir_name):
    if Path(dir_name).is_dir():
        path = Path(dir_name)
    else:
        path = Path("\\".join([source_path, dir_name]))
        if not path.exists():
            raise Exception('"{}" not exist'.format(path))

    path_list = [dir for dir in path.iterdir() if dir.is_dir()]
    file_list = [dir for dir in path.iterdir() if dir.is_file() and is_not_txt(str(dir))]
    if path_list:
        for path in path_list:
            if path.name not in exclude_dir:
                # print("path:", path)
                # print("dir_name:", dir_name)
                tree(path)

    if file_list:
        if 'albums' in str(file_list[0]).split('\\'):
            write(file_list, path, 'albums')
        else:
            write(file_list, path, 'ordinary')
