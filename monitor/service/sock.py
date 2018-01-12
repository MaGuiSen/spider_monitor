# -*- coding: utf-8 -*-

import socket

# 可以用
# http://www.maguisen.top/all/html/baicha.html
# get_str = (
#     "GET /all/html/baicha.html HTTP/1.1\r\n"
#     "Host: www.maguisen.top\r\n"
#     "Connection: keep-alive\r\n"
#     "Cache-Control: max-age=0\r\n"
#     "Upgrade-Insecure-Requests: 1\r\n"
#     "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36\r\n\r\n\r\n"
#     "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n"
#     "Accept-Encoding: gzip, deflate\r\n"
#     "Accept-Language: zh-CN,zh;q=0.8\r\n"
#     "If-None-Match: \"8d4d6fd392fd31:0\"\r\n"
#     "If-Modified-Since: Sat, 16 Sep 2017 16:35:37 GMT\r\n"
# )
#
# def get():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(('www.maguisen.top', 80))
#     url = "/zj510/article/details/52278144"
#     port = "80"
#     sock.send(get_str)
#     response = sock.recv(4096)
#     return response

# 待测试http://www.cookteching.com:8888/demo/insert?name=cjm&status=1
# http://www.cookteching.com:8888/demo/get?id=aaa
get_str = (
    "GET /demo/get?id=02a56a67-76df-41f5-bc6f-81edef177ae7\r\nHTTP/1.1\r\n"
    "Host: www.cookteching.com:8888\r\n"
    "Connection: keep-alive\r\n"
    "Cache-Control: max-age=0\r\n"
    "Upgrade-Insecure-Requests: 1\r\n"
    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36\r\n\r\n"
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n"
    "Accept-Encoding: gzip, deflate\r\n"
    "Accept-Language: zh-CN,zh;q=0.8\r\n"
)

def get():
    sock = socket.socket()
    sock.connect(('www.cookteching.com', 8888))
    sock.send(get_str)
    temp = sock.recv(4096)
    response = temp
    while temp:
        temp = sock.recv(4096)
        response += temp
    return response


print get()
print len(get_str)
