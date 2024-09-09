from flask import Flask, jsonify, request
import logging
import random
import string

app = Flask(__name__)

# 设置日志记录
logging.basicConfig(level=logging.INFO)


@app.before_request
def log_request_info():
    # 记录请求方法、URL 和参数
    logging.info('Request Method: %s', request.method)
    logging.info('Request URL: %s', request.url)
    logging.info('Request Args: %s', request.args)

    # 记录请求头
    logging.info('Request Headers: %s', dict(request.headers))

    # 记录请求体（如果有的话）
    if request.method in ['POST', 'PUT']:
        logging.info('Request Body: %s', request.get_data(as_text=True))


@app.route('/get/text', methods=['GET'])
def get_text():
    # 检查请求中的 forge_flag 字段
    forge_flag = request.args.get('forge_flag', 'false').lower() == 'true'

    # 打印 forge_flag 的值
    logging.info('forge_flag: %s', forge_flag)

    if forge_flag:
        # 生成随机字符串
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(20, 100)))
        return random_string
    else:
        # 正常的响应数据
        data = {
            "success": True,
            "code": 10000,
            "message": "获取成功",
            "data": [
                {
                    "id": "1832970636837150720",
                    "title": "Android加载大图片，解决OOM问题",
                    "viewCount": 262,
                    "commentCount": 69,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    # "cover": "/imgs/3.png"
                },
                {
                    "id": "1832970636837150721",
                    "title": "Volley/Xutils对大图片处理算法源码分析",
                    "viewCount": 164,
                    "commentCount": 62,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/3.png"
                },
                {
                    "id": "1832970636837150722",
                    "title": "Android开发网络安全配置",
                    "viewCount": 120,
                    "commentCount": 92,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/16.png"
                },
                {
                    "id": "1832970636837150723",
                    "title": "Android开发网络编程，请求图片",
                    "viewCount": 35,
                    "commentCount": 39,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/9.png"
                },
                {
                    "id": "1832970636837150724",
                    "title": "Intent页面跳转工具类分享",
                    "viewCount": 270,
                    "commentCount": 96,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/14.png"
                },
                {
                    "id": "1832970636837150725",
                    "title": "阳光沙滩商城的API文档",
                    "viewCount": 230,
                    "commentCount": 11,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/9.png"
                },
                {
                    "id": "1832970636837150726",
                    "title": "Android课程视频打包下载",
                    "viewCount": 319,
                    "commentCount": 78,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/16.png"
                },
                {
                    "id": "1832970636837150727",
                    "title": "非常轻量级的gif录制软件",
                    "viewCount": 276,
                    "commentCount": 40,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/11.png"
                },
                {
                    "id": "1832970636837150728",
                    "title": "Fiddler抓包工具，墙裂推荐，功能很强大很全的一个工具",
                    "viewCount": 325,
                    "commentCount": 84,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/7.png"
                },
                {
                    "id": "1832970636837150729",
                    "title": "AndroidStudio奇淫技巧-代码管理",
                    "viewCount": 185,
                    "commentCount": 10,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/14.png"
                },
                {
                    "id": "1832970636837150730",
                    "title": "OC和Swift混编",
                    "viewCount": 106,
                    "commentCount": 108,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/10.png"
                },
                {
                    "id": "1832970636837150731",
                    "title": "最新的Android studio是不是没有Android Device Monitor",
                    "viewCount": 235,
                    "commentCount": 90,
                    "publishTime": "2024-09-09T02:33:49.426+0000",
                    "userName": "Foursuns",
                    "cover": "/imgs/7.png"
                }
            ]
        }
        return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4202)
