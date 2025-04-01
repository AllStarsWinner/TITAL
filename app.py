from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='About us')],
        [KeyboardButton(text='Special firefighting vehicles'), KeyboardButton(text='Aeroport special vehicles')],
        [KeyboardButton(text='Rescue special vehicles'), KeyboardButton(text='Forest firefighting vehicles')],
        [KeyboardButton(text='Aerial ladders'), KeyboardButton(text='Firefighting boats')],
        [KeyboardButton(text='Special vehicles for airports'), KeyboardButton(text='Search & Rescue vehicles')],
        [KeyboardButton(text='Medical trailer'), KeyboardButton(text='Anti-Riot vehicles')],
        [KeyboardButton(text='Mobile watch tower'), KeyboardButton(text='Explosion laboratories')],
        [KeyboardButton(text='New type water tanks'), KeyboardButton(text='Carbon dioxide extinguishing machine')],
        [KeyboardButton(text='Special washing vehicles')], [KeyboardButton(text='Special vehicles for nuclear power plants')],
        [KeyboardButton(text='Our general presentation')], [KeyboardButton(text=''), KeyboardButton(text='Contact us')],
    ]
)

