from flask import Flask, request, abort
import time
import urllib.request
from linebot.models import *

from flask import render_template

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

majors = ['012','新聞學系','新聞系',
          '022','廣播電視電影學系廣播組','廣電系廣播組',
          '032','廣播電視電影學系電視組','廣電系電視組',
          '042','廣播電視電影學系電影組','廣電系電影組',
          '052','圖文傳播暨數位出版學系','圖傳系',
          '062','公共關係暨廣告學系','公廣系',
          '072','口語傳播暨社群媒體學系','口傳系',
          '082','資訊傳播學系','資傳系',
          '092','數位多媒體設計學系動畫設計組','數媒系動畫組',
          '102','數位多媒體設計學系遊戲設計組','數媒系遊戲組',
          '112','傳播管理學系','傳管系',
          '122','資訊管理學系資訊管理組','資訊管理系資訊管理組','資訊管理系資管組','資管系資管組',
          '132','資訊管理學系資訊科技組','資訊管理系資訊科技組','資訊管理系資科組','資管系資科組',
          '142','資訊管理學系網路科技組','資訊管理系網路科技組','資訊管理系網科組','資管系網科組','資訊管理學系智慧網路應用組',
          '152','財務金融學系','財金系',
          '162','行政管理學系','行管系',
          '172','觀光學系餐旅經營管理組','觀光系餐旅組',
          '182','觀光學系旅遊暨休閒事業管理組','觀光系旅遊組',
          '192','觀光學系觀光規劃暨資源管理組','觀光系觀規組','觀光系規劃組',
          '202','經濟學系','經濟系',
          '212','企業管理學系','企管系',
          '222','社會心理學系','社心系',
          '232','英語暨傳播應用學系','英語系',
          '242','中國文學系','中文系',
          '252','日本語文學系','日文系',
          '262','法律學系','法律系']

majorIndex = '99'
majorTemp = ''
majorList = []
messageString = ''

@app.route("/")
def home():
    return render_template("home.html")

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
    id = event.source.user_id
    majorList = []
    majorIndex = '99'
    majorTemp = ''
    if '選才主選單' in msg:
        if os.path.exists(str(id)+'.txt'):
            f = open(str(id)+'.txt','r')
            message = imagemap_message(f.read())
            f.close
        else:
            message = TextSendMessage(text='請先輸入校系')
        line_bot_api.reply_message(event.reply_token, message)
    elif '開始使用選才機器人' in msg:
        message = TextSendMessage(text=str(id)+'\n使用說明：\n請輸入您的科系(含組)全名\n例：資訊管理學系資訊管理組')
        line_bot_api.reply_message(event.reply_token, message)
    elif '系' in msg:
        for i in range(len(majors)):
            if majors[i].isdigit():
                majorTemp = majors[i]
                majorList = []
                for j in range(i+1,len(majors)):
                    if majors[j].isdigit() == False:
                        majorList.append(majors[j])
                    else:
                        break
            elif msg == majors[i]:
                majorIndex = majorTemp
                f = open(str(id)+'.txt','w')
                f.write(majorIndex)
                f.close
                messageString = '您的科系為：\n「'+msg +'」\n\n也可輸入為：'
                for k in majorList:
                    messageString += '\n' + k
                #message = TextSendMessage(text=messageString)
                #message = TextSendMessage(text='選才主選單')
                
                f = open(str(id)+'.txt','r')
                message = imagemap_message(f.read())
                f.close
                break
            else:
                message = TextSendMessage(text='請重新輸入校系')
        
        line_bot_api.reply_message(event.reply_token, message)
    '''
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    '''
    elif '性別' in msg:
        if os.path.exists(str(id)+'.txt'):
            f = open(str(id)+'.txt','r')
            message = gender_message('gender_'+f.read())
            f.close
        else:
            message = TextSendMessage(text='請先輸入校系')
        line_bot_api.reply_message(event.reply_token, message)
    elif '區域' in msg:
        if os.path.exists(str(id)+'.txt'):
            f = open(str(id)+'.txt','r')
            message = area_message('area_'+f.read())
            f.close
        else:
            message = TextSendMessage(text='請先輸入校系')
        line_bot_api.reply_message(event.reply_token, message)
    elif '競爭友校' in msg:
        if os.path.exists(str(id)+'.txt'):
            f = open(str(id)+'.txt','r')
            message = majorsCom_message('majorsCompetition_'+f.read())
            f.close
        else:
            message = TextSendMessage(text='請先輸入校系')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        '''
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
        '''
        message = TextSendMessage(text='無法辨識，請重新輸入。')
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
