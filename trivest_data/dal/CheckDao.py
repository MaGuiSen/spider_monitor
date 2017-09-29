# -*- coding: utf-8 -*-
from util import EncryptUtil
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
    # 'diyicaijing_detail': DiyicaijingDetail,
    # 'fenghuang_detail': FenghuangDetail,
    # 'hexun_detail': HexunDetail,
    # 'jiemian_detail': JiemianDetail,
    # 'jingrongjie_detail': JingrongjieDetail,
    # 'kuaixun_detail': KuaixunDetail,
    # 'sina_detail': SinaDetail,
    # 'sohu_detail': SohuDetail,
    # 'taoguba_detail': TaogubaDetail,
    # 'tengxun_detail': TengxunDetail,
    # 'wangyi_detail': WangyiDetail,
    # 'weixin_detail': WeixinDetail,
    # 'weixin_source': WeixinSource,
    # 'xueqiu_detail': XueqiuDetail,

    'diyicaijing_detail': DiyicaijingDetailTest,
    'fenghuang_detail': FenghuangDetailTest,
    'hexun_detail': HexunDetailTest,
    'jiemian_detail': JiemianDetailTest,
    'jingrongjie_detail': JingrongjieDetailTest,
    'kuaixun_detail': KuaixunDetailTest,
    'sina_detail': SinaDetailTest,
    'sohu_detail': SohuDetailTest,
    'taoguba_detail': TaogubaDetailTest,
    'tengxun_detail': TengxunDetailTest,
    'wangyi_detail': WangyiDetailTest,
    'weixin_detail': WeixinDetailTest,
    'weixin_source': WeixinSourceTest,
    'xueqiu_detail': XueqiuDetailTest,
}


class CheckDao(object):
    def __init__(self, tableName):
        self.hashList = []  # 代表此次已经存在的hash,防止同一时间得到相同文章进行抓取
        self.Table = Tables[tableName]  # TODO..del 删除test

    def resetHashList(self):
        # 每次重新抓取的时候清除
        self.hashList = []

    def checkExist(self, source_url):
        """
        存在逻辑判断
        """
        hash_code = self.getHashCode(source_url)
        results = self.Table.select().where(self.Table.hash_code == hash_code)
        if results or self.isInHashList(hash_code):
            return True
        else:
            self.hashList.append(hash_code)
            return False

    def checkWxArticleExist(self, title, wx_account, source_id):
        """
        存在逻辑判断
        source_id : 源ID 微信为1
        """
        hash_code = self.getWxArticleHashCode(title, wx_account, source_id)
        results = self.Table.select().where(self.Table.hash_code == hash_code)
        if results or self.isInHashList(hash_code):
            return True
        else:
            self.hashList.append(hash_code)
            return False

    def isInHashList(self, hash_code):
        return hash_code in self.hashList

    def getWxArticleHashCode(self, title, wx_account, source_id):
        # 具体逻辑 微信专用，别的请使用getHashCode
        return EncryptUtil.md5(title.encode('utf8')+wx_account.encode('utf8')+str(source_id))

    def getHashCode(self, source_url):
        # 具体逻辑
        return EncryptUtil.md5(source_url)

    def getAllHtml(self):
        return self.Table.select(self.Table.hash_code, self.Table.content_html)

    def update(self, hash_code, styles, content_html):
        self.Table.update(styles=styles, content_html=content_html).where(self.Table.hash_code == hash_code).execute()

    def getHtml(self, pageIndex):
        """
        获取content_html
        """
        return self.Table.select(self.Table.hash_code, self.Table.content_html)\
            .order_by(self.Table.update_time)\
            .paginate(pageIndex, 15)

    def getSubChannel(self, pageIndex):
        """
        获取sub_channel
        """
        return self.Table.select(self.Table.hash_code, self.Table.sub_channel) \
            .order_by(self.Table.update_time) \
            .paginate(pageIndex, 15)

    def updateStyles(self, hash_code, styles):
        self.Table.update(styles=styles).where(self.Table.hash_code == hash_code).execute()

    def updateHtml(self, hash_code, content_html):
        self.Table.update(content_html=content_html).where(self.Table.hash_code == hash_code).execute()

    def updateSubChannel(self, hash_code, sub_channel):
        self.Table.update(sub_channel=sub_channel).where(self.Table.hash_code == hash_code).execute()

