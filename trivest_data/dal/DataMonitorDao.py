# -*- coding: utf-8 -*-
import time
import datetime

from trivest_spider import getTableByName, fn

tablesName = [
    'diyicaijing_detail',
    'fenghuang_detail',
    'hexun_detail',
    'jiemian_detail',
    'jinrongjie_detail',
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
            'jinrongjie_detail': u'金融界',
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
            'jinrongjie_detail': u'金融界',
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

    def getProjectHeartBeat(self, projectIdentify):
        try:
            table = getTableByName('spider_monitor')
            return table.select(table.heart_beat_time, table.heart_beat_time_space, table.heart_beat_remark).where(table.project_identify == projectIdentify
                                        , table.item_type == 'project')
        except Exception as e:
            print str(e)
        pass

    def getHeartBeatTime(self):
        """
        得到心跳更新时间
        """
        table = getTableByName('spider_monitor')
        return table.select()