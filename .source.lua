local function get_replacer(skintone)
    return function (item)
        local name = item:sub(2, -2):lower()
        
        name, _ = name:gsub("[_-%.]", "")
        local st_name = name .. skintone

        return codes[st_name] or codes[name] or item
    end
end

local Emoji = {}
local proto = {}
setmetatable(Emoji, proto)

function proto.__call(self, text, skintone)
    skintone = skintone or ""

    local new, _ = text:gsub(":[%w%p]+:", get_replacer(skintone))

    return new
end

Emoji.Dark = "darkskintone"
Emoji.MediumDark = "mediumdarkskintone"
Emoji.Medium = "mediumskintone"
Emoji.MediumLight = "mediumlightskintone"
Emoji.Light = "lightskintone"

return Emoji
