import glob

img_list = glob.glob(r"C:\Users\SKNP\Documents\GitHub\cdn\img\arknights/*.jpg")
print(img_list)
with open('albums.txt', mode='w') as f:
    for img in img_list:
        caption = img.split("\\")[-1]
        src = "https://cdn.jsdelivr.net/gh/Sknp1006/cdn/img/arknights/" + caption

        f.writelines("- caption: " + caption + '\n')
        f.writelines("  src: " + src + '\n')

