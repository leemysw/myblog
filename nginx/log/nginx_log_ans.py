#!/usr/lib/python

import re
import os
import time
from urllib.request import urlopen

import pymysql

"""查询ip地址归属地"""
while True:

    def addrs(ip):
        # 尝试打开url查询ip所属地
        try:
            url = urlopen('http://wap.ip138.com/ip.asp?ip=%s' % ip)
            html = url.read()
            html = html.decode('utf-8')
            r = re.compile(r"<br/><b>查询结果：(.*)</b><br/>")
            result = r.findall(html)
            return result

        # 出现异常 写入错误日志，ip所属地返回"Not found"
        except:
            result = "Not found"

            """ 写入错误日志 """
            with open("/lee/nginx/log/get_adr_log.txt", "a") as e_log:
                e_log.write(time.strftime('%Y-%m-%d %H:%M') + " - _ -! " + "can't open url" + '\n')
            return result


    def ans_log(file_dir):
        ips = []
        datas = []
        ip_count = []

        with open(file_dir) as log:
            for line in log:
                ip = line.split()[0]
                day = line.split()[3][1:-9].replace('/', '-')
                time = line.split()[3][-8:-3].replace('/', '-')
                # byte = line.split()[9]

                if ip:
                    ips.append(ip)
                    datas.append([ip, day + ' ' + time])

        ip_set = set(ips)
        for ip in ip_set:
            ip_count.append([ip, ips.count(ip)])

        uv_today = len(ip_set)
        pv_today = len(datas)

        # if uv_today > 15:
        #     ip_count = sorted(ip_count, key=lambda x: x[1], reverse=True)[0:15]
        # else:
        #     ip_count = sorted(ip_count, key=lambda x: x[1], reverse=True)[0:uv_today]

        ip_count = sorted(ip_count, key=lambda x: x[1])

        for m in range(0, len(ip_count)):
            for i in range(0, len(datas)):
                if ip_count[m][0] == datas[i][0]:
                    ip_count[m].append(datas[i][1])
                    break

        for m in range(0, len(ip_count)):
            ip_count[m].append(addrs(ip_count[m][0]))

        print(ip_count)

        return pv_today, uv_today, ip_count


    try:
        pv_today, uv_today, list = ans_log('/lee/nginx/log/access.log')
        flag = pv_today
    except:
        print("日志文件出错")
        flag = 0
        with open("/lee/nginx/log/get_adr_log.txt", "a") as e_log:
            e_log.write(time.strftime('%Y-%m-%d %H:%M') + " - _ -! " + "can't open log file" + '\n')

    if flag != 0:
        connect = pymysql.connect(host='47.96.93.129',
                                  port=3306,
                                  user='lee',
                                  password='9557ywwd',
                                  db='myweb',
                                  charset='utf8')
        cur = connect.cursor()

        sql1 = """SELECT PV, UV FROM blog_view """
        cur.execute(sql1)
        result = cur.fetchall()
        pv_all = int(result[-1][0]) + int(pv_today)
        uv_all = int(result[-1][1]) + int(uv_today)
        # sql2 = """TRUNCATE TABLE blog_view"""
        # cur.execute(sql2)
        for i in range(0, len(list)):
            data = list[i] + [pv_all, uv_all]
            sql3 = """INSERT INTO blog_view(IP, IP_COUNT, VIEW_TIME, IP_ADDRESS, PV, UV)
                      VALUE (%s, %s, %s, %s, %s, %s);"""
            cur.execute(sql3, data)
            print('all is ok')

        connect.commit()
        connect.close()

    os.system('rm -f /lee/nginx/log/access.log')
    os.system('touch /lee/nginx/log/access.log')
    os.system("/usr/bin/docker exec -i lee_nginx_1 /bin/bash -c 'kill -USR1 $(cat /var/run/nginx.pid)'")
    time.sleep(1800)