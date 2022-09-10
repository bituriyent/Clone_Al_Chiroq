import logging
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher, executor,types
from keyboards import *
import logging

API_TOKEN = '5051937836:AAEvBasO_wnuNRYK2kBXNM8TH97Zv6kj_0A'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)




async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🔄Перезапуск бота"),
            types.BotCommand("levels", "🎁Призы"),
            types.BotCommand("policy", "📄Публичная оферта"),
            types.BotCommand("settings", "⚙Настройка")
        ]
    )


@dp.message_handler(text='/start')
async def sticker_hand(msg: types.Message):
    await msg.answer_sticker(sticker="CAACAgIAAxkBAAER5nZjGDUmJAu_H5Q587jzQlGR294BtgACxRIAAm7wkUrbYPAUWNH_FSkE",reply_markup=home)
    await msg.answer(text="Hurmatli foydalanuvchi! Tizimda muvaffaqiyatli ro'yxatdan o'tganingiz bilan tabriklaymiz.")
    await msg.answer(text=
        "Endi siz bonuslarni olishingiz va ballarni to'plashingiz mumkin! Mavjud sovrinlar va ballar to'plamini ko'rish uchun Al-Chiroq dasturini yuklab oling.",
        reply_markup=main_menu_inline_key)


@dp.message_handler(text="🎁 Sovg`alar")
@dp.message_handler(Command('levels'))
async def bot_start(message: types.Message):
    await message.answer("Harakat tanlang:")
    await message.answer(text=
                         f"❇️ level 1\n📶 Foiz:  0%\n\n🎁 Sovg`alar:\n\nOrganayzer x 50\nSmart Watch Amazfit x 2\nfitnes soati x 28\nSmart budilnik x 50\nportativ dinamik x 40\nportativ dinamik x 40\n"
                         f"Simsiz eshitish vositasi x 23\nSimsiz zaryadlovchi x 43\nSimli eshitish vositasi x 51\nMi Band 5 x 8\nOvozli to’plam 1000 daqiqa x ♾\nMonopod Mi x 29\nInternet to’plam 1000 MB x ♾\n"
                         f"Termos x 50\nXiaomi Redmi AIR simsiz naushniklar x 25\nelektron o'quvchi x 30\nTashqi HDD x 20\nTelevizor pristavkasi x 20\nhavo tozalagich x 20\nLogitech dinamiklari x 20\nryukzak x 30",
                         reply_markup=ortga
                         )
    await message.answer(text=
                         f"❇️ level 2\n📶 Foiz:  0%\n\n🎁 Sovg`alar:\n\nXiaomi elektr choynak x 45\nrobot changyutgich x 10\nMi/Realme/Redmi smartfoni x 5\nKamera x 5\nPanasonic ovoz paneli x 5\n"
                         f"Trimmer x 28\nTelevizor pristavkasi x 30\nNoutbuk x 5\nXiaomi massaj qurilma x 20\nGrafik planshet x 30\nXiaomi stabilizatori x 10\nTelevizor 32 x 5\nelektron o'quvchi x 40\n"
                         f"fitnes soati x 37\nSamsung smartfoni x 5\nSmart Soat Amazfit x 1\nXiaomi Wi-Fi router x 26\nOvozli to’plam 2000 daqiqa x ♾\nMi Band 6 x 2\nInternet to'plam 2000 Mb x ♾"
                         )
    await message.answer(text=
                         f"❇️ level 3\n📶 Foiz:  0%\n\n🎁 Sovg`alar: \n\nOvozli to’plam 3000 daqiqa x ♾\nTelevizor 32 x 10\nVR virtual reallik ko'zoynaklari x 10\nYandex.Station Lite x 20\nSamsung smartfoni x 5\n"
                         f"Samsung plansheti x 5\nLogitech dinamiklari x 15\nApple iPhone 12 4/64 x 5\nTelevizor pristavkasi x 40\nelektr soqol oladigan mashinasi x 50\nMi/Realme/Redmi smartfoni x 5\n"
                         f"Xiaomi Wanbo proyektori x 5\nMikroto'lqinli pech x 10\nelektr skuter x 5\nMonoblok x 5\nXiaomi stol chiroqchasi x 47\nInternet to'plam 5000 Mb x ♾\nMi Band 6 x 37\nApple iPad x 4")


@dp.message_handler(commands='policy')
async def bot_help(message: types.Message):
    text = ("https://telegra.ph/AL-CHIROQ-Aksiya-qoidalari-va-shartlari-06-30")
    await message.answer(text,reply_markup=ortga)


@dp.message_handler(text="⚙ Sozlamalar")
@dp.message_handler(text="/settings")
async def setting_Mennu(msg:types.Message):
    await msg.answer(text="Harakat tanlang:",reply_markup=settings)


@dp.message_handler(text="⬅ Ortga")
async def uyga(msg:types.Message):
    await msg.answer_sticker(sticker="CAACAgIAAxkBAAER5nZjGDUmJAu_H5Q587jzQlGR294BtgACxRIAAm7wkUrbYPAUWNH_FSkE",reply_markup=home)
    await msg.answer(text="Hurmatli foydalanuvchi! Tizimda muvaffaqiyatli ro'yxatdan o'tganingiz bilan tabriklaymiz.")
    await msg.answer(text=
        "Endi siz bonuslarni olishingiz va ballarni to'plashingiz mumkin! Mavjud sovrinlar va ballar to'plamini ko'rish uchun Al-Chiroq dasturini yuklab oling.",
        reply_markup=main_menu_inline_key)


@dp.message_handler(text="🎮 O’yin Portali")
async def gamesPortal(msg:types.Message):
    idd=msg.from_user.username
    await msg.answer(text=f"🎮 O’yinchi: @{idd}\n💣 Ballar: 0\n💣 Bugun yig’ilgan ballar: 0\n💵 Hisibingiz: 0 so`m\n🎫 Biletlaringiz: 0 dona",reply_markup=gamePortal)


@dp.message_handler(text="🧨 Turnir")
async def Turnirlar(msg:types.Message):
    await msg.answer(text="O’yinni tanlang",reply_markup=turnir)
    await msg.answer(text="Hozirda turnirlar yo`q")

@dp.message_handler(text="Sovrinlar")
async def Sovrinlar(msg:types.Message):
    await msg.answer("https://telegra.ph/Alchiroqdan-yangi-yil-turniri-12-20")


@dp.message_handler(text="Turnir qoidalari")
async def Turnir_Qoidalari(msg:types.Message):
    await msg.answer("https://telegra.ph/Al-Tournament-turniri-qoidalari-12-21")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)