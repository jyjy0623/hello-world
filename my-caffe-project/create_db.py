# -*- coding: UTF-8 -*-
import commands
import os
import re

"""
函数说明:生成图片列表清单txt文件

Parameters:
    images_path - 图片存放目录
    txt_save_path - 图片列表清单txt文件的保存目录
Returns:
    无
Author:
    Jack Cui
Modify:
    2017-03-29
"""
def createFileList(images_path, txt_save_path):
    #打开图片列表清单txt文件
    fw = open(txt_save_path,"w")
    #查看图片目录下的文件,相当于shell指令ls
    images_name = os.listdir(images_path)
    #遍历所有文件名
    for eachname in images_name:
        #正则表达式这里可以根据情况进行更改
        #正则表达式规则:找以cat开头,紧跟0到10个数字,并以jpg结尾的图片文件
        pattern_cat = r'(^cat\d{0,10}.jpg$)'
        #正则表达式规则:找以fish-bike开头,紧跟0到10个数字,以jpg结尾的图片文件
        pattern_bike = r'(^fish-bike\d{0,10}.jpg$)'
        #正则表达式匹配
        cat_name = re.search(pattern_cat, eachname)
        bike_name = re.search(pattern_bike, eachname)
        #按照规则将内容写入txt文件中
        if cat_name != None:
            fw.write(cat_name.group(0) + ' 1\n')
        if bike_name != None:
            fw.write(bike_name.group(0) + ' 2\n')
    #打印成功信息
    print "生成txt文件成功"
    #关闭fw
    fw.close()

"""
Parameters:
    caffe_root - caffe根目录
    images_path - 图片存放目录
    txt_save_path - 图片列表清单txt文件的保存目录
Returns:
    无
Author:
    Jack Cui
Modify:
    2017-03-29
"""
def create_db(caffe_root, images_path, txt_save_path):
    #lmdb文件名字
    lmdb_name = 'img_train.lmdb'
    #生成的db文件的保存目录
    lmdb_save_path = caffe_root + 'my-caffe-project/' + lmdb_name
    #convert_imageset工具路径
    convert_imageset_path = caffe_root + 'build/tools/convert_imageset'
    cmd = """%s --shuffle --resize_height=256 --resize_width=256 %s %s %s"""
    status, output = commands.getstatusoutput(cmd % (convert_imageset_path, images_path, 
        txt_save_path, lmdb_save_path))
    print output
    if(status == 0):
        print "lmbd文件生成成功"

if __name__ == '__main__':
    #caffe_root目录
    caffe_root = '/home/jyjy0623/caffe/'
    #my-caffe-project目录
    my_caffe_project = caffe_root + 'my-caffe-project/'
    #图片存放目录
    images_path = caffe_root + 'examples/images/'
    #生成的图片列表清单txt文件名
    txt_name = 'filelist.txt'
    #生成的图片列表清单txt文件的保存目录
    txt_save_path = my_caffe_project + txt_name
    #生成txt文件
    createFileList(images_path, txt_save_path)
    #生成lmdb文件
    create_db(caffe_root, images_path, txt_save_path)
