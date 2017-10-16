# coding:utf-8
"""
    python图片处理
    @author:fc_lamp
    @blog:http://fc-lamp.blog.163.com/
"""
import os

import requests
from PIL import Image as image


def resizeImg(**args):
    args_key = {'ori_img': '', 'dst_img': '', 'dst_w': '', 'dst_h': '', 'save_q': 100}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]

    im = image.open(arg['ori_img'])
    if im.format in ['gif', 'GIF', 'Gif']:
        return
    ori_w, ori_h = im.size
    widthRatio = heightRatio = None
    ratio = 1
    if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):
        if arg['dst_w'] and ori_w > arg['dst_w']:
            widthRatio = float(arg['dst_w']) / ori_w  # 正确获取小数的方式
        if arg['dst_h'] and ori_h > arg['dst_h']:
            heightRatio = float(arg['dst_h']) / ori_h

        if widthRatio and heightRatio:
            if widthRatio < heightRatio:
                ratio = widthRatio
            else:
                ratio = heightRatio

        if widthRatio and not heightRatio:
            ratio = widthRatio
        if heightRatio and not widthRatio:
            ratio = heightRatio

        newWidth = int(ori_w * ratio)
        newHeight = int(ori_h * ratio)
    else:
        newWidth = ori_w
        newHeight = ori_h

    if len(im.split()) == 4:
        # prevent IOError: cannot write mode RGBA as BMP
        r, g, b, a = im.split()
        im = image.merge("RGB", (r, g, b))

    im.resize((newWidth, newHeight), image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])


image_urls = [
    {
        'url': 'http://p0.ifengimg.com/pmop/2017/1010/E66C2599CE9403A670AD405F4CCAB271B366D7DC_size415_w1290_h692.png',
        'size': '195k'
    },
    {
        'url': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1507628845453&di=86cd609300a55bde04a185d2eb4b719b&imgtype=0&src=http%3A%2F%2Fb.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F55e736d12f2eb9380291af03df628535e4dd6f47.jpg',
        'size': '120k'
    },
    {
        'url': 'http://image.baidu.com/search/down?tn=download&word=download&ie=utf8&fr=detail&url=http%3A%2F%2Fimg6.3lian.com%2Fc23%2Fdesk4%2F04%2F57%2Fd%2F10.jpg',
        'size': '1M'
    }
]
image_paths = []
savePath = os.getcwd()
for index, image_url in enumerate(image_urls):
    fileName = str(index) + '.jpg'
    srcPath = savePath + '\\image\\src\\' + fileName
    desPath = savePath + '\\image\\des\\' + fileName

    fileResponse = requests.get(image_url.get('url', ''), timeout=10)
    req_code = fileResponse.status_code
    req_msg = fileResponse.reason

    if req_code == 200:
        open(srcPath, 'wb').write(fileResponse.content)
        # 判断大小是否大于100kb 压缩一半，
        if len(fileResponse.content) > 100 * 1000:
            # TODO...压缩
            pass
            # 目标图片大小
            dst_w = 600
            dst_h = 600
            # 保存的图片质量
            save_q = 80
            resizeImg(ori_img=srcPath, dst_img=srcPath, dst_w=dst_w, dst_h=dst_h, save_q=save_q)
