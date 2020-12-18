"""
Creation Time : 2020.08.14

Create author : Tian FuKang
"""
import os
import glob
import pandas as pd
import random
import cv2
import xml.etree.ElementTree as ET


def resize_image(img, max_l):
    w = img.shape[1]
    h = img.shape[0]

    if w > h:
        scale = float(max_l) / float(w)
        w = max_l
        h = int(h * scale)
    else:
        scale = float(max_l) / float(h)
        h = max_l
        w = int(w * scale)

    img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)

    return img, scale


def xml_to_csv(path_1):
    xml_file_list = []

    # 在这里修改你需要检测的类别名字
    class_text = ['红灯', '绿灯', '黄灯', '斑马线', '限速', '解除限速']

    for xml_file in glob.glob(path_1 + '/*.xml'):
        xml_file_list.append(xml_file)

    for i in range(0, len(xml_file_list)):

        tree = ET.parse(xml_file_list[i])
        root = tree.getroot()

        filename = root.find('filename').text

        name = str(i + 1).zfill(12)
        # 在这里修改保存数据和标签的文件路径
        img_name = 'output/' + filename
        txt_name = 'output/' + filename.replace('.jpg', '') + '.txt'

        file_txt = open(txt_name, mode='a', encoding='utf-8')

        img_path = path_1.replace('xmls', 'imgs/') + filename
        image = cv2.imread(img_path)

        image, scale = resize_image(image, 640)

        cv2.imwrite(img_name, image)

        for member in root.findall('object'):
            class_id = class_text.index(member[0].text)

            xmin = int(member[5][0].text)
            ymin = int(member[5][1].text)
            xmax = int(member[5][2].text)
            ymax = int(member[5][3].text)

            # round(x, 6) 这里我设置了6位有效数字，可根据实际情况更改
            center_x = round(((xmin + xmax) / 2.0) * scale / float(image.shape[1]), 6)
            center_y = round(((ymin + ymax) / 2.0) * scale / float(image.shape[0]), 6)
            box_w = round(float(xmax - xmin) * scale / float(image.shape[1]), 6)
            box_h = round(float(ymax - ymin) * scale / float(image.shape[0]), 6)

            file_txt.write(str(class_id))
            file_txt.write(' ')
            file_txt.write(str(center_x))
            file_txt.write(' ')
            file_txt.write(str(center_y))
            file_txt.write(' ')
            file_txt.write(str(box_w))
            file_txt.write(' ')
            file_txt.write(str(box_h))
            file_txt.write('\n')

        file_txt.close()


def main():
    # 在这里修改xml文件的路径，我的xml文件在image_xml文件夹中，因此是以下设置方式
    path_2 = 'input/xmls'
    xml_to_csv(path_2)
    print('Successfully converted xml to csv.')


main()