from flask import Flask, request, abort
import time
import urllib.request

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('BDI6ylS9MznYiQN5NYMpon16tmO26AqIXJllRdUQnRl1aO7Rhb8B4j7r6GqtaJcbk9NKTJ7cTX/20TfzxhM98V/Stw9Jwv96VhGfnfeE23uswO0jkaP7fhLhiGH5tuIsHnWFg58LWScFoB3cy4DoKwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b22403a4e09be637b37ebcc7fc3325d3')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    id = event.source.userd
    if '開始使用選才機器人' in msg:
        message = TextSendMessage(text='ID:'+str(id)+'%0D%0A使用說明：%0D%0A請輸入您的科系(含組)全名')
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        fName = 'text.txt'
        if os.path.exists(fName):
            f = open(fName,'a')
            f.write('/n'+str(time.time()))
            f.close()
            file1 = open(fName,'r')
            out = file1.read()
            message = TextSendMessage(text=out)
        else:
            f = open(fName,'w')
            f.write(str(time.time()))
            f.close()
            file1 = open(fName,'r')
            out = file1.read()
            message = TextSendMessage(text=out)
        #message = TextSendMessage(text=f)file.read().decode("utf-8"))
        
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
