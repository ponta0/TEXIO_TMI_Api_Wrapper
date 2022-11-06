import time
from TMI_Api import TMI_Api

api = TMI_Api()

delay = 1

print("電源に接続します")
dev_hID = api.TMI_HandleOpen("PW-A", "USB:1:1")
time.sleep(delay)

if dev_hID > 0:
    print(f"hID: {dev_hID}")

    print("機種名を表示します")
    ret, name = api.TMI_ModelNameQ(dev_hID)
    print(f"ret: {ret}")
    print(f"Model: {name}")
    time.sleep(delay)

    print("電圧, 電流設定値を表示します")
    ret, data = api.TMI_AllPresetQ(dev_hID)
    print(f"ret: {ret}")
    print(list(data))
    time.sleep(delay)

    print("通信を切断します")
    ret = api.TMI_HandleClose(dev_hID)
    print(f"ret: {ret}")
    print("電源との通信を切断しました")
else:
    print(f"エラーコード: {dev_hID}")