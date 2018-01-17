# -*- coding: utf-8 -*-

from trivest_spider import execute_sql


def getPageDetail(tableName, news_id):
    sql = (u"select a.post_user, a.src_ref, a.tags, a.post_date, a.source_url, a.title, a.content_html, b.styles from "
           u"%s a left JOIN all_styles b on a.style_hash "
           u"= b.hash_code "
           u"where a.id=%s" % (tableName, news_id))
    result = execute_sql(sql)
    if result.rowcount:
        return result._rows[0]
    else:
        return None


def getLastPageDetail(tableName):
    sql = (u"select a.post_user, a.src_ref, a.tags, a.post_date, a.source_url, a.title, a.content_html, "
           u"b.styles from %s a left JOIN all_styles b on a.style_hash "
           u"= b.hash_code "
           u"order by a.update_time desc limit 0,1" % (tableName,))
    result = execute_sql(sql)
    if result.rowcount:
        return result._rows[0]
    else:
        return None


