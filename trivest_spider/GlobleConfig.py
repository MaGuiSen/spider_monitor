# -*- coding: utf-8 -*-
# 项目唯一标识，分布式，不同的项目思考(规则：项目名称!@项目部署位置!@部署时间!@ 1000-9999的随机数）
projectIdentify = 'news spider!@xiamen!@2017-9-30 15:59!@7699'

# key为spider的名称 此配置和数据库：spider_monitor字段一致
spiderDetails = {
    'diyicaijing_news': {
        'table_name': 'diyicaijing_detail',
        'table_name_zh': u'第一财经',
        'spider_name': 'diyicaijing_news',
        'spider_name_zh': u'第一财经新闻'
    },
    'fenghuang_finance_bond_news': {
        'table_name': 'fenghuang_detail',
        'table_name_zh': u'凤凰',
        'spider_name': 'fenghuang_finance_bond_news',
        'spider_name_zh': u'凤凰金融-证券'
    },
    'fenghuang_finance_quoted_company': {
        'table_name': 'fenghuang_detail',
        'table_name_zh': u'凤凰',
        'spider_name': 'fenghuang_finance_quoted_company',
        'spider_name_zh': u'凤凰-财经-上市公司'
    },
    'fenghuang_game_e_sports': {
        'table_name': 'fenghuang_detail',
        'table_name_zh': u'凤凰',
        'spider_name': 'fenghuang_game_e_sports',
        'spider_name_zh': u'凤凰-游戏-点子竞技'
    },
    'fenghuang_game_hot_news': {
        'table_name': 'fenghuang_detail',
        'table_name_zh': u'凤凰',
        'spider_name': 'fenghuang_game_hot_news',
        'spider_name_zh': u'凤凰-游戏-热点新闻'
    },
    'fenghuang_game_product_news': {
        'table_name': 'fenghuang_detail',
        'table_name_zh': u'凤凰',
        'spider_name': 'fenghuang_game_product_news',
        'spider_name_zh': u'凤凰-游戏-产品咨询'
    },
    'fenghuang_tech_news': {
        'table_name': 'fenghuang_detail',
        'table_name_zh': u'凤凰',
        'spider_name': 'fenghuang_tech_news',
        'spider_name_zh': u'凤凰-科技资讯'
    },
    'hexun_tech_main_news': {
        'table_name': 'hexun_detail',
        'table_name_zh': u'和讯',
        'spider_name': 'hexun_tech_main_news',
        'spider_name_zh': u'和讯-科技要闻'
    },
    'jiemian_news': {
        'table_name': 'jiemian_detail',
        'table_name_zh': u'界面',
        'spider_name': 'jiemian_news',
        'spider_name_zh': u'界面-新闻'
    },
    'jinrongjie_main_news': {
        'table_name': 'jinrongjie_detail',
        'table_name_zh': u'金融界',
        'spider_name': 'jinrongjie_main_news',
        'spider_name_zh': u'金融界-要闻'
    },
    'jinrongjie_quoted_company': {
        'table_name': 'jinrongjie_detail',
        'table_name_zh': u'金融界',
        'spider_name': 'jinrongjie_quoted_company',
        'spider_name_zh': u'金融界-上市公司'
    },
    'kuaixun_quoted_company': {
        'table_name': 'kuaixun_detail',
        'table_name_zh': u'快讯',
        'spider_name': 'kuaixun_quoted_company',
        'spider_name_zh': u'快讯-上市公司'
    },
    'kuaixun_world_live': {
        'table_name': 'kuaixun_detail',
        'table_name_zh': u'快讯',
        'spider_name': 'kuaixun_world_live',
        'spider_name_zh': u'快讯-全球直播'
    },
    'sina_finance_main_news': {
        'table_name': 'sina_detail',
        'table_name_zh': u'新浪',
        'spider_name': 'sina_finance_main_news',
        'spider_name_zh': u'新浪-财经要闻'
    },
    'sina_finance_ssgs_scroll_news': {
        'table_name': 'sina_detail',
        'table_name_zh': u'新浪',
        'spider_name': 'sina_finance_ssgs_scroll_news',
        'spider_name_zh': u'新浪-财经-上市公司'
    },
    'sina_finance_stock_main_news': {
        'table_name': 'sina_detail',
        'table_name_zh': u'新浪',
        'spider_name': 'sina_finance_stock_main_news',
        'spider_name_zh': u'新浪-财经-股票要闻'
    },
    'sina_tech_scroll_news': {
        'table_name': 'sina_detail',
        'table_name_zh': u'新浪',
        'spider_name': 'sina_tech_scroll_news',
        'spider_name_zh': u'新浪-科技新闻'
    },
    'sina_tech_scroll_news_2': {
        'table_name': 'sina_detail',
        'table_name_zh': u'新浪',
        'spider_name': 'sina_tech_scroll_news_2',
        'spider_name_zh': u'新浪-科技新闻-2'
    },
    'sohu_a_stock_hu_shen': {
        'table_name': 'sohu_detail',
        'table_name_zh': u'搜狐',
        'spider_name': 'sohu_a_stock_hu_shen',
        'spider_name_zh': u'搜狐-A股-沪深'
    },
    'sohu_tech_news': {
        'table_name': 'sohu_detail',
        'table_name_zh': u'搜狐',
        'spider_name': 'sohu_tech_news',
        'spider_name_zh': u'搜狐-科技新闻'
    },
    'taoguba_core_post': {
        'table_name': 'taoguba_detail',
        'table_name_zh': u'淘股吧',
        'spider_name': 'taoguba_core_post',
        'spider_name_zh': u'淘股吧-核心推荐'
    },
    'taoguba_day_recommend': {
        'table_name': 'taoguba_detail',
        'table_name_zh': u'淘股吧',
        'spider_name': 'taoguba_day_recommend',
        'spider_name_zh': u'淘股吧-每日推荐'
    },
    'tenxun_finance_main_news': {
        'table_name': 'tenxun_detail',
        'table_name_zh': u'腾讯',
        'spider_name': 'tenxun_finance_main_news',
        'spider_name_zh': u'腾讯-财经要闻'
    },
    'tenxun_stock_main_news': {
        'table_name': 'tenxun_detail',
        'table_name_zh': u'腾讯',
        'spider_name': 'tenxun_stock_main_news',
        'spider_name_zh': u'腾讯-股票要闻'
    },
    'tenxun_stock_quoted_company': {
        'table_name': 'tenxun_detail',
        'table_name_zh': u'腾讯',
        'spider_name': 'tenxun_stock_quoted_company',
        'spider_name_zh': u'腾讯-股票-上市公司'
    },
    'tenxun_tech_scroll_news': {
        'table_name': 'tenxun_detail',
        'table_name_zh': u'腾讯',
        'spider_name': 'tenxun_tech_scroll_news',
        'spider_name_zh': u'腾讯-科技新闻'
    },
    'wangyi_finance_scroll_news': {
        'table_name': 'wangyi_detail',
        'table_name_zh': u'网易',
        'spider_name': 'wangyi_finance_scroll_news',
        'spider_name_zh': u'网易-财经新闻'
    },
    'wangyi_stock_news': {
        'table_name': 'wangyi_detail',
        'table_name_zh': u'网易',
        'spider_name': 'wangyi_stock_news',
        'spider_name_zh': u'网易-股票新闻'
    },
    'wangyi_tech_scroll_news': {
        'table_name': 'wangyi_detail',
        'table_name_zh': u'网易',
        'spider_name': 'wangyi_tech_scroll_news',
        'spider_name_zh': u'网易-科技新闻'
    },
    'weixin_public_article': {
        'table_name': 'weixin_detail',
        'table_name_zh': u'微信',
        'spider_name': 'weixin_public_article',
        'spider_name_zh': u'微信-公众号文章'
    },
    'weixin_source': {
        'table_name': 'weixin_source',
        'table_name_zh': u'微信源',
        'spider_name': 'weixin_source',
        'spider_name_zh': u'微信-源'
    },
    'xueqiu_hu_shen': {
        'table_name': 'xueqiu_detail',
        'table_name_zh': u'雪球',
        'spider_name': 'xueqiu_hu_shen',
        'spider_name_zh': u'雪球沪深'
    },
}


def getSpiderDetail(spiderName):
    return spiderDetails[spiderName]