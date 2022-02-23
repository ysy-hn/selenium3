import unittest
import yagmail
from time import *
from HTMLTestRunner import HTMLTestRunner


# 把测试报告作为附件发送到指定邮箱
def send_mail(report):
    yag = yagmail.SMTP(user = 'sender@126.com',
                       password = 'a123456',
                       host = 'smtp.126.com')
    subject = "主题， 自动化测试报告"
    contents = '正文， 请查看附件'
    yag.send('receiver@126.com', subject, contents, report)
    print('邮件发送成功')


if __name__ == '__main__':
    # 定义测试用例的目录为当前目录中的test_case/目录
    test_dir = './test_code'
    suits = unittest.defaultTestLoader.discover(test_dir, pattern = 'test*.py')
    # 获取当前日期与时间
    now_time = strftime("%Y_%m_%d %H:%M:%S")
    html_report = './test_report/' + now_time +'result.html'
    fp = open(html_report, 'wb')
    # 调用HTMLTestRunner， 运行测试用例
    runner = HTMLTestRunner(stream = fp,
                            title = "百度搜索测试报告",
                            description = "运行环境：Windows 10， Chrome浏览器"
                            )
    runner.run(suits)
    fp.close()
    send_mail(html_report)  # 发送报告



