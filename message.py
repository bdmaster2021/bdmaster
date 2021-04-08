#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import os


def gender_message(id):
    message = TextSendMessage(text='性別Error')
    
    majorIndex = ''
    if os.path.exists(id+'.txt'):
        f = open(id+'.txt','r')
        majorIndex = f.read()
        f.close
    else:
        message = TextSendMessage(text='請先輸入校系')
        
    path = 'https://raw.githubusercontent.com/bdmaster2021/bdmaster/main/gender/gender_'
    message = ImageSendMessage(original_content_url=path + majorIndex +'.png',
                               preview_image_url=path + majorIndex +'.png')
    return message

def area_message(id):
    message = TextSendMessage(text='區域Error')
    
    majorIndex = ''
    if os.path.exists(id+'.txt'):
        f = open(id+'.txt','r')
        majorIndex = f.read()
        f.close
    else:
        message = TextSendMessage(text='請先輸入校系')
        
    path = 'https://raw.githubusercontent.com/bdmaster2021/bdmaster/main/area/area_'
    message = ImageSendMessage(original_content_url=path + majorIndex +'.png',
                               preview_image_url=path + majorIndex +'.png')
    return message

def majorsCom_message(id):
    message = TextSendMessage(text='競爭友校Error')
    
    majorIndex = ''
    if os.path.exists(id+'.txt'):
        f = open(id+'.txt','r')
        majorIndex = f.read()
        f.close
    else:
        message = TextSendMessage(text='請先輸入校系')
    
    path = 'majorsCompetition.txt'
    f = open(path,'r',encoding = 'utf-8-sig')
    data = f.read().split(',')
    indexTemp = data.index(majorIndex)
    msg = '\n1.'+data[indexTemp+1]+'\n2.'+data[indexTemp+2]+'\n3.'+data[indexTemp+3]+'\n4.'+data[indexTemp+4]+'\n5.'+data[indexTemp+5]
    #message = TextSendMessage(text=msg)
    f.close
    return msg

#ImagemapSendMessage(組圖訊息)
def imagemap_message(majorIndex):
    message = ImagemapSendMessage(
        #base_url="https://raw.githubusercontent.com/bdmaster2021/bdmaster/main/MainUI.png",
        #base_url="https://imgur.com/kCGImJt.png",
        base_url="https://imgur.com/GaoLS7r.png",
        alt_text='主選單開啟',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            MessageImagemapAction(
                #性別
                #text='性別'+'_'+majorIndex,
                text='性別',
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            MessageImagemapAction(
                #區域
                #text='區域'+'_'+majorIndex,
                text='區域',
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            MessageImagemapAction(
                #競爭友校
                #text='競爭友校'+'_'+majorIndex,
                text='競爭友校',
                area=ImagemapArea(
                    x=0, y=1000, width=2000, height=1000
                )
            ),
        ]
    )
    return message
'''
#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='金門',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message
'''
#關於LINEBOT聊天內容範例
