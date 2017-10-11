# coding=utf-8
# Code generated by:
# python -m pwiz -e mysql -H 192.168.0.20 -p 3306 -u root -i -P trivest_spider
# Date: September 25, 2017 09:29AM
# Database: trivest_spider
# Peewee version: 2.9.2

from peewee import *
from trivest_data.config.app import config
from playhouse.shortcuts import RetryOperationalError

__mysql_config = config['mysql']


class MyRetryDB(RetryOperationalError, MySQLDatabase):
    pass

import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

database = MyRetryDB(__mysql_config['database'],
                     **{'host': __mysql_config['host'], 'password': __mysql_config['password'],
                        'port': int(__mysql_config['port']), 'user': __mysql_config['user']})


# TODO...新增一个表的对象，就在此处添加一个键值对，指定数据库名称和类的对应关系(key为数据库名称)
def getTableByName(tableName):
    Tables = {
        'spider_monitor': SpiderMonitor,

        'diyicaijing_detail': DiyicaijingDetail,
        'fenghuang_detail': FenghuangDetail,
        'hexun_detail': HexunDetail,
        'jiemian_detail': JiemianDetail,
        'jinrongjie_detail': JinrongjieDetail,
        'kuaixun_detail': KuaixunDetail,
        'sina_detail': SinaDetail,
        'sohu_detail': SohuDetail,
        'taoguba_detail': TaogubaDetail,
        'tengxun_detail': TengxunDetail,
        'wangyi_detail': WangyiDetail,
        'weixin_detail': WeixinDetail,
        'weixin_source': WeixinSource,
        'xueqiu_detail': XueqiuDetail,

        # 'diyicaijing_detail': DiyicaijingDetailTest,
        # 'fenghuang_detail': FenghuangDetailTest,
        # 'hexun_detail': HexunDetailTest,
        # 'jiemian_detail': JiemianDetailTest,
        # 'jinrongjie_detail': JinrongjieDetailTest,
        # 'kuaixun_detail': KuaixunDetailTest,
        # 'sina_detail': SinaDetailTest,
        # 'sohu_detail': SohuDetailTest,
        # 'taoguba_detail': TaogubaDetailTest,
        # 'tengxun_detail': TengxunDetailTest,
        # 'wangyi_detail': WangyiDetailTest,
        # 'weixin_detail': WeixinDetailTest,
        # 'weixin_source': WeixinSourceTest,
        # 'xueqiu_detail': XueqiuDetailTest,
    }
    return Tables[tableName]


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


# 爬虫监控类
class SpiderMonitor(BaseModel):
    heart_beat_time = DateTimeField(null=True)
    heart_beat_remark = CharField(null=True)
    start_spider_time = DateTimeField(null=True)
    close_spider_time = DateTimeField(null=True)
    table_name = CharField(null=True)
    spider_name = CharField(null=True)
    spider_name_zh = CharField(null=True)
    table_name_zh = CharField(null=True)
    project_identify = CharField(null=True)
    item_type = CharField(null=True)
    heart_beat_time_space = IntegerField(null=True)

    class Meta:
        db_table = 'spider_monitor_new'


class DataMonitor(BaseModel):
    account = CharField(null=True)
    info = CharField(null=True)
    remark = CharField(null=True)
    type = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        db_table = 'data_monitor'


# TODO..del
class DiyicaijingDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'diyicaijing_detail_test'


class DiyicaijingDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'diyicaijing_detail'


class EtlHistory(BaseModel):
    apply_time = DateTimeField(null=True)
    table_name = CharField(primary_key=True)

    class Meta:
        db_table = 'etl_history'


# TODO..del
class FenghuangDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'fenghuang_detail_test'


class FenghuangDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'fenghuang_detail'


# TODO..del
class HexunDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'hexun_detail_test'


class HexunDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'hexun_detail'


# TODO...del
class JiemianDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'jiemian_detail_test'


class JiemianDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'jiemian_detail'


# TODO...del
class JinrongjieDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'jinrongjie_detail_test'


class JinrongjieDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'jinrongjie_detail'


# TODO...del
class KuaixunDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'kuaixun_detail_test'


class KuaixunDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'kuaixun_detail'


class ScrapyLog(BaseModel):
    attach = CharField(null=True)
    belong_to = CharField(null=True)
    info = TextField(null=True)
    level = CharField(null=True)
    save_time = DateTimeField(null=True)

    class Meta:
        db_table = 'scrapy_log'


# TODO...del
class SinaDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        db_table = 'sina_detail_test'


class SinaDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        db_table = 'sina_detail'


class SinaHkCompany(BaseModel):
    auditor = TextField(null=True)
    business = TextField(null=True)
    directors = TextField(null=True)
    email = TextField(null=True)
    en_name = TextField(null=True)
    fax = TextField(null=True)
    from_url = TextField(null=True)
    header_address = TextField(null=True)
    industry = TextField(null=True)
    lawer = TextField(null=True)
    main_bank = TextField(null=True)
    main_holder = TextField(null=True)
    name = TextField(null=True)
    president = TextField(null=True)
    reg_address = TextField(null=True)
    secretory = TextField(null=True)
    share_num = TextField(null=True)
    symbol = TextField(null=True)
    tel = TextField(null=True)
    transfer_address = TextField(null=True)
    website = TextField(null=True)

    class Meta:
        db_table = 'sina_hk_company'


