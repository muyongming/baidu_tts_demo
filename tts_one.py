#! /usr/bin/python3
# -*- coding: utf-8 -*- 
from aip import AipSpeech

AppID='11378601'
APPKEY="5KuYlT9jzIgnPGv3jw05rrRT"
APPSECRET="ONIQz4BT783zkxcLOEFS74VSZZOoDyqE"

SPEAKER=0	# 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
SPEED=5		# Speed, 0 ~ 15; 语速，取值0-9，默认为5中语速
PITCH=5		# Pitch, 0 ~ 15; 音调，取值0-9，默认为5中语调
VOLUME=8	# Volume, 0 ~ 9; 音量，取值0-9，默认为5中音量
AUE=6		# Aue,下载音频的格式 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav

client = AipSpeech(AppID,APPKEY,APPSECRET)

while True:
    txt = input("请输入文字:\n")
    fname = txt + '.mp3'
    result = client.synthesis(txt,'zh', 1, {'per':SPEAKER, 'spd':SPEED, 'pit':PITCH, 'vol':VOLUME,})
    #result = client.synthesis(txt,'zh',1,{'vol':5, 'per':4,})
    if txt != '':
        if not isinstance(result, dict):
            print("文件名："+fname)
            with open(fname, 'wb') as fp:
                fp.write(result)
                fd.close()
