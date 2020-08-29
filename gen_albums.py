import glob
import time
import random
from pathlib import Path
from tree import tree
from setting import cdn_path, albums_path


def create_albums(albums_dict, album, title=None, passwd=None,
                  cover="https://cdn.jsdelivr.net/gh/Sknp1006/cdn/img/avatar/none.jpg", desc=None):  # 创建新相册
    """
    创建相册流程:
      1) 新建[album_name].md文件
      2) 查看并保存index.md文件
      3) 更新index.md文件
    :param albums_dict:  相册字典
    :param album:  相册名(默认文件名)
    :param title:  标题(默认文件名)
    :param passwd:  密码
    :param cover:  封面(默认阿卡林)
    :param desc:  相册描述
    :return:
    """
    print("creating {}".format(album))
    md = "\\".join([albums_path, "{}.md".format(album)])  # 新建的md文件路径
    with open(md, 'w+', encoding='utf-8') as f:
        f.write('---\n')
        if title:
            f.write('title: {}\n'.format(title))  # title默认文件夹名
        else:
            f.write('title: {}\n'.format(album))
        f.write('date: {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))  # date会覆盖原来开的时间
        f.write('layout: gallery\n')
        if passwd:
            f.write('password: {}\n'.format(passwd))  # 设置密码
        f.write('photos:\n')
        f.writelines(albums_dict[album])
        f.write('---\n')
    with open("\\".join([albums_path, 'index.md']), 'r', encoding='utf-8') as f:  # 读取原来的index.md
        txt = f.readlines()[:-1]
    with open("\\".join([albums_path, 'index.md']), 'w', encoding='utf-8') as f:  # 在index.md添加新album
        f.writelines(txt)
        f.write('  - caption: {}\n'.format(title))
        f.write('    url: /albums/{}.html\n'.format(album))
        f.write('    cover: {}\n'.format(cover))
        f.write('    desc: {}\n'.format(desc))
        f.write('---\n')


def update_albums(albums_dict):  # 更新相册
    """
    更新相册流程:
    

    :param albums_dict:  相册字典

    :return:
    """
    for album in albums_dict:
        md = "\\".join([albums_path, "{}.md".format(album)])  # 对应album的md文件
        if not Path(md).is_file():  # 找不到，则新建一个相册
            cover = random.choice(albums_dict[album][1::2]).strip()[5:]  # 随机选取封面
            create_albums(albums_dict, album, cover=cover)
        with open(md, 'w+', encoding='utf-8') as f:
            f.write('---\n')
            f.write('title: {}\n'.format(album))
            f.write('date: {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
            f.write('layout: gallery\n')
            f.write('photos:\n')
            f.writelines(albums_dict[album])
            f.write('---\n')
        print("{} updated done!".format(album))


def read_txt(tree_path):  # 从txt读取文件配置
    albums_dict = {}
    txt_list = glob.glob(tree_path + "\\" + "*.txt")
    albums_txt = [txt for txt in txt_list if txt.split("\\")[-1].split("&")[0] == "albums"]
    for file in albums_txt:
        with open(file, 'r') as f:
            albums_dict[file.split("&")[-1].split(".")[0]] = f.readlines()
    return albums_dict


def update_tree(dir_name):  # 更新文件配置
    tree(dir_name)
    return "update done"


if __name__ == '__main__':
    update_tree('img/albums')
    dict = read_txt(cdn_path)
    update_albums(dict)
