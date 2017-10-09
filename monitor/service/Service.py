# -*- coding: utf-8 -*-
# pip install web.py 通过这个安装
import json

import web
from trivest_data.dal.DataMonitorDao import DayNumTotalDao, SpaceCatchTotalDao, SpiderMonitor

urls = (
    '/monitor/dayNum', 'dayNum',
    '/monitor/spaceCatchNum', 'spaceCatchNum',
    '/(html|js|css|images)/(.*)', 'static',
    '/monitor/getAllProjectIdentify', 'ProjectIdentify',
    '/monitor/getProjectSpider', 'ProjectSpider',
    '/monitor/getProjectHeartBeat', 'ProjectHeatBeat'
)
app = web.application(urls, globals())


def dateToString(date):
    if not date:
        return ''
    try:
        return date.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print str(e)
        return ''


class dayNum:
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
        result = DayNumTotalDao().getAllTotal(dayBefore=dayBefore)
        return json.dumps(result)

    def POST(self, name):
        web.header("Access-Control-Allow-Origin", "*")
        print web.input()
        return "POST hello world"


class spaceCatchNum:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        # 获取各表的数量
        params = web.input()
        startTime = params.startTime
        endTime = params.endTime
        result = SpaceCatchTotalDao().getAllTotal(startTime, endTime)
        return json.dumps(result)

    def POST(self, name):
        web.header("Access-Control-Allow-Origin", "*")
        print web.input()
        return "POST hello world"


class ProjectIdentify:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        # 获取各表的数量
        params = web.input()
        results = SpiderMonitor().getAllProjectIdentify()
        newResults = []
        for result in results:
            newResults.append({
                'project_identify': result.project_identify
            })
        return json.dumps(newResults)

    def POST(self, name):
        web.header("Access-Control-Allow-Origin", "*")
        print web.input()
        return "POST hello world"


class ProjectHeatBeat:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        # 获取各表的数量 news spider!@xiamen!@2017-9-30 15:59!@7699
        params = web.input()
        projectIdentify = params.projectIdentify
        results = SpiderMonitor().getProjectHeartBeat(projectIdentify)
        newResults = []
        for result in results:
            newResults.append({
                'heart_beat_time': dateToString(result.heart_beat_time),
                'heart_beat_remark': result.heart_beat_remark,
            })
        return json.dumps(newResults)

    def POST(self, name):
        web.header("Access-Control-Allow-Origin", "*")
        print web.input()
        return "POST hello world"


class ProjectSpider:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        # 获取各表的数量 news spider!@xiamen!@2017-9-30 15:59!@7699
        params = web.input()
        projectIdentify = params.projectIdentify
        results = SpiderMonitor().getProjectSpider(projectIdentify)

        newResults = []
        for result in results:
            newResults.append({
                'heart_beat_time': dateToString(result.heart_beat_time),
                'heart_beat_remark': result.heart_beat_remark,
                'start_spider_time': dateToString(result.start_spider_time),
                'close_spider_time': dateToString(result.close_spider_time),
                'table_name': result.table_name,
                'spider_name': result.spider_name,
                'spider_name_zh': result.spider_name_zh,
                'table_name_zh': result.table_name_zh,
                'project_identify': result.project_identify,
                'item_type': result.item_type,
            })
        return json.dumps(newResults)

    def POST(self, name):
        web.header("Access-Control-Allow-Origin", "*")
        print web.input()
        return "POST hello world"


class static:
    def GET(self, media, file):
        try:
            f = open(media + '/' + file, 'r')
            return f.read()
        except:
            return 'no found'  # you can send an 404 error here if you want


if __name__ == '__main__':
    app.run()
