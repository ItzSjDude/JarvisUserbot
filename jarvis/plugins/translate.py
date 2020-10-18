""" Google Translate
Available Commands:
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate"""

import emoji
from googletrans import Translator
from jarvis.utils import jarvis_cmd, sudo_cmd


@jarvis.on(jarvis_cmd("tr ?(.*)"))
@jarvis.on(sudo_cmd("tr ?(.*)",allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        # https://t.me/c/1220993104/192075
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "gu"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply("`.tr LanguageCode` as reply to a message")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        output_str = """** ✓ 𝚃𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎𝚍 𝙱𝚢 𝙹𝚊𝚛𝚟𝚒𝚜 ✓ **
         Source **( {} )**
         Translation **( {} )**
         {}""".format(
            translated.src,
            lan,
            after_tr_text
        )
        await event.reply(output_str)
    except Exception as exc:
        await event.reply(str(exc))