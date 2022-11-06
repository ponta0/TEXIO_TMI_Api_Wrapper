from ctypes import *


class TMI_Api:
    def __init__(self) -> None:
        self.tmi_api = windll.LoadLibrary("TMI_API.dll")
    def TMI_HandleOpen(self, model: str, set: str) -> int:
        """
        デバイスハンドルのオープン

        引数: 
            電源名指定の文字列: "PW-A"
            IF 種類: PC アドレス,システムアドレスを指定する文字列 （「IF 種類」+ ":" +「PC アドレス」+ ":" +「システムアドレス」）
                GP-IB の場合: DEV0～DEV3
                USB の場合: USB
                RS-232C の場合:  COM1～COM9
        戻り値:
            ID番号 エラーの場合は負数が戻ります
        """
        return self.tmi_api.TMI_HandleOpen(c_char_p(model.encode("utf-8")), c_char_p(set.encode("utf-8")))
    def TMI_HandleClose(self, hID: int) -> int:
        """
        デバイスハンドルのクローズ

        引数:
            ID番号
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_HandleClose(c_int(hID))
    def TMI_TimeOut(self, hID: int, Time: int) -> int:
        """
        タイムアウト時間の設定

        引数:
            ID番号
            タイムアウト時間（秒）
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_TimeOut(c_int(hID), c_int(Time))
    def TMI_Refresh(self, hID: int) -> int:
        """
        通信バッファのリフレッシュ
        引数:
            ID番号
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_Refresh(c_int(hID))
    def TMI_ModelNameQ(self, hID: int) -> int:
        """
        電源モデル名の取得

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            電源モデル名
        例:
            api = TMI_Api()
            ret, name = api.TMI_ModelNameQ(hID)
        """
        Model = create_string_buffer(20)
        return self.tmi_api.TMI_ModelNameQ(c_int(hID), byref(Model)), Model.value.decode("utf-8")
    def TMI_Voltage(self, hID: int, ch: str, preset: str, voltage: float) -> int:
        """
        プリセット・メモリへの電圧値設定

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
            プリセット番号: 1～4
            電圧設定値（V）
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
            -3: 出力範囲外
        """
        return self.tmi_api.TMI_Voltage(c_int(hID), c_char_p(ch.encode("utf-8")), c_char_p(preset.encode("utf-8")), c_double(voltage))
    def TMI_VoltageQ(self, hID: int, ch: str, preset: str) -> int:
        """
        プリセット・メモリからの電圧値取得

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
            プリセット番号: 1～4
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            電圧設定値（V）
        例:
            api = TMI_Api()
            ret, voltage = api.TMI_VoltageQ(hID, "1", "1")
        """
        Voltage = c_double()
        return self.tmi_api.TMI_VoltageQ(c_int(hID), c_char_p(ch.encode("utf-8")), c_char_p(preset.encode("utf-8")), byref(Voltage)), Voltage.value
    def TMI_Current(self, hID: int, ch: str, preset: str, current: float) -> int:
        """
        プリセットメモリへの電流値設定

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
            プリセット番号: 1～4
            電流設定値（A）
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
            -3: 出力範囲外
        """
        return self.tmi_api.TMI_Current(c_int(hID), c_char_p(ch.encode("utf-8")), c_char_p(preset.encode("utf-8")), c_double(current))
    def TMI_CurrentQ(self, hID: int, ch: str, preset: str) -> int:
        """
        プリセットメモリからの電流値取得

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
            プリセット番号: 1～4
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            電流設定値（A）
        例:
            api = TMI_Api()
            ret, current = api.TMI_CurrentQ(hID, "1", "1")
        """
        Current = c_double()
        return self.tmi_api.TMI_CurrentQ(c_int(hID), c_char_p(ch.encode("utf-8")), c_char_p(preset.encode("utf-8")), byref(Current)), Current.value
    def TMI_MainOutput(self, hID: int, onoff: str) -> int:
        """
        メインアウトプットのON/OFF

        引数:
            ID番号
            ON/OFF指定の文字列: 1: ON, 0: OFF
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_MainOutput(c_int(hID), c_char_p(onoff.encode("utf-8")))
    def TMI_MainOutputQ(self, hID: int) -> int:
        """
        メインアウトプットのON/OFF状態取得

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            ON/OFF状態の文字列: 1: ON, 0: OFF
        例:
            api = TMI_Api()
            ret, onoff = api.TMI_MainOutputQ(hID)
        """
        ans = create_string_buffer(2)
        return self.tmi_api.TMI_MainOutputQ(c_int(hID), byref(ans)), ans.value.decode("utf-8")
    def TMI_Delay(self, hID: int, onoff: str) -> int:
        """
        ディレイ機能の設定 

        引数:
            ID番号
            ON/OFF指定の文字列: 1: ON, 0: OFF
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_Delay(c_int(hID), c_char_p(onoff.encode("utf-8")))
    def TMI_DelayQ(self, hID: int) -> int:
        """
        ディレイ機能の状態取得

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            ON/OFF状態の文字列: 1: ON, 0: OFF
        例:
            api = TMI_Api()
            ret, onoff = api.TMI_DelayQ(hID)
        """
        ans = create_string_buffer(2)
        return self.tmi_api.TMI_DelayQ(c_int(hID), byref(ans)), ans.value.decode("utf-8")
    def TMI_OutputSel(self, hID: int, ch: str, onoff: str) -> int:
        """
        アウトプットセレクトの設定

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
            ON/OFF指定の文字列: 1: ON, 0: OFF
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
            -3: 出力範囲外
        """
        return self.tmi_api.TMI_OutputSel(c_int(hID), c_char_p(ch.encode("utf-8")), c_char_p(onoff.encode("utf-8")))
    def TMI_OutputSelQ(self, hID: int, ch: str) -> int:
        """
        アウトプットセレクトの状態取得

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
                -3: 出力範囲外
            ON/OFF状態の文字列: 1: ON, 0: OFF
        例:
            api = TMI_Api()
            ret, onoff = api.TMI_OutputSelQ(hID, "1")
        """
        ans = create_string_buffer(2)
        return self.tmi_api.TMI_OutputSelQ(c_int(hID), c_char_p(ch.encode("utf-8")), byref(ans)), ans.value.decode("utf-8")
    def TMI_TrackingOnOff(self, hID: int, onoff: str) -> int:
        """
        トラッキング機能の設定

        引数:
            ID番号
            ON/OFF指定の文字列: 1: ON, 0: OFF
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_TrackingOnOff(c_int(hID), c_char_p(onoff.encode("utf-8")))
    def TMI_TrackingOnOffQ(self, hID: int) -> int:
        """
        トラッキング機能の状態取得

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            ON/OFF状態の文字列: 1: ON, 0: OFF
        例:
            api = TMI_Api()
            ret, onoff = api.TMI_TrackingOnOffQ(hID)
        """
        ans = create_string_buffer(2)
        return self.tmi_api.TMI_TrackingOnOffQ(c_int(hID), byref(ans)), ans.value.decode("utf-8")
    def TMI_TrackingMode(self, hID: int, mode: str) -> int:
        """
        トラッキングモードの設定

        引数:
            ID番号
            モード指定の文字列: 1: 相対値, 0: 絶対値
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_TrackingMode(c_int(hID), c_char_p(mode.encode("utf-8")))
    def TMI_TrackingModeQ(self, hID: int) -> int:
        """
        トラッキングモードの状態取得

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            モード状態の文字列: 1: 相対値, 0: 絶対値
        例:
            api = TMI_Api()
            ret, mode = api.TMI_TrackingModeQ(hID)
        """
        ans = create_string_buffer(2)
        return self.tmi_api.TMI_TrackingModeQ(c_int(hID), byref(ans)), ans.value.decode("utf-8")
    def TMI_TrackingGroup(self, hID: int, ch: str, set: str) -> int:
        """
        トラッキングチャンネルの設定

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
            トラッキング設定の文字列: 2: -方向, 1: +方向, 0: OFF
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
            -3: 出力範囲外
        """
        return self.tmi_api.TMI_TrackingGroup(c_int(hID), c_char_p(ch.encode("utf-8")), c_char_p(set.encode("utf-8")))
    def TMI_TrackingGroupQ(self, hID: int, ch: str) -> int:
        """
        トラッキングチャンネルの状態取得

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
                -3: 出力範囲外
            トラッキング設定の文字列: 2: -方向, 1: +方向, 0: OFF
        例:
            api = TMI_Api()
            ret, set = api.TMI_TrackingGroupQ(hID, "1")
        """
        ans = create_string_buffer(2)
        return self.tmi_api.TMI_TrackingGroupQ(c_int(hID), c_char_p(ch.encode("utf-8")), byref(ans)), ans.value.decode("utf-8")
    def TMI_TrackingData(self, hID: int, ch: str, va: str, data: float) -> int:
        """
        トラッキングデータの設定

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
            データ指定の文字列: 1: 電流指定, 0: 電圧指定
            トラッキング設定データ
        戻り値:
             0: 成功
            -1: タイムアウトエラー
            -2: オープンクローズエラー
            -3: 出力範囲外
        例:
            api = TMI_Api()
            # 絶対値
            ret = api.TMI_TrackingData(hID, "1", "0", 5.0) # トラッキングの電圧値を+5.0V変化させます
            # 相対値
            ret = api.TMI_TrackingData(hID, "1", "0", 50.0) # トラッキングの電圧値を+50.0%変化させます
        """
        return self.tmi_api.TMI_TrackingData(c_int(hID), c_char_p(ch.encode("utf-8")), c_char_p(va.encode("utf-8")), c_double(data))
    def TMI_TrackingDataQ(self, hID: int, ch: str, va: str) -> int:
        """
        トラッキングデータの状態取得

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
            データ指定の文字列: 1: 電流指定, 0: 電圧指定
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
                -3: 出力範囲外
            トラッキング設定データ
        例:
            api = TMI_Api()
            ret, data = api.TMI_TrackingDataQ(hID, "1", "0")
        """
        data = c_double()
        return self.tmi_api.TMI_TrackingDataQ(c_int(hID), c_char_p(ch.encode("utf-8")), c_char_p(va.encode("utf-8")), byref(data)), data.value
    def TMI_DelayTime(self, hID: int, ch: str, data: float) -> int:
        """
        ディレイ時間の設定

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
            ディレイ時間 （0.0 秒～10.0 秒  設定単位: 0.1 秒）
        戻り値:
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
                -3: 出力範囲外
        """
        return self.tmi_api.TMI_DelayTime(c_int(hID), c_char_p(ch.encode("utf-8")), c_double(data))
    def TMI_DelayTimeQ(self, hID: int, ch: str) -> int:
        """
        ディレイ時間設定の取

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
                -3: 出力範囲外
            ディレイ時間 （0.0 秒～10.0 秒  設定単位: 0.1 秒）
        例:
            api = TMI_Api()
            ret, data = api.TMI_DelayTimeQ(hID, "1")
        """
        data = c_double()
        return self.tmi_api.TMI_DelayTimeQ(c_int(hID), c_char_p(ch.encode("utf-8")), byref(data)), data.value
    def TMI_Display(self, hID: int, ch: str) -> int:
        """
        ディスプレイ内容の設定

        引数:
            ID番号
            表示チャンネル指定の文字列: 1～4
        戻り値:
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
                -3: 出力範囲外
        """
        return self.tmi_api.TMI_Display(c_int(hID), c_char_p(ch.encode("utf-8")))
    def TMI_DisplayQ(self, hID: int) -> int:
        """
        ディスプレイ内容の取得

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
                -3: 出力範囲外
            表示チャンネル指定の文字列: 1～4
        例:
            api = TMI_Api()
            ret, data = api.TMI_DisplayQ(hID)
        """
        ans = create_string_buffer(1)
        return self.tmi_api.TMI_DisplayQ(c_int(hID), byref(ans)), ans.value.decode("utf-8")
    def TMI_Preset(self, hID: int, preset: str) -> int:
        """
        プリセット番号の選択

        引数:
            ID番号
            プリセット指定の文字列: 1～4
        戻り値:
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_Preset(c_int(hID), c_char_p(preset.encode("utf-8")))
    def TMI_PresetQ(self, hID: int) -> int:
        """
        プリセット番号の取得

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            プリセット指定の文字列: 1～4
        例:
            api = TMI_Api()
            ret, data = api.TMI_PresetQ(hID)
        """
        ans = create_string_buffer(1)
        return self.tmi_api.TMI_PresetQ(c_int(hID), byref(ans)), ans.value.decode("utf-8")
    def TMI_MoniDataQ(self, hID: int, ch: str) -> int:
        """
        出力モニタ値の取得

        引数:
            ID番号
            チャンネル指定の文字列: 1～4
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
                -3: 出力範囲外
            モニタ電圧値
            モニタ電流値
            CV/CC状態 1: CC, 0: CV
        例:
            api = TMI_Api()
            ret, data1, data2, data3 = api.TMI_MoniDataQ(hID, "1")
        """
        voltage = c_double()
        current = c_double()
        cv_cc = c_char()
        return self.tmi_api.TMI_MoniDataQ(c_int(hID), c_char_p(ch.encode("utf-8")), byref(voltage), byref(current), byref(cv_cc)), voltage.value, current.value, cv_cc.value
    def TMI_AdrQ(self, hID: int) -> int:
        """
        システムアドレスの取得

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            システムアドレス
        例: 
            api = TMI_Api()
            ret, data = api.TMI_AdrQ(hID)
        """
        ans = c_char()
        return self.tmi_api.TMI_AdrQ(c_int(hID), byref(ans)), ans.value
    def TMI_RemoteLocal(self, hID: int) -> int:
        """
        ローカル設定

        引数:
            ID番号
        戻り値:
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_RemoteLocal(c_int(hID))
    def TMI_LocalLockOut(self, hID: int) -> int:
        """
        ローカルロックアウト設定

        引数:
            ID番号
        戻り値:
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_LocalLockOut(c_int(hID))
    def TMI_DataBackUp(self, hID: int) -> int:
        """
        データバックアップ

        引数:
            ID番号
        戻り値:
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_DataBackUp(c_int(hID))
    def TMI_SRQEnable(self, hID: int, onoff: int) -> int:
        """
        サービスリクエストの設定

        引数:
            ID番号
            サービスリクエストせってい 1: 許可, 0: 禁止
        戻り値:
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
        """
        return self.tmi_api.TMI_SRQEnable(c_int(hID), c_int(onoff))
    def TMI_AllPresetQ(self, hID: int) -> int:
        """
        全プリセットの取得

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            プリセット指定の文字列: 1～4
            モニタ電圧,電流値[4*4*2]
        例: 
            api = TMI_Api()
            ret, data = api.TMI_AllPresetQ(hID)
        """
        data = (c_double * (4 * 4 * 2))()
        return self.tmi_api.TMI_AllPresetQ(c_int(hID), byref(data)), data
    def TMI_AllPresetQS(self, hID: int) -> int:
        """
        全プリセットの取得(カンマ区切り文字列)

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            プリセット指定の文字列: 1～4
            モニタ電圧,電流値
        例: 
            api = TMI_Api()
            ret, data = api.TMI_AllPresetQS(hID)
        """
        data = (c_char * 256)()
        return self.tmi_api.TMI_AllPresetQS(c_int(hID), byref(data)), data.value.decode("utf-8")
    def TMI_Out(self, hID: str, cmd: str) -> int:
        """
        コマンドの送信

        引数:
            ID番号
            コマンド
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
        例: 
            api = TMI_Api()
            ret = api.TMI_Out(hID, "SW1") # メインアウトプットをONにする
        """
        return self.tmi_api.TMI_Out(c_int(hID), c_char_p(cmd.encode("utf-8")))
    def TMI_In(self, hID: str) -> int:
        """
        コマンド応答の受信

        引数:
            ID番号
        戻り値:
            エラーコード
                0: 成功
                -1: タイムアウトエラー
                -2: オープンクローズエラー
            受信した文字列
        例: 
            api = TMI_Api()
            ret, data = api.TMI_In(hID)
        """
        data = (c_char * 256)()
        return self.tmi_api.TMI_In(c_int(hID), byref(data)), data.value.decode("utf-8")






