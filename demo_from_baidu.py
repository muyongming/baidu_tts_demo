# coding=utf-8

import sys
import json

# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode

# 发音人列表：
# speaker(基础音库) 度小美=0,度小宇=1,度逍遥(基础)=3,度丫丫=4
# speaker(精品音库) 度逍遥(精品)=5003,度小鹿=5118,度博文=106,度小童=110,度小萌=111,度米朵=103,度小娇=5

SPEAKER = 4    # 发音人选择
SPEED = 5      # Speed, 0 ~ 15; 语速,取值0-9,默认为5中语速
PITCH = 5      # Pitch, 0 ~ 15; 音调,取值0-9,默认为5中语调
VOLUME = 8     # Volume, 0 ~ 9; 音量,取值0-9,默认为5中音量
AUE = 6        # Aue,下载音频的格式 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav

API_KEY = 'nu9r2plGFi3s1ugayDPSM6Mk'
SECRET_KEY = 'G62YGnq84eKTqu0mBgvdpmC6gNBzHdai'

TTS_URL = 'http://tsn.baidu.com/text2audio'

"""  TOKEN start """
TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'

"""
    获取token
"""
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    if (IS_PY3):
        result_str = result_str.decode()

    result = json.loads(result_str)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'audio_tts_post' in result['scope'].split(' '):
            print ('please ensure has check the tts ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()


"""  TOKEN end """
if __name__ == '__main__':
    # 默认示例内容：
    TEXT = u"三分钟前,由北京市顺义区二经路与二纬路交汇处北侧,北京首都国际机场T3航站楼去往东城区北三环东路36号喜来登大酒店(北京金隅店)"
    FILENAME = u"大姚的订单信息.mp3"

    if (len(sys.argv) < 3):
        print(u'usage: python demo.py [text] [filename]')
        print(u'example: python demo.py 三分钟前,由北京市顺义区二经路与二纬路交汇处北侧,北京首都国际机场T3航站楼去往东城区北三环东路36号喜来登大酒店(北京金隅店) 大姚的订单信息.mp3')
    else :
        TEXT = sys.argv[1]
        FILENAME = sys.argv[2]

    token = fetch_token()
    tex = quote_plus(TEXT)  # 此处TEXT需要两次urlencode
    params = {'tok': token, 'tex': tex, 'cuid': "quickstart",
              'lan': 'zh', 'ctp': 1, 'per':SPEAKER, 'spd':SPEED, 'pit':PITCH, 'vol':VOLUME}  # lan ctp 固定参数

    data = urlencode(params)
    req = Request(TTS_URL, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()

        headers = dict((name.lower(), value) for name, value in f.headers.items())

        has_error = ('content-type' not in headers.keys() or headers['content-type'].find('audio/') < 0)
    except  URLError as err:
        print('http response http code : ' + str(err.code))
        result_str = err.read()
        has_error = True

    save_file = "error.txt" if has_error else (FILENAME)

    with open(save_file, 'wb') as of:
        of.write(result_str)

    if has_error:
        if (IS_PY3):
            result_str = str(result_str, 'utf-8')
        print("tts api  error:" + result_str)

    print("file saved as : " + save_file)
