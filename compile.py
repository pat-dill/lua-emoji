from getemojis import get_emojis
import json

with open("./.header.lua", "r") as file:
    header = file.read()

with open("./.source.lua", "r") as file:
    source = file.read()

middle = "local codes = HttpService:JSONDecode([[{}]])".format(json.dumps(get_emojis()))

with open("emoji.lua", "w") as file:
    file.write("\n\n".join([header, middle, source]))