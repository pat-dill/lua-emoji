import requests
import re
from emoji import emojize
import json

names = re.compile(r"u':(\S+):':")

sanitize = lambda s: s.lower().replace("_", "").replace("-", "").replace(" ", "").replace(".", "")

def get_emojis():
    dump = {}

    # base set

    r = requests.get("https://raw.githubusercontent.com/carpedm20/emoji/master/emoji/unicode_codes.py")
    for item in names.finditer(r.text):
        name = item.group(1)
        e_name = ":{}:".format(name)
        emoji = emojize(e_name, use_aliases=True)

        name = sanitize(name)

        if ":" not in emoji:
            dump[name.lower()] = emoji

    base_len = len(dump)
    print("{} base emojis".format(base_len))

    # country codes

    countries = requests.get("http://country.io/names.json").json()
    iso3 = requests.get("http://country.io/iso3.json").json()
    for code, name in countries.items():
        s_name = sanitize(name)
        if s_name in dump:
            dump[code.lower()] = dump[s_name]
            dump[iso3[code.upper()].lower()] = dump[s_name]

    # manual updates

    dump.update({
        "light": "\ud83c\udffb",
        "dark": "\ud83c\udfff",
        "mediumlight": "\ud83c\udffc",
        "mediumdark": "\ud83c\udffe",
        "medium": "\ud83c\udffd"
    })

    # log

    print("{} aliases\n{} total".format(len(dump)-base_len, len(dump)))

    return dump

if __name__ == "__main__":
    json.dump(get_emojis(), open("emojis.json", "w"), indent=4, separators=(',', ': '))
