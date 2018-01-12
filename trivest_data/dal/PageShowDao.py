# -*- coding: utf-8 -*-

from trivest_spider import execute_sql


def getPageDetail(tableName, news_id):
    sql = (u"select a.title, a.content_html, b.styles from %s a left JOIN all_styles b on a.style_hash = b.hash_code "
           u"where a.id=%s" % (tableName, news_id))
    result = execute_sql(sql)
    if result.rowcount:
        return result._rows[0]
    else:
        return u"", u"未找到%s相关页面" % news_id, u""