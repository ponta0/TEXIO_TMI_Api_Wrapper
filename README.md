# TEXIO TMI_Apiラッパー

PythonからTEXIOの電源を制御するためのラッパーです。
使用するためには[TEXIOが提供するドライバとライブラリ](https://www.texio.co.jp/uploads/PWA_Dr_API310B.zip)が必要です。

使用例 (example.py)
```python
import time
from TMI_Api import TMI_Api

api = TMI_Api()

delay = 1

print("電源に接続します")
dev_hID = api.TMI_HandleOpen("PW-A", "USB:1:1")
print(f"hID: {dev_hID}")
time.sleep(delay)

if dev_hID > 0:
    #print(f"hID: {dev_hID}")
    ret, name = api.TMI_ModelNameQ(dev_hID)
    print(f"ret: {ret}")
    print(f"Model: {name}")
    time.sleep(delay)

    ret, data = api.TMI_AllPresetQ(dev_hID)
    print(list(data))

    time.sleep(delay)
    ret = api.TMI_HandleClose(dev_hID)
    print(f"ret: {ret}")
    print("電源との通信を切断しました")
else:
    print(f"エラーコード: {dev_hID}")
```