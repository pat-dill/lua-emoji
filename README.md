:smile:    lua-emoji :smile:
=======
```lua

local emoji = require(path.to.emoji)

print(emoji("emojis are :ok_hand:!"))

-- output: emojis are 👌!

```

lua-emoji supports skin tones!
---

`emoji()` takes an optional second argument for the skin tone. Available skin tones are
- `emoji.Light`
- `emoji.Dark`
- `emoji.MediumLight`
- `emoji.MediumDark`
- `emoji.Medium`

Aliases
----

Several aliases can be used for each emoji depending on your preferences:

```lua
print(emoji(":thumbs_up: = :thumbs-up: = :thumbsup:"))
-- output: 👍 = 👍 = 👍
```

lua-emoji also allows you to use ISO country codes from https://countrycode.org/ for flags.

Install
------

All the code is in one module, so you can install it by downloading the `emoji.lua` file from the [GitHub repository](https://github.com/jpatrickdill/lua-emoji) and inserting it in your game.

Resources
---------------
- [Emoji Cheatsheet](https://www.webfx.com/tools/emoji-cheat-sheet/)
- [Official Unicode List](http://www.unicode.org/emoji/charts/full-emoji-list.html)

The emoji list is generated from Taehoon Kim's [emoji](https://pypi.org/project/emoji/) for Python.
