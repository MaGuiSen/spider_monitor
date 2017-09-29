# -*- coding: utf-8 -*-
import time
import datetime

from trivest_spider import DataMonitor, fn
from trivest_spider import DiyicaijingDetail, DiyicaijingDetailTest
from trivest_spider import FenghuangDetail, FenghuangDetailTest
from trivest_spider import HexunDetail, HexunDetailTest
from trivest_spider import JiemianDetail, JiemianDetailTest
from trivest_spider import JingrongjieDetail, JingrongjieDetailTest
from trivest_spider import KuaixunDetail, KuaixunDetailTest
from trivest_spider import SinaDetail, SinaDetailTest
from trivest_spider import SohuDetail, SohuDetailTest
from trivest_spider import TaogubaDetail, TaogubaDetailTest
from trivest_spider import TengxunDetail, TengxunDetailTest
from trivest_spider import WangyiDetail, WangyiDetailTest
from trivest_spider import WeixinDetail, WeixinDetailTest
from trivest_spider import WeixinSource, WeixinSourceTest
from trivest_spider import XueqiuDetail, XueqiuDetailTest

# TODO..如果是测试，就启用下方的
Tables = {
    'diyicaijing_detail': DiyicaijingDetail,
    'fenghuang_detail': FenghuangDetail,
    'hexun_detail': HexunDetail,
    'jiemian_detail': JiemianDetail,
    'jingrongjie_detail': JingrongjieDetail,
    'kuaixun_detail': KuaixunDetail,
    'sina_detail': SinaDetail,
    'sohu_detail': SohuDetail,
    'taoguba_detail': TaogubaDetail,
    'tengxun_detail': TengxunDetail,
    'wangyi_detail': WangyiDetail,
    'weixin_detail': WeixinDetail,
    'xueqiu_detail': XueqiuDetail,

    # 'diyicaijing_detail': DiyicaijingDetailTest,
    # 'fenghuang_detail': FenghuangDetailTest,
    # 'hexun_detail': HexunDetailTest,
    # 'jiemian_detail': JiemianDetailTest,
    # 'jingrongjie_detail': JingrongjieDetailTest,
    # 'kuaixun_detail': KuaixunDetailTest,
    # 'sina_detail': SinaDetailTest,
    # 'sohu_detail': SohuDetailTest,
    # 'taoguba_detail': TaogubaDetailTest,
    # 'tengxun_detail': TengxunDetailTest,
    # 'wangyi_detail': WangyiDetailTest,
    # 'weixin_detail': WeixinDetailTest,
    # 'xueqiu_detail': XueqiuDetailTest,
}


class SpaceCatchTotalDao(object):
    def getAllTotal(self, startTime, endTime):
        result = []
        for tableName in Tables:
            total = self.getTotalByTable(Tables[tableName], startTime, endTime)
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
            return WeixinSource.select().where(WeixinSource.is_enable == 1, WeixinSource.wx_url != '').count()
        except Exception as e:
            print str(e)
            return 0


class DayNumTotalDao(object):
    def getAllTotal(self, dayBefore=0):
        result = []
        for tableName in Tables:
            total = self.getTotalByTable(Tables[tableName], dayBefore)
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
            return WeixinSource.select().where(WeixinSource.is_enable == 1, WeixinSource.wx_url != '').count()
        except Exception as e:
            print str(e)
            return 0



if __name__== '__main__':
    result = TotalDao().getTotalByTable(WeixinDetail, dayBefore=0)
    print result

class DataMonitorDao(object):
    def getHeartBeatTime(self, type=''):
        """
        得到心跳更新时间
        """
        if type:
            return DataMonitor.select()
        else:
            return DataMonitor.select().where(DataMonitor.type == type)

    def heartBeat(self, type='', info='跳动中', remark='1分钟更新一次'):
        """
        更新跳动时间(不存在则添加)
        """
        if not type:
            return
        results = self.getHeartBeatTime()
        nowDate = datetime.datetime.now()
        print '跳一下', nowDate
        if len(results):
            for result in results:
                result.update_time = nowDate
                result.remark = remark
                result.info = info
                result.save()
        else:
            DataMonitor.create(info=info, remark=remark, type=type, update_time=nowDate)