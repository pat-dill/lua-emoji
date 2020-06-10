import requests
import re
from emoji import emojize
import json

names = re.compile(r"u':(\S+):':")

r = requests.get("https://raw.githubusercontent.com/carpedm20/emoji/master/emoji/unicode_codes.py")

dump = {}

for item in names.finditer(r.text):
    name = item.group(1)
    e_name = ":{}:".format(name)
    emoji = emojize(e_name, use_aliases=True)

    name = name.lower().replace("_", "").replace("-", "")

    if ":" not in emoji:
        dump[name.lower()] = emoji

json.dump(dump, open("emojis.json", "w"), indent=4, separators=(',', ': '))