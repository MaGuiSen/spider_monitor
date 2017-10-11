# -*- coding: utf-8 -*-
import logging
import random
import time

import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# 参考网站：http://www.cnblogs.com/xcblogs-python/p/5727238.html
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr

from trivest_data.dal.DataMonitorDao import SpiderMonitor

# 为了处理：No handlers could be found for logger “apscheduler.scheduler”
logging.basicConfig()

my_sender = 'maguisen@163.com'  # 发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user = '1059876295@qq.com'  # 收件人邮箱账号，为了后面易于维护，所以写成了变量


def mail(info):
    ret = True
    try:
        msg = MIMEText(info, 'plain', 'utf-8')
        msg['From'] = formataddr(["maguisen", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["我的天", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "心跳出问题"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, "Ma123456")  # 括号中对应的是发件人邮箱账号、邮箱密码（授权码）
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 这句是关闭连接的意思
    except Exception as e:  # 如果try中的语句没有执行，则会执行下面的ret=False
        ret = False
        print e
    return ret

lastSendTime = 0l


def checkNeedSend():
    # 如果在晚上12点到早上6点不爬
    hour = datetime.datetime.now().hour
    if 0 <= hour <= 6:
        return False

    currTime = int(time.time())
    global lastSendTime
    if currTime - lastSendTime > 30 * 60:
        return True
    else:
        return False


def outOfData(currTime, beatTime_long, timeSpace):
    spaceTime = currTime - beatTime_long
    if spaceTime.seconds > (timeSpace + 4*60):
        return True
    else:
        return False


def heartBeat():
    # 心跳
    results = SpiderMonitor().getHeartBeatTime()
    print 'check....'
    needSendTypes = []
    currTime = datetime.datetime.now()
    print 'now: ', currTime
    for result in results:
        timeSpace = result.heart_beat_time_space
        beatTime = result.heart_beat_time
        projectIdentify = result.project_identify
        spiderName = result.spider_name
        spiderNameZh = result.spider_name_zh

        print 'that: ', beatTime, timeSpace, spiderName
        if beatTime and outOfData(currTime, beatTime, timeSpace):
            print 'outOfData--------', timeSpace, beatTime, projectIdentify, spiderName, spiderNameZh
            needSendTypes.append((timeSpace, beatTime, projectIdentify, spiderName, spiderNameZh))

    if len(needSendTypes) and checkNeedSend():
        print '-------need send email---------'
        types = []
        for needSendType in needSendTypes:
            timeSpace, beatTime, projectIdentify, spiderName, spiderNameZh = needSendType
            sb = []
            sb.append(str(timeSpace))
            sb.append(str(beatTime))
            if projectIdentify:
                sb.append(projectIdentify)
            if spiderName:
                sb.append(spiderName)
            if spiderNameZh:
                sb.append(spiderNameZh)
            types.append(u'， '.join(sb))
        randomStr = str(random.uniform(0, 1))
        ret = mail(randomStr + ':\n' + '\n\n'.join(types))
        for timeSpace, beatTime, projectIdentify, spiderName, spiderNameZh in needSendTypes:
            print timeSpace, beatTime, projectIdentify, spiderName, spiderNameZh
        if ret:
            print 'send_success'
            global lastSendTime
            lastSendTime = int(time.time())


def startMailMonitor():
    heartTime = 3*60   # 心跳跳动时间间隔 3分钟
    scheduler = BlockingScheduler(daemonic=False)
    scheduler.add_job(heartBeat, 'interval', seconds=heartTime,
                      next_run_time=datetime.datetime.now(),
                      start_date=datetime.datetime.now() + datetime.timedelta(seconds=5))
    scheduler.start()

if __name__ == '__main__':
    startMailMonitor()
    # heartBeat()

