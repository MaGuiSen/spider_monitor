# -*- coding: utf-8 -*-
import time
import datetime

from trivest_spider import getTableByName, fn

tablesName = [
    'diyicaijing_detail',
    'fenghuang_detail',
    'hexun_detail',
    'jiemian_detail',
    'jingrongjie_detail',
    'kuaixun_detail',
    'sina_detail',
    'sohu_detail',
    'taoguba_detail',
    'tengxun_detail',
    'wangyi_detail',
    'weixin_detail',
    'xueqiu_detail',
]


class SpaceCatchTotalDao(object):
    def getAllTotal(self, startTime, endTime):
        result = []
        for tableName in tablesName:
            table = getTableByName(tableName)
            total = self.getTotalByTable(table, startTime, endTime)
            tableNameShow = self.getTableNameShow(tableName)
            result.append({
                "total": total,
                "tableNameShow": tableNameShow,
                "table": tableName
            })
        result.append({
            "total": self.getWXSourceTotal(),
            "tableNameShow": u"微信源",
            "table": "weixin_source"
        })
        return result

    def getTotalByTable(self, table, startTime, endTime):
        try:
            startTime = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
            endTime = datetime.datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
            return table.select().where(table.update_time >= startTime, table.update_time <= endTime).count()
        except Exception as e:
            print str(e)
            return 0

    def getTableNameShow(self, tableName):
        tableNames = {
            'diyicaijing_detail': u'第一财经',
            'fenghuang_detail': u'凤凰',
            'hexun_detail': u'和讯',
            'jiemian_detail': u'界面',
            'jingrongjie_detail': u'金融界',
            'kuaixun_detail': u'快讯',
            'sina_detail': u'新浪',
            'sohu_detail': u'搜狐',
            'taoguba_detail': u'淘股吧',
            'tengxun_detail': u'腾讯',
            'wangyi_detail': u'网易',
            'weixin_detail': u'微信',
            'xueqiu_detail': u'雪球'
        }
        return tableNames[tableName]

    def getWXSourceTotal(self):
        try:
            table = getTableByName('weixin_source')
            return table.select().where(table.is_enable == 1, table.wx_url != '').count()
        except Exception as e:
            print str(e)
            return 0


class DayNumTotalDao(object):
    def getAllTotal(self, dayBefore=0):
        result = []
        for tableName in tablesName:
            table = getTableByName(tableName)
            total = self.getTotalByTable(table, dayBefore)
            tableNameShow = self.getTableNameShow(tableName)
            result.append({
                "total": total,
                "tableNameShow": tableNameShow,
                "table": tableName
            })
        result.append({
            "total": self.getWXSourceTotal(),
            "tableNameShow": u"微信源",
            "table": "weixin_source"
        })
        return result

    def getTotalByTable(self, table, dayBefore=0):
        try:
            today = datetime.datetime.today()
            lingChenTime_today = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
            lingChenTime_start = lingChenTime_today + datetime.timedelta(days=dayBefore)
            lingChenTime_end = lingChenTime_today + datetime.timedelta(days=dayBefore) + datetime.timedelta(days=1)
            return table.select().where(table.post_date >= lingChenTime_start, table.post_date < lingChenTime_end).count()
        except Exception as e:
            print str(e)
            return 0

    def getTableNameShow(self, tableName):
        tableNames = {
            'diyicaijing_detail': u'第一财经',
            'fenghuang_detail': u'凤凰',
            'hexun_detail': u'和讯',
            'jiemian_detail': u'界面',
            'jingrongjie_detail': u'金融界',
            'kuaixun_detail': u'快讯',
            'sina_detail': u'新浪',
            'sohu_detail': u'搜狐',
            'taoguba_detail': u'淘股吧',
            'tengxun_detail': u'腾讯',
            'wangyi_detail': u'网易',
            'weixin_detail': u'微信',
            'xueqiu_detail': u'雪球'
        }
        return tableNames[tableName]

    def getWXSourceTotal(self):
        try:
            table = getTableByName('weixin_source')
            return table.select().where(table.is_enable == 1, table.wx_url != '').count()
        except Exception as e:
            print str(e)
            return 0


if __name__== '__main__':
    table = getTableByName('spider_monitor')
    results = table.select(fn.Distinct(table.table_name))
    for ress in results:
        print ress
    pass


