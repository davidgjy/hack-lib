import pymysql
import smtplib  
import traceback
from email.mime.text import MIMEText

import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  

def sendMail(body):
    sender = 'yxc_robot@163.com'  
    receiver = 'linlg@yxcat.com.cn'  
    subject = '易养护订单提醒'  
    smtpserver = 'smtp.163.com'  
    username = 'yxc_robot'  
    password = 'yxc791214'  
    
    msg = MIMEText(body,'plain','utf-8') #中文需参数‘utf-8'，单字节字符不需要  
    msg['Subject'] = Header(subject, 'utf-8')  
    msg['From'] = 'Robot<yxc_robot@163.com>'    
    msg['To'] = "gujy@dadi18.com"  
    smtp = smtplib.SMTP()  
    smtp.connect('smtp.163.com')  
    smtp.login(username, password)  
    smtp.sendmail(sender, receiver, msg.as_string())  
    smtp.quit()  

conn = pymysql.connect(host='localhost', user='root', passwd='mysql', db='repairtstdb', port=3306, charset='utf8')
cur = conn.cursor()

sql = "select tp.id, o.order_no, o.merch_day \
from t_repair_order o inner join temp_yyh_order_need_notify_2017 tp \
on o.order_no = tp.order_no and o.status = 4 and tp.flag <> 1"

cur = conn.cursor()
cur.execute(sql)
alldata = cur.fetchall()
mailBody = ""
separator = "----------------------------------------------\n"
for rec in alldata:
    tempOrdId = rec[0]
    orderNo = rec[1]
    merchDay = rec[2]
    line = "订单号: %s \t 到店时间: %s \n" % (orderNo, merchDay)
    mailBody = mailBody + line + separator
    
    #sql = "update temp_yyh_order_need_notify_2017 set flag = 1 where id = %s"
    #cur.execute(sql, (tempOrdId))
    #cur.connection.commit()
    #print("Temp Id: %s  Order No: %s has been scaned and flag updated!" % (tempOrdId, orderNo))

print(mailBody)
sendMail(mailBody)



