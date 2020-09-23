''''''


_translation = {
    'zh': {
        'start': 'Hi %(user)s，歡迎光臨🎊\n\n輸入 /help 查看使用方法。',
        'help': '''*TG Downloader Bot 使用方法*
1. GIF 圖片：
☛ 直接傳送 `GIF 圖片`。
☚ 打包的 `MP4` 和 `GIF` 檔案。

2. 靜態貼圖：
☛ 直接傳送`靜態貼圖`。
☚ `PNG` 檔案。

3. 動態貼圖：
☛ 伺服器資源有限尚未提供。

4. 靜態貼圖合集：
☛ 直接傳送`靜態貼圖`，點選下方按鈕「下載完整貼圖合集」。
☛ 直接傳送`靜態貼圖合集連結`，如 [EmmaWatsonStickers](https://t.me/addstickers/EmmaWatsonStickers)。
☚ 打包的 `PNG` 檔案。

⚠︎ 下載貼圖合集非常耗費資源，如非必要還請挑選後逐個下載。對此不勝感激。

請盡情使用 :)''',
        'limit_exceed': '今日用量已超出 %(limit)s，請明天再試',
        'kb_sticker_set': '下載完整貼圖合集',
        'unsupport': '資源有限尚未支援，請自行下載轉換',
        'zip_preparing': '正在準備檔案，所需時間較長，請等待',
        'zip_packing': '等待檔案打包，所需時間較長，請等待',
        'zip_timeout': '等待超時，請稍後重試',
        'exec_error': '執行錯誤，請自行下載轉換',
        'file_size_exceed': '檔案過大，請自行下載轉換',
    },

    'en': {
        'start': 'Hi %(user)s，Welcome🎊\n\nUse /help to find detail usage.',
        'help': '''*TG Downloader Bot Usage*
1. GIF:
☛ Send `GIF` directly.
☚ File packed with `MP4` and `GIF`.

2. Static Sticker:
☛ Send `Sticker` directly.
☚ File of `PNG`.

3. Animated Sticker:
☛ Due to the resource limitation, it is not support to decode this type of sticker right now.

4. Static Sticker Set：
☛ Send `Sticker` first, then tap「Download Sticker Set」button.
☛ Send `Sticker Set Link` directly, for example [EmmaWatsonStickers](https://t.me/addstickers/EmmaWatsonStickers).
☚ File packed with a list of `PNGs`.

⚠︎ It is resource consuming to download the entire sticker set, PLEASE select and download what you want one by one if not necessary. I would deeply appreciate if you do so.

Hope you enjoy it :)''',
        'limit_exceed': 'Limit exceed %(limit)s today, try tomorrow',
        'kb_sticker_set': 'Download Sticker Set',
        'unsupport': 'Resource limited, please download and decode by yourself',
        'zip_preparing': 'File preparing, hold on please',
        'zip_packing': 'File packing, hold on please',
        'zip_timeout': 'Timeout waiting, try again later',
        'exec_error': 'Error executing, please download and decode by yourself',
        'file_size_exceed': 'File too large, please download and decode by yourself',
    }
}
_translation_default = _translation['en']


def l10n(key, locale='en'):
    ''''''
    locale = locale or 'en'
    locale = locale[:2] if len(locale) > 2 else locale
    document = _translation.get(locale, _translation_default)
    return document.get(key, key)


if __name__ == '__main__':
    pass
