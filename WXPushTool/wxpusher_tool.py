# -*- coding: UTF-8 -*-
# @Time    : 2021/12/21 19:52
# @Author  : Hui-Shao


import json
import traceback
import time
import logging
from datetime import datetime
import requests

logging.basicConfig(level=logging.INFO)


class WxPusherTool:
    @staticmethod
    def send_wxmsg(_app_token: str, _type: int, _content: str, _summary: str = "", _uids=None, _topic_ids=None,
                   _origin_url: str = ""):
        """
        Args:
            _app_token: (str) "AT_xxx"
            _type: (int) 内容类型 1 表示文字  2 表示html(只发送body标签内部的数据即可，不包括body标签) 3 表示markdown
            _content: (str) 正文内容
            _summary: (str)消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
            _uids: (list-str) 发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。"UID_xxxx"
            _topic_ids: (list-str) 发送目标的topicId，是一个数组，也就是群发，使用uids单发的时候， 可以不传。
            _origin_url: (str) 原文链接(可选)
        """
        if _uids is None:
            _uids = []
        if len(_app_token) <= 5:
            return 1
        url_postmsg = "https://wxpusher.zjiecode.com/api/send/message"
        hea = {
            "Content-Type": "application/json"
        }
        data = {
            "appToken": str(_app_token),
            "content": str(_content),
            "summary": str(_summary),
            "contentType": int(_type),
            "topicIds": _topic_ids,
            "uids": _uids,
            "url": _origin_url
        }
        retry_n = 1
        while 1:
            if retry_n > 5:
                logging.error("\n达到最大重试次数, 退出")
                break
            try:
                res = requests.post(url=url_postmsg, json=data, headers=hea)  # 注: 不可用 data=data
            except requests.exceptions.SSLError:
                logging.error("SSL 错误, 2s后重试 -> SSLError: An SSL error occurred.")
                time.sleep(2)
            except requests.exceptions.ConnectTimeout:
                logging.error(
                    "建立连接超时, 5s后重试 -> ConnectTimeout: The request timed out while trying to connect to the remote server.")
                time.sleep(5)
            except requests.exceptions.ReadTimeout:
                logging.error(
                    "读取数据超时, 3s后重试 -> ReadTimeout: The server did not send any data in the allotted amount of time.")
                time.sleep(3)
            except requests.exceptions.ConnectionError:
                logging.error(f"{traceback.format_exc(3)}")
                logging.error("建立连接错误, 5s后重试")
                time.sleep(5)
            except requests.exceptions.RequestException:
                logging.error(f"{traceback.format_exc(3)}")
                logging.error("其他网络连接错误, 5s后重试")
                time.sleep(5)
            except KeyboardInterrupt:
                logging.warning("捕获到 KeyboardInterrupt, 退出")
                return False
            except Exception as e:
                sign = '=' * 60 + '\n'
                print(f'{sign}>>> Time: \t{datetime.now()}\n>>> "Detail": \t{e}')
                print(f'{sign}{traceback.format_exc()}{sign}')
            else:
                if res.text:
                    msg_back = json.loads(res.text)
                    if msg_back["success"]:
                        print("[WxPusher] 消息推送成功！")
                        return True
                    else:
                        print("[WxPusher] 消息推送可能失败 返回值：%s" % (msg_back["msg"]))
                        return False
                else:
                    print("[WxPusher] 消息推送失败 res.text 为空!")
                    return False
            finally:
                retry_n += 1
