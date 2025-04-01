import asyncio  # Імпортуємо модуль для роботи з асинхронністю
from aiogram import Bot, Dispatcher, F, types  # Імпортуємо необхідні компоненти з бібліотеки aiogram
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
import app
from aiogram.fsm.state import State, StatesGroup


# await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./'))
from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('You are greeted by TITAL\'s Telegram chatbot. Please select the category you would like to see',reply_markup=app.main)
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('photos/greetingsEN.png'))



@dp.message(F.text == 'Firefighting pumpers')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('photos/apdTech/apd-03.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('photos/apdTech/apd-04.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('photos/apdTech/apd1.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('photos/apdTech/apd-07.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('photos/apdTech/apd-08.jpg'), caption='Interested in purchasing? Call us +38 0672098020')



@dp.message(F.text == 'Special firefighting vehicles')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('photos/spezgaz/akg-01.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('photos/spezgaz/akg-02.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('photos/spezgaz/akg-03.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('photos/spezgaz/akg-05.png'), caption='Interested in purchasing? Call us +38 0672098020')



@dp.message(F.text == 'Special vehicles for airports')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/aerodrom/aa-01_4x4-1.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/aerodrom/aa-02_4x4-1.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/aerodrom/aa-03_4x4-1.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/aerodrom/aa-04_4x4-1.jpg'), caption='Interested in purchasing? Call us +38 0672098020')


@dp.message(F.text == 'Rescue special vehicles')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/helper/sarm_l-01.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/helper/sarm_l-02.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/helper/sarm_l-04.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/helper/sarm_l-07.jpg'), caption='Interested in purchasing? Call us +38 0672098020')


@dp.message(F.text == 'Aerial ladders')
async def cmd_text1(message: Message):

    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/drabina/apt_30-01.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/drabina/apt_30-02.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/drabina/apt_30-03.png'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/drabina/apt_30-05.jpg'), caption='Interested in purchasing? Call us +38 0672098020')


@dp.message(F.text == 'Forest firefighting vehicles')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/lisovi/acl-03.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/lisovi/acl-02.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/lisovi/acl-07.png'), caption='Interested in purchasing? Call us +38 0672098020')



@dp.message(F.text == 'Firefighting boats')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/kater/fb-02.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/kater/fb-03.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/kater/fb-07.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/kater/fb-07.jpg'),caption='Interested in purchasing? Call us +38 0672098020')



@dp.message(F.text == 'Contact us')
async def cmd_text1(message: Message):
    await message.answer('Telegram +38 0672098020, WhatsApp +38 0672098020, E-Mail vbfunds@gmail.com')


@dp.message(F.text == 'Go back')
async def cmd_text1(message: Message):
    await message.answer('')


@dp.message(F.text == 'Aeroport special vehicles')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos2/aerodrom/aa-01_4x4-1.jpg'),)
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos2/aerodrom/aa-03_4x4-1.jpg'),)
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos2/aerodrom/aa-08_4x4-1.png'),caption='Interested in purchasing? Call us +38 0672098020')


@dp.message(F.text == 'Search & Rescue vehicles')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos2/poshuk/pra-01.jpg'),)
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos2/poshuk/pra-02.jpg'),)
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos2/poshuk/pra-04.png'),caption='Interested in purchasing? Call us +38 0672098020')



@dp.message(F.text == 'Medical trailer')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos2/medic/ppmd-01.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos2/medic/ppmd-02.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos2/medic/ppmd-03.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos2/medic/ppmd-04.png'),caption='Interested in purchasing? Call us +38 0672098020')


@dp.message(F.text == 'Explosion laboratories')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./mentik/labs/vtl-01.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./mentik/labs/vtl-02.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./mentik/labs/vtl-07.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./mentik/labs/vtl-09.jpg'),caption='Interested in purchasing? Call us +38 0672098020')



@dp.message(F.text == 'Mobile watch tower')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./mentik/spy/mvs-01.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./mentik/spy/mvs-02.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./mentik/spy/mvs-04.jpg'), caption='Interested in purchasing? Call us +38 0672098020')


@dp.message(F.text == 'Anti-Riot vehicles')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./mentik/zavorush/barrier-01-1.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./mentik/zavorush/barrier-02-1.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./mentik/zavorush/barrier-07-1.jpg'),caption='Interested in purchasing? Call us +38 0672098020')




@dp.message(F.text == 'Drinking water tanks trucks')
async def cmd_text1(message: Message):
    await message.answer('Please wait while the presentation is being loaded...')
    await bot.send_document(chat_id=message.chat.id, document=FSInputFile('pres/Termos.docx'))


@dp.message(F.text == 'About us')
async def cmd_text1(message: Message):
    await message.answer("""✅ Machine Building Plant "TITAL COMPANY" (special fire fighting vehicles) is engaged in the production of fire fighting equipment, emergency tools, and other special machinery. The company’s products help save lives and protect property during emergencies.

✅ In addition, TITAL COMPANY manufactures fire boats, emergency equipment for airports, fire ladders, and fire platforms. These products are designed to meet the diverse needs of emergency services, ensuring efficiency and reliability.

✅ The company uses modern design technologies, and its design and technology bureau promotes innovative engineering solutions.

✅ All projects are in compliance with the highest standards, and the components, materials, and equipment undergo thorough quality testing to ensure safety and functionality.

✅ Our products are popular in Ukraine and abroad, reliably sold in Estonia, Georgia, Uzbekistan, the Czech Republic, and other countries.""")

@dp.message(F.text == '')
async def cmd_text1(message: Message):
    await message.answer('')





@dp.message(F.text == 'Наші нові розробки')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos4/photo_2025-02-18_07-48-26.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos4/photo_2025-02-18_07-48-36.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos4/photo_2025-02-18_07-48-40.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos4/photo_2025-02-18_07-48-44.jpg')),
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/p1.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('./photos/p2.jpg'), caption='Interested in purchasing? Call us +38 0672098020')


@dp.message(F.text == 'Our general presentation')
async def cmd_text1(message: Message):
    await message.answer('Please wait, the presentation is being loaded...')
    await bot.send_document(chat_id=message.chat.id, document=FSInputFile('pres/Firefighting Vehicles.pdf'))



@dp.message(F.text == 'New type water tanks')
async def cmd_text1(message: Message):
    await message.answer('Please wait, the presentation is being loaded...')
    await bot.send_document(chat_id=message.chat.id, document=FSInputFile('pres/Termos.docx'))


@dp.message(F.text == 'Carbon dioxide extinguishing machine')
async def cmd_text1(message: Message):
    await message.answer('Please wait, the presentation is being loaded...')
    await bot.send_document(chat_id=message.chat.id, document=FSInputFile('pres/dioxide.docx'))


@dp.message(F.text == 'Special washing vehicles')
async def cmd_text1(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('washing/mvu1-01.jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('washing/mvu1-02 (1).jpg'))
    await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile('washing/mvu1-03.png'))

@dp.message(F. text == 'Special vehicles for nuclear power plants')
async def cmd_text1(message: Message):
    await message.answer('Please wait, the presentation is being loaded...')
    await bot.send_document(chat_id=message.chat.id, document=FSInputFile('pres/Presentation KOBOM (2).pptx'))

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('не працює')