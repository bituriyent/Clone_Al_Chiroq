from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

"""=============Default keyboards=========="""
home=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎮 O’yin Portali", callback_data="Games")
        ],
        [
            KeyboardButton(text="🎁 Sovg`alar",callback_data="Prizes"),
            KeyboardButton(text="⚙ Sozlamalar",callback_data="setting")
        ]
    ],
    resize_keyboard=True
)
ortga=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅ Ortga",callback_data=" ")
        ]
    ],
    resize_keyboard=True
)
gamePortal=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧨 Turnir")
        ],
        [
            KeyboardButton(text="Blocks"),
            KeyboardButton(text="Stair Master 3D")
        ],
        [
            KeyboardButton(text="Geometry Run 3D"),
            KeyboardButton(text="Little Plane")
        ],
        [
            KeyboardButton(text="SPIKY FISH 3")
        ],
        [
           KeyboardButton(text="⬅ Ortga")
        ]
    ],
    resize_keyboard=True
)
turnir=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sovrinlar"),
            KeyboardButton(text="Turnir qoidalari")
        ],
        [
            KeyboardButton(text="⬅ Ortga")
        ]
    ],
    resize_keyboard=True
)
settings=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Raqamni o’zgartirish"),
            KeyboardButton(text="🇺🇿🇷🇺 Tilni o’zgartirish"),

        ],
        [
            KeyboardButton(text="📄 Ommaviy taklif"),
            KeyboardButton(text="📌 Obuna")
        ],
        [
            KeyboardButton(text="⬅ Ortga",callback_data=ortga)
        ],
    ],
    resize_keyboard=True
)
"""=================INLINE KEYBOARDS====================="""
main_menu_inline_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔔 Al-Chrioqni ishqalash", callback_data="Al_Chiroqni_ishqalash")
        ],[
          InlineKeyboardButton(text="⭐ Premium chiroq", callback_data="Premium_Chiroq")
        ],
        [
            InlineKeyboardButton(text="🎮 O’yin Portali", callback_data="Game_Portal")
        ]
    ]
)