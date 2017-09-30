# -*- coding: utf-8 -*-
from trivest_spider import ScrapyLog
import util.loggerutils as loggerUtil
import logging

'''
  scrapy_log
      id
      info 具体内容
      level 级别：info warn
      save_time 时间
      belong_to 所属模块
      attach 附加信息
  '''

def queryAll():
    return ScrapyLog.select()


def queryPart(belong_to):
    return ScrapyLog.select().where(ScrapyLog.belong_to == belong_to)


def logShow(msg, level='info', belong_to='', attach='', saveInDB=False):
    logging.basicConfig(level=(logging.INFO if level == 'info' else logging.WARN))
    logger = loggerUtil.bas_console_logger('logger')
    belong_to = (belong_to+':') if belong_to else ''
    logger.info(belong_to + msg)

def warn(msg, belong_to='', attach='', saveInDB=False):
    logShow(msg, level='warn', belong_to=belong_to, attach=attach, saveInDB=saveInDB)


def info(msg, belong_to='', attach='', saveInDB=False):
    logShow(msg, level='info', belong_to=belong_to, attach=attach, saveInDB=saveInDB)

if __name__ == '__main__':
    warn('1111')
    info('222')