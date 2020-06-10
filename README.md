# lua-emoji

**lua-emoji** allows you to convert text to emoji just as you would in a chat client like Discord:

```lua
local emoji = require(path.to.emoji)

print(emoji("Emojis are :ok_hand:!"))

-- output: Emojis are 👌!
```

For a list of emoji aliases, check out this [cheat sheet](https://www.webfx.com/tools/emoji-cheat-sheet/)

The emoji list is generated from Taehoon Kim's [emoji library](https://pypi.org/project/emoji/) for Python.