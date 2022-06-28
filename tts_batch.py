#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from aip import AipSpeech

AppID = '11378601'
APPKEY = "5KuYlT9jzIgnPGv3jw05rrRT"
APPSECRET = "ONIQz4BT783zkxcLOEFS74VSZZOoDyqE"

client = AipSpeech(AppID,APPKEY,APPSECRET)
text = sys.argv[1]
fname = sys.argv[2] + ".wav"

# 发音人列表：
# speaker(基础音库) 度小美=0,度小宇=1,度逍遥(基础)=3,度丫丫=4
# speaker(精品音库) 度逍遥(精品)=5003,度小鹿=5118,度博文=106,度小童=110,度小萌=111,度米朵=103,度小娇=5

SPEAKER = 0    # 发音人选择
SPEED = 5      # Speed, 0 ~ 15; 语速,取值0-9,默认为5中语速
PITCH = 5      # Pitch, 0 ~ 15; 音调,取值0-9,默认为5中语调
VOLUME = 8     # Volume, 0 ~ 9; 音量,取值0-9,默认为5中音量
AUE = 6        # Aue,下载音频的格式 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav

if __name__ == "__main__":
    data = client.synthesis(text,'zh', 1, {'per':SPEAKER, 'spd':SPEED, 'pit':PITCH, 'vol':VOLUME,})
    if not isinstance(data, dict):
        print(fname + "  <----  " + text)
        fp = open(fname, 'wb')
        fp.write(data)
        fp.close()
