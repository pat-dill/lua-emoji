from getemojis import get_emojis
import re
import json
import codecs

with open("./.header.lua", "r") as file:
    header = file.read()

with open("./.source.lua", "r") as file:
    source = file.read()

encoded = "{" + ",".join([
    '["{}"]="{}"'.format(key, val) for key, val in get_emojis().items()
]) + "}"

middle = "local codes = " + encoded

with codecs.open("emoji.lua", "w+", "utf-8", errors="surrogatepass") as file:
    file.write("\n\n".join([header, middle, source]))