class SinaNewsDetail(BaseModel):
    content_html = TextField(null=True)
    html = TextField(null=True)
    title = TextField(null=True)
    url = TextField(null=True)

    class Meta:
        db_table = 'sina_news_detail'


class SinaNewsList(BaseModel):
    author = TextField(null=True)
    authoruid = TextField(null=True)
    categoryid = TextField(null=True)
    channelid = TextField(null=True)
    columnid = TextField(null=True)
    comment_reply = FloatField(null=True)
    comment_show = FloatField(null=True)
    comment_total = FloatField(null=True)
    commentid = TextField(null=True)
    ctime = TextField(null=True)
    docid = TextField(null=True)
    ext = TextField(null=True)
    ext_0 = TextField(null=True)
    ext_1 = TextField(null=True)
    ext_2 = TextField(null=True)
    ext_3 = TextField(null=True)
    ext_4 = TextField(null=True)
    images = TextField(null=True)
    img = TextField(null=True)
    intime = TextField(null=True)
    intro = TextField(null=True)
    ipad_vid = TextField(null=True)
    keywords = TextField(null=True)
    level = TextField(null=True)
    lids = TextField(null=True)
    media_name = TextField(null=True)
    mediaid = TextField(null=True)
    mlids = TextField(null=True)
    mtime = TextField(null=True)
    oid = TextField(null=True)
    productid = TextField(null=True)
    stitle = TextField(null=True)
    subjectid = TextField(null=True)
    summary = TextField(null=True)
    templateid = TextField(null=True)
    title = TextField(null=True)
    url = TextField(null=True)
    urls = TextField(null=True)
    vid = TextField(null=True)
    video = TextField(db_column='video_id', null=True)
    video_time_length = TextField(null=True)
    wapsummary = TextField(null=True)
    wapurl = TextField(null=True)
    wapurls = TextField(null=True)

    class Meta:
        db_table = 'sina_news_list'


class SinaUsCompany(BaseModel):
    address = TextField(null=True)
    en_name = TextField(null=True)
    from_url = TextField(null=True)
    intro = TextField(null=True)
    name = TextField(null=True)
    short_name = TextField(null=True)
    symbol = TextField(null=True)
    website = TextField(null=True)

    class Meta:
        db_table = 'sina_us_company'


class SinaUsDirector(BaseModel):
    crawl_time = TextField(null=True)
    from_url = TextField(null=True)
    name = TextField(null=True)
    resume = TextField(null=True)
    symbol = TextField(null=True)

    class Meta:
        db_table = 'sina_us_director'


class SinaUsManager(BaseModel):
    crawl_time = TextField(null=True)
    from_url = TextField(null=True)
    name = TextField(null=True)
    resume = TextField(null=True)
    symbol = TextField(null=True)

    class Meta:
        db_table = 'sina_us_manager'


class SogouNews(BaseModel):
    content = TextField(null=True)
    contenttitle = TextField(null=True)
    docno = TextField(null=True)
    url = TextField(null=True)

    class Meta:
        db_table = 'sogou_news'


# TODO...del
class SohuDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'sohu_detail_test'


class SohuDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'sohu_detail'


# TODO...del
class TaogubaDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'taoguba_detail_test'


class TaogubaDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'taoguba_detail'


# TODO...del
class TengxunDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        db_table = 'tengxun_detail_test'


class TengxunDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        db_table = 'tengxun_detail'


# TODO...del
class WangyiDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        db_table = 'wangyi_detail_test'


class WangyiDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        db_table = 'wangyi_detail'


# TODO...del
class WeixinDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'weixin_detail_test'


class WeixinDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'weixin_detail'


# TODO...del
class WeixinSourceTest(BaseModel):
    is_enable = CharField(null=True)
    source = IntegerField(db_column='source_id', null=True)
    update_status = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)
    wx_avatar = CharField(null=True)
    wx_name = CharField(null=True)
    wx_url = CharField(null=True)

    class Meta:
        db_table = 'weixin_source_test'


class WeixinSource(BaseModel):
    is_enable = CharField(null=True)
    source = IntegerField(db_column='source_id', null=True)
    update_status = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)
    wx_avatar = CharField(null=True)
    wx_name = CharField(null=True)
    wx_url = CharField(null=True)

    class Meta:
        db_table = 'weixin_source'


# TODO...del
class XueqiuDetailTest(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'xueqiu_detail_test'


class XueqiuDetail(BaseModel):
    content_html = TextField(null=True)
    content_txt = TextField(null=True)
    hash_code = CharField(null=True)
    info_type = IntegerField(null=True)
    post_date = DateTimeField(null=True)
    post_user = CharField(null=True)
    source_url = CharField(null=True)
    src_account = IntegerField(db_column='src_account_id', null=True)
    src_channel = CharField(null=True)
    src_ref = CharField(null=True)
    src_source = IntegerField(db_column='src_source_id', null=True)
    styles = TextField(null=True)
    sub_channel = CharField(null=True)
    tags = CharField(null=True)
    title = CharField(null=True)
    update_time = DateTimeField(null=True)
    wx_account = CharField(null=True)

    class Meta:
        db_table = 'xueqiu_detail'
