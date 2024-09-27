# -*- coding: utf-8 -*-
from openai import OpenAI
import paho.mqtt.client as mqtt
import paho.mqtt.client as paho
import time
broker = "broker.hivemq.com"
client = ''
NAME = 'unit5'
client = paho.Client(NAME)
client.connect(broker)
client.loop_start()
client.subscribe("playsub")

api_key = ""

openai_client = OpenAI(api_key=api_key)



messages = []
# with open('test.txt', 'r', encoding='utf-8') as file: #讀取檔案robot_action.txt檔裡的內容
#     text = file.read()    
# messages.append({"role": "user", "content": text})

temp = []#把gpt()回傳的數列的值暫存到這個列表
def gpt(msg):
    messages.append({"role": "user", "content": msg})
    stream = openai_client.chat.completions.create(
        model = "ft:gpt-4o-mini-2024-07-18:personal::A0TsUCVR",
        # model = "ft:gpt-4o-2024-08-06:personal::9z5fU4S9",
        # model="ft:gpt-3.5-turbo-0125:personal::9z4t441Q",
        # messages=[{"role": "system", "content": "你是一個幫我把文字敘述轉成數字的機器人,只會回復我數字,數字的範圍是0到1000,根據情緒愈高低數值就高,反之情緒低弱的話,數值就低,並且根據我給你的文字敘述裡的動作給予相對應的數字"},
        #         {"role": "user", "content": msg}
        # ],
        messages=[{"role": "system", "content": "你是一個幫我把文字敘述轉成數字的機器人,只會回復我數字,數字的範圍是0到1000,根據給予的文字賦予id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12,id13,id14,id15,id16數字,id1到id8是機器人左邊的個別關節馬達,id9到id16是機器人右邊的個別關節馬達,且左右兩邊是對應關西,id8對應的是id16,id8是左邊控制手臂上下的馬達,id16是控制右邊手臂上下的馬達,id16是手臂愈高數值愈大,最大數值1000也是手臂舉到最高,id8則相反,手臂愈高數值愈小,最小數值為0也是手臂舉到最高,其餘馬達也是對應的關係,id1對應id9這兩個馬達是控制腳底板左右翻轉,id2對應的是id10,id3對應的是id11,id4對應的是id12,id2到id4跟id10到id12這幾個馬達是腳的控制馬達,如果兩邊沒有平衡就會導致機器人跌倒,id5對應的是id13,這兩個馬達基本是不作用的,也就是數值基本上固定,除非要左右滑動,這兩個馬達是讓腳可以向左或向右,id6對應的是id14,id7對應的是id15,id6和id14是控制手臂的左右,id7和id15則是控制手掌的彎曲,如果id1到id16都有賦予相對應的數字了,也就是已經賦予16個數字後,這16個為一個動作,而根據我給予的文字賦予更多連貫動作,也就是先賦予id1到id16一次數字後也就是有16個數值後,再次賦予id1到id16數值,直到該文字的動作完全被體現,16個數值為1組,每段文字所賦予的動作可能有好幾個以16個(id1到id16)的動作合併的,也會根據情緒高低影響數字幅度。"},
                {"role": "user", "content": msg}
        ],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            temp.append(chunk.choices[0].delta.content)
    full_text = ''.join(temp)
    return full_text #回傳數值

def split_number(num):
    index = 0
    check = 0
    temp_ = []
    for x in range(len(num)):
        if num[x] == ",":
            temp_.append(int(num[index:x]))
            check += 1
            index = x + 1
        if check == 16:
            result.append(temp_)
            temp_ = []
            check = 0
result = [] #要放入.d6a的數列表
while True:
    msg = input("請輸入:")
    if msg.lower() == "q":
        client.publish("playsub", msg)
        time.sleep(2)
        break
    elif msg == "歷史":
        print(messages)
    else:
        num = gpt(msg)
        client.publish("playsub", num)
        temp = []

    