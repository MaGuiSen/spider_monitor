# -*- coding: utf-8 -*-
# pip install web.py 通过这个安装
import json

import web
from trivest_data.dal.DataMonitorDao import TotalDao

urls = (
    '/monitor', 'monitor',
    '/(html|js|css|images)/(.*)', 'static',
)
app = web.application(urls, globals())


class monitor:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        # 获取各表的数量
        params = web.input()
        dayBefore = params.dayBefore or 0
        try:
            dayBefore = int(dayBefore)
        except Exception as e:
            print str(e)
            dayBefore = 0
        result = TotalDao().getAllTotal(dayBefore=dayBefore)
        return json.dumps(result)

    def POST(self, name):
        web.header("Access-Control-Allow-Origin", "*")
        print web.input()
        return "POST hello world"


class static:
    def GET(self, media, file):
        try:
            f = open(media+'/'+file, 'r')
            return f.read()
        except:
            return 'no found'  # you can send an 404 error here if you want


if __name__ == '__main__':
    app.run()