class SpiderMonitor(object):
    def getAllProjectIdentify(self):
        try:
            table = getTableByName('spider_monitor')
            return table.select(fn.Distinct(table.project_identify))
        except Exception as e:
            print str(e)

    def getProjectSpider(self, projectIdentify):
        try:
            table = getTableByName('spider_monitor')
            return table.select().where(table.project_identify == projectIdentify
                                        , table.item_type == 'spider')
        except Exception as e:
            print str(e)
        pass

    def getHeartBeatTime(self, projectIdentify, itemType, spiderName=''):
        """
        得到心跳更新时间
        """
        table = getTableByName('spider_monitor')
        return table.select().where(table.project_identify == projectIdentify,
                                    table.spider_name == spiderName,
                                    table.item_type == itemType)

    def projectHeatBeat(self, projectIdentify, heartBeatRemark=''):
        try:
            results = self.getHeartBeatTime(projectIdentify, 'project')
            nowDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(results):
                for result in results:
                    result.heart_beat_time = nowDate
                    result.heart_beat_remark = heartBeatRemark
                    result.save()
            else:
                table = getTableByName('spider_monitor')
                table.create(heart_beat_time=nowDate,
                             heart_beat_remark=heartBeatRemark,
                             project_identify=projectIdentify,
                             item_type='project',
                             spider_name='')
        except Exception as e:
            print str(e)

    def spiderHeatBeat(self, projectIdentify, spiderName, spiderDetail, heartBeatRemark=''):
        try:
            # spiderDetail 包含了spider相关的说明，此对象和数据子字段对应
            results = self.getHeartBeatTime(projectIdentify, 'spider', spiderName=spiderName)
            nowDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(results):
                for result in results:
                    result.heart_beat_time = nowDate
                    result.heart_beat_remark = heartBeatRemark
                    result.table_name = spiderDetail.get('table_name', '')
                    result.spider_name = spiderDetail.get('spider_name', '')
                    result.spider_name_zh = spiderDetail.get('spider_name_zh', '')
                    result.table_name_zh = spiderDetail.get('table_name_zh', '')
                    result.save()
            else:
                table = getTableByName('spider_monitor')
                table.create(
                    heart_beat_time=nowDate,
                    heart_beat_remark=heartBeatRemark,
                    project_identify=projectIdentify,
                    item_type='spider',
                    **spiderDetail)
        except Exception as e:
            print str(e)

    def updateStartSpiderTime(self, projectIdentify, spiderName, spiderDetail):
        try:
            results = self.getHeartBeatTime(projectIdentify, 'spider', spiderName=spiderName)
            nowDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(results):
                for result in results:
                    result.start_spider_time = nowDate
                    result.table_name = spiderDetail.get('table_name', '')
                    result.spider_name = spiderDetail.get('spider_name', '')
                    result.spider_name_zh = spiderDetail.get('spider_name_zh', '')
                    result.table_name_zh = spiderDetail.get('table_name_zh', '')
                    result.save()
            else:
                table = getTableByName('spider_monitor')
                table.create(
                    start_spider_time=nowDate,
                    project_identify=projectIdentify,
                    item_type='spider',
                    **spiderDetail)
            pass
        except Exception as e:
            print str(e)

    def updateCloseSpiderTime(self, projectIdentify, spiderName, spiderDetail):
        try:
            results = self.getHeartBeatTime(projectIdentify, 'spider', spiderName=spiderName)
            nowDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(results):
                for result in results:
                    result.close_spider_time = nowDate
                    result.table_name = spiderDetail.get('table_name', '')
                    result.spider_name = spiderDetail.get('spider_name', '')
                    result.spider_name_zh = spiderDetail.get('spider_name_zh', '')
                    result.table_name_zh = spiderDetail.get('table_name_zh', '')
                    result.save()
            else:
                table = getTableByName('spider_monitor')
                table.create(
                    close_spider_time=nowDate,
                    project_identify=projectIdentify,
                    item_type='spider',
                    **spiderDetail)
            pass
        except Exception as e:
            print str(e)

if __name__ == '__main__':
    SpiderMonitor().projectHeatBeat('11212', heartBeatRemark='10分钟跳一次')
    SpiderMonitor().projectHeatBeat('21', heartBeatRemark='10分钟跳一次')
    spiderDetail1 = {
        'table_name': 'wangyi_detail',
        'table_name_zh': '网易',
        'spider_name': 'wangyi_tech_scroll_news',
        'spider_name_zh': '网易-科技新闻'
    }
    SpiderMonitor().spiderHeatBeat('11212', 'wangyi_tech_scroll_news', spiderDetail1, heartBeatRemark='10分钟一次')

    spiderDetail2 = {
        'table_name': 'weixin_source',
        'table_name_zh': '微信',
        'spider_name': 'weixin_source',
        'spider_name_zh': '微信-科技新闻'
    }
    SpiderMonitor().spiderHeatBeat('11212', 'weixin_source', spiderDetail2, heartBeatRemark='半小时一次')

    spiderDetail3 = {
        'table_name': 'weixin_source',
        'table_name_zh': '微信',
        'spider_name': 'weixin_source',
        'spider_name_zh': '微信'
    }
    SpiderMonitor().spiderHeatBeat('22222', 'weixin_source', spiderDetail3, heartBeatRemark='半小时一次')

    SpiderMonitor().updateCloseSpiderTime('22222', 'weixin_source', spiderDetail3)
    SpiderMonitor().updateStartSpiderTime('22222', 'weixin_source', spiderDetail3)
    SpiderMonitor().updateCloseSpiderTime('11212', 'weixin_source', spiderDetail3)
    SpiderMonitor().updateCloseSpiderTime('wwwwwww', 'weixin_source', spiderDetail3)