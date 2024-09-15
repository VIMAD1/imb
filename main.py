import telebot
from telebot import types
import webbrowser
bot = telebot.TeleBot('7470540360:AAEV0HAKh7w66U12fqaWNvOQREpDurewDXQ')

reklama = 'Тут может быть ваша реклама'
imgx = 'https://frankfurt.apollo.olxcdn.com/v1/files/gzomy52lz6i62-KZ/image;s=600x0;q=50'

@bot.message_handler(commands=['start'])
def main(message):
    bot.delete_message(message.chat.id, message.message_id )
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Турники', callback_data='t' ))
    markup.add(types.InlineKeyboardButton('Брусья', callback_data='b'))
    markup.add(types.InlineKeyboardButton('Канал', url='https://t.me/street_simulators'))
    bot.send_message(message.chat.id, f'<b>Здравствуйте</b>, {message.from_user.first_name} , выберите на чем будете тренироваться, а мой бот вам поможет 🏆',  parse_mode='html' , reply_markup=markup)
    




@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 't':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Упражнения', callback_data='ypdr' ))
        markup.add(types.InlineKeyboardButton('Элементы', callback_data='afdu'))
        markup.add(types.InlineKeyboardButton('Выходы', callback_data='vidh'))
        markup.add(types.InlineKeyboardButton('Назад', callback_data='nazad'))
        bot.edit_message_text('<b>Отлично, теперь выберете: </b> \n \n Упражнения \n Элименты \n Выходы' , callback.message.chat.id , callback.message.message_id ,  parse_mode='html' , reply_markup=markup  )
    if callback.data == 'b': # брусья
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Упражнения', callback_data='yprb' ))
        markup.add(types.InlineKeyboardButton('Элементы', callback_data='aldb'))
        markup.add(types.InlineKeyboardButton('Назад', callback_data='nazad'))
        bot.edit_message_text('Отлично, теперь выберете:привет' , callback.message.chat.id , callback.message.message_id  , reply_markup=markup )
    if callback.data == 'ypdr': # упражнения для турника
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Бицепс', callback_data='bihe' ))
        markup.add(types.InlineKeyboardButton('Трицепс', callback_data='trih'))
        markup.add(types.InlineKeyboardButton('Плечи', callback_data='plechi' ))
        markup.add(types.InlineKeyboardButton('Пресс', callback_data='press' ))
        markup.add(types.InlineKeyboardButton('Спина', callback_data='spina'))
        markup.add(types.InlineKeyboardButton('Назад', callback_data='t'))
        bot.edit_message_text('Отлично, теперь выберете:' , callback.message.chat.id , callback.message.message_id  , reply_markup=markup )
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
        
    if callback.data == 'afdu': # элементы для турника
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Анти Оли ', callback_data='antiol'))
        markup.add(types.InlineKeyboardButton('Бочка', callback_data='bochka'))
        markup.add(types.InlineKeyboardButton('Гробик', callback_data='hropic'))
        markup.add(types.InlineKeyboardButton('Замок', callback_data='hamok'))
        markup.add(types.InlineKeyboardButton('икс (x) вылет ', callback_data='x'))
        markup.add(types.InlineKeyboardButton('Лач гейнер', callback_data='lanch'))
        markup.add(types.InlineKeyboardButton('Луна', callback_data='lyna'))
        markup.add(types.InlineKeyboardButton('Манки', callback_data='manki'))
        markup.add(types.InlineKeyboardButton('Оли', callback_data='olil'))
        markup.add(types.InlineKeyboardButton('Подъём переворотом', callback_data='podiomsperev' ))
        markup.add(types.InlineKeyboardButton('Перышко', callback_data='perishko'))
        markup.add(types.InlineKeyboardButton('Перелет на 180', callback_data='perel180'))
        markup.add(types.InlineKeyboardButton('Пистолетик', callback_data='pistol'))
        markup.add(types.InlineKeyboardButton('Родео', callback_data='rodeo'))
        markup.add(types.InlineKeyboardButton('Русские обороты', callback_data='russ'))
        markup.add(types.InlineKeyboardButton('склепка', callback_data='sklepka' ))
        markup.add(types.InlineKeyboardButton('солнышко', callback_data='solnishko' ))
        markup.add(types.InlineKeyboardButton('Санжировка', callback_data='sanhir'))
        markup.add(types.InlineKeyboardButton('Стульчик вперед', callback_data='stylv'))
        markup.add(types.InlineKeyboardButton('Сульчик назад', callback_data='stylntehnich'))
        markup.add(types.InlineKeyboardButton('Скорпион', callback_data='skorp'))
        markup.add(types.InlineKeyboardButton('Смертник', callback_data='smer'))
        markup.add(types.InlineKeyboardButton('Финский подъем', callback_data='finsk'))
        markup.add(types.InlineKeyboardButton('360', callback_data='360'))
        markup.add(types.InlineKeyboardButton('360 из упора', callback_data='360ypor'))
        markup.add(types.InlineKeyboardButton('Назад', callback_data='t'))
        bot.edit_message_text('Отлично, теперь выберете: \n А-Я' , callback.message.chat.id , callback.message.message_id  , parse_mode='html', reply_markup=markup )
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
        
    if callback.data == 'vidh': # выходы для турника
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Ангела(выход)', callback_data='angel'))
        markup.add(types.InlineKeyboardButton('Выход на одну', callback_data='v1'))
        markup.add(types.InlineKeyboardButton('Выход на две', callback_data='v2'))
        markup.add(types.InlineKeyboardButton('Выход на три', callback_data='v3'))
        markup.add(types.InlineKeyboardButton('Выход на четыре', callback_data='v4'))
        markup.add(types.InlineKeyboardButton('Декстер', callback_data='dexter'))
        markup.add(types.InlineKeyboardButton('Печатная машинка', callback_data='peredpech2'))
        markup.add(types.InlineKeyboardButton('Испанский', callback_data='ispan'))
        markup.add(types.InlineKeyboardButton('Итальянский (армейский)', callback_data='ital'))
        markup.add(types.InlineKeyboardButton('Из под турника (выход)', callback_data='ispodternika'))
        markup.add(types.InlineKeyboardButton('Кит фуэрзе', callback_data='kitfayer'))
        markup.add(types.InlineKeyboardButton('Капитанский', callback_data='kapit'))
        markup.add(types.InlineKeyboardButton('Крабик1', callback_data='krab'))
        markup.add(types.InlineKeyboardButton('Офицерский', callback_data='ofis'))
        markup.add(types.InlineKeyboardButton('Полотенце', callback_data='polotence'))
        markup.add(types.InlineKeyboardButton('Принц на одну руку', callback_data='princ1'))
        markup.add(types.InlineKeyboardButton('Приц на две руки', callback_data='princ2'))
        markup.add(types.InlineKeyboardButton('Феникс', callback_data='fenix'))
        markup.add(types.InlineKeyboardButton('Филин', callback_data='filin'))
        markup.add(types.InlineKeyboardButton('Назад', callback_data='t'))
        bot.edit_message_text('Отлично, теперь выберете: \n А-Я' , callback.message.chat.id , callback.message.message_id  , parse_mode='html', reply_markup=markup )
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
    if callback.data == 'nazad': # стартовая 
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Турники', callback_data='t' ))
        markup.add(types.InlineKeyboardButton('Брусья', callback_data='b'))
        markup.add(types.InlineKeyboardButton('Канал', url='https://t.me/street_simulators'))
        bot.edit_message_text( '<b>Выберите на чем будете тренироваться, а мой бот вам поможет. 🏆 \n\nТакже можете подписаться на мой канал. 🥇</b> ', callback.message.chat.id ,callback.message.message_id , parse_mode='html' , reply_markup=markup)
        
    if callback.data == 'antiol':
        img = 'https://www.youtube.com/watch?v=ik3jlODGn_4'
        im = 'https://www.youtube.com/watch?v=tVD_clKMzSc&'
        bot.edit_message_text(  '<b>Анити Оли </b> \n \n Сложность - среднее \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'bochka':
        
        
        im = 'https://yandex.ru/video/preview/8407792785617479840'
        img = 'https://www.youtube.com/watch?v=GkVMKK9JndY'
        bot.edit_message_text(  '<b>Бочка </b> \n \n Сложность - легко \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'hropic':
        
        im = 'https://yandex.ru/video/preview/5180405196260316984'
        img = 'https://www.youtube.com/watch?v=qB09nrQ8C7E'
        bot.edit_message_text(  '<b>Гробик </b> \n \n Сложность - легко (но страшно) \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'hamok':
        
        im = 'https://yandex.ru/video/preview/5354231249204874346'
        img = 'https://www.youtube.com/watch?v=1NcO5WaTxPY'
        
        bot.edit_message_text(  '<b>Замок </b> \n \n Сложность - легко \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'x':
        
        im = 'https://yandex.ru/video/preview/4472560617699113118'
        img = 'https://www.youtube.com/watch?v=O81reAs5TqA'
        
        bot.edit_message_text(  '<b>X вылет </b> \n \n Сложность - тяжело \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'lanch':
        
        im = 'https://www.youtube.com/watch?v=J-r5EyDeFd8'
        img = 'https://rutube.ru/video/8368d676866f3ec050192135d8aae818/'
        
        bot.edit_message_text(  '<b>Лач гейнер </b> \n \n Сложность - легко (но страшно) \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html',  )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'lyna':
        
        im = 'https://rutube.ru/video/43a013cf71789d13156d8223338aa2b1/'
        img = 'https://www.youtube.com/watch?v=DZ5sOO55ICU'
        
        bot.edit_message_text(  '<b>Луна </b> \n \n Сложность - среднее \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'manki':
        
        im = 'https://www.youtube.com/watch?v=JTVbAfi0Pfs'
        
        
        bot.edit_message_text(  '<b>Манки </b> \n \n Сложность - легко \n  \n Видео: \n  \n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'olil':
        
        img = 'https://rutube.ru/video/d54799a773c69fc49702325012c6a9a6/'
        im = 'https://www.youtube.com/watch?v=8vFpPc73pTM'
        
        bot.edit_message_text(  '<b>Оли </b> \n \n Сложность - легко \n  \n Видео: \n  \n \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'podiomsperev':
        img = 'https://rutube.ru/video/2c7fd1cba4805e9abe2d25ee75202c99/'
        im = 'https://www.youtube.com/watch?v=K-REve-NCIQ'
        
        bot.edit_message_text(  '<b>Подъем с переворотом </b> \n \n Сложность - \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'perishko':
        
        img = 'https://rutube.ru/video/9f7b1b8d1345dd37b923da76a2a4652c/'
        im = 'https://www.youtube.com/watch?v=YdHL3GIu_g8'
        
        bot.edit_message_text(  '<b>Перышко </b> \n \n Сложность - среднее \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'perel180':
        
        img = 'https://www.youtube.com/watch?v=-e93kVQ1bNc'
        im = 'https://www.youtube.com/watch?v=_WfBcRbmnOY'
        
        bot.edit_message_text(  '<b>Перелет на 180 </b> \n \n Сложность - среднее \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'pistol':
        
        img = 'https://rutube.ru/video/2cc22389ea07d26ed839f2b34329943a/'
        im = 'https://rutube.ru/video/f1c2288b94b9f55e830ba0126aa4e87d/'
        
        bot.edit_message_text(  '<b>Пистолетик </b> \n \n Сложность - легко \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'rodeo':
        
        img = 'https://dzen.ru/video/watch/617980216d36b52873f4f067?f=video'
        
        
        bot.edit_message_text(  '<b>Родео </b> \n \n Сложность - среднее \n  \n Видео: \n  \n ' f'{img}\n  ', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'russ':
        
        img = 'https://vk.com/video216662736_165391716'
        im = 'https://ok.ru/video/222357164313'
        
        bot.edit_message_text(  '<b>Русские обороты </b> \n \n Сложность - сложно \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'sklepka':
        
        img = 'https://vk.com/video299044839_456239412'
        im = 'https://rutube.ru/video/e08507b7ea76f154bff2b314367ae04b/'
        
        bot.edit_message_text(  '<b>Склепка </b> \n \n Сложность - среднее \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'solnishko':
        
        img = 'https://rutube.ru/video/971429a599863c452fba77bbf5e403d7/'
        im = 'https://rutube.ru/video/67ca15bd70b3680c8315cfb3df39f4d5/'
        
        bot.edit_message_text(  '<b>Солнышко </b> \n \n Сложность - сложно \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'sanhir':
        
        img = 'https://vk.com/video-40377126_456260588'
        im = 'https://rutube.ru/video/5af9a7013ccb0720bc5ff1d4fc3c39e9/'
        
        bot.edit_message_text(  '<b>Санжировка </b> \n \n Сложность - среднее \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'stylv ':
        
        img = 'https://rutube.ru/video/de59ba3cae9cb99a77ff126cc3988d82/'
        im = 'https://dzen.ru/shorts/665b33e30abbc959455d8892?f=video'
        
        bot.edit_message_text(  '<b>Стульчик вперед </b> \n \n Сложность - Лекго(страшно) \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
        
    if callback.data == 'stylntehnich':
        
        img = 'https://ok.ru/video/89598265927'
        im = 'https://dzen.ru/video/watch/60a42bf22e52323856e5b42c?f=video'
        
        bot.edit_message_text(  '<b>Стульчик назад </b> \n \n Сложность -  Лекго(страшно) \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'skorp':
        
        img = 'https://rutube.ru/video/56b25fcac27491ff201f2f8eeacd4fa0/'
        im = 'https://dzen.ru/video/watch/6179872cb6e1f712e23ecdc6?f=video'
        
        bot.edit_message_text(  '<b>Скорпион </b> \n \n Сложность - Среднее \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'smer':
        
        img = 'https://rutube.ru/video/6694d7ac4ba03f3b064af28d6aa079f1/'
        im = 'https://ok.ru/video/12465605140'
        
        bot.edit_message_text(  '<b>Смертник </b> \n \n Сложность - Среднее \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'finsk':
        
        img = 'https://vk.com/video-10768183_138681819?ysclid=m0tqu26h4y432483897'
        im = 'https://rutube.ru/video/4bf6ce278812cf6e9c092c625911668a/?ysclid=m0tqut3f1b412470913'
        
        bot.edit_message_text(  '<b>Финские обороты </b> \n \n Сложность - сложно \n  \n Видео: \n  \n ' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == '360':
        
        img = 'https://rutube.ru/video/44e1ce89fda628558ab02593fac3dad3/'
        im = 'https://rutube.ru/video/694995270f2410e1111cf2b93f89f971/'
        
        bot.edit_message_text(  '<b>360 </b> \n \n Сложность - среднее \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == '360ypor':
        
        img = 'https://rutube.ru/video/548aee982f63562999e57eb7f1e9f9da/'
        im = 'https://www.youtube.com/watch?v=pgPlBdhfbLY'
        
        bot.edit_message_text(  '<b>360 из упора </b> \n \n Сложность - среднее \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='afdu'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
        
        
        
    if callback.data == 'angel':
        
        img = 'https://vk.com/video129381027_456239446'
        im = 'https://www.youtube.com/watch?v=o3yCwYm8fuc'
        
        bot.edit_message_text(  '<b>Выход Ангела</b> \n \n Сложность - Сложное \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'v1':
        
        img = 'https://rutube.ru/video/c7b56cf78b92f8ce976b9a862c7640a2/'
        im = 'https://www.youtube.com/watch?v=chuxif0XVTY'
        
        bot.edit_message_text(  '<b>Выход на одну</b> \n \n Сложность - Легко \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'v2':
        
        img = 'https://www.youtube.com/watch?v=EHcAgOsozww'
        im = 'https://rutube.ru/video/8fe7b562134d65dd706ce735f6bb172b/'
        bot.edit_message_text(  '<b>Выход на две</b> \n \n Сложность - Среднее \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'v3':
        
        img = 'https://www.youtube.com/watch?v=6xuD8qUOJTo'
        im = 'https://www.youtube.com/watch?v=2xM8-zaZRuc'
        bot.edit_message_text(  '<b>Выход на три</b> \n \n Сложность - Легко \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'v4':
        
        img = 'https://www.youtube.com/watch?v=V5hBHX8VSYk'
        im = 'https://rutube.ru/video/185e9f712a37c0cba9db999fefd29f50/'
        bot.edit_message_text(  '<b>Выход на четыре</b> \n \n Сложность - Легко \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'vperedpech2':
        
        img = 'https://www.youtube.com/watch?v=HMWlNuHDw_4'
        im = 'https://rutube.ru/video/b5ed7fc0d268b3746b166ce76fdc8e9c/'
        bot.edit_message_text(  '<b>печатная машинка</b> \n \n Сложность - Среднее \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'ispan':
        
        img = 'https://rutube.ru/video/91e61a7c6018361e343def51c8d7a465/'
        im = 'https://www.youtube.com/watch?v=HoOrVIzt8SU'
        bot.edit_message_text(  '<b>Испанский выход</b> \n \n Сложность - Сложное \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'ital':
        
        img = 'https://www.youtube.com/watch?v=b65Obrj305Q'
        im = 'https://www.youtube.com/watch?v=tXLXH5Yq9TU'
        bot.edit_message_text(  '<b>Итальянский выход</b> \n \n Сложность - Сложное \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'ispodternika':
        
        img = 'https://rutube.ru/video/2cf507717108794f0a73bb6aa61ff6a9/'
        im = 'https://rutube.ru/video/5fb641817b9bf806c4067de5030c39c1/'
        bot.edit_message_text(  '<b>Выход из под турника</b> \n \n Сложность - Среднее \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'kitfayer':
        
        img = 'https://www.youtube.com/watch?v=K4hJWkvsW6o'
        
        bot.edit_message_text('<b>Кит фуэрзе</b> \n \n Сложность - Среднее \n  \n Видео: \n  \n' f'{img}\n' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'kapit':
        
        img = 'https://www.youtube.com/watch?v=J2EXYcAtZoQ'
        im = 'https://rutube.ru/video/267728d9b0a7e57a5ff360a7429ba3dd/'
        bot.edit_message_text(  '<b>Капитанский выход</b> \n \n Сложность - Легко \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'krab':
        
        img = 'https://www.youtube.com/watch?v=pJa_2O7t1Rg'
        im = 'https://www.youtube.com/watch?v=dqg13soiOw0'
        bot.edit_message_text(  '<b>Крабик</b> \n \n Сложность - Легко \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'ofis':
        
        img = 'https://www.youtube.com/watch?v=FgpKC1H-nm0'
        im = 'https://www.youtube.com/watch?v=FZpEycdRJsg'
        bot.edit_message_text(  '<b>Офицерский</b> \n \n Сложность - Среднее \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'polotence':
        
        img = 'https://www.youtube.com/watch?v=VStAOFNwAVY'
        im = 'https://rutube.ru/video/27ddaae35a127a8dc6c463d78a10b646/'
        bot.edit_message_text(  '<b>Полотенце</b> \n \n Сложность - Среднее \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'princ1':
        
        img = 'https://www.youtube.com/watch?v=MpqeH3HYpdw'
        bot.edit_message_text(  '<b>Принц на одну руку</b> \n \n Сложность - Сложное \n  \n Видео: \n  \n' f'{img}\n  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'princ2':
        
        im = 'https://www.youtube.com/watch?v=15Kb3aGt1Is'
        img = 'https://ok.ru/video/222355591449'
        bot.edit_message_text(  '<b>Приц на две руки</b> \n \n Сложность - Сложное \n  \n Видео: \n  \n' f'{img}\n  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'fenix':
        
        im = 'https://rutube.ru/video/48e15fac36ea25dba39a11d41764f027/'
        img = 'https://www.youtube.com/watch?v=xDjkPkkt5RQ'
        bot.edit_message_text(  '<b>Феникс</b> \n \n Сложность - Легко \n  \n Видео: \n  \n' f'{img}\n  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'filin':
        
        im = 'https://rutube.ru/video/073acde38d01cc6743d15dcbfc593ffe/'
        img = 'https://www.youtube.com/watch?v=tPP6_0tlPBU'
        bot.edit_message_text(  '<b>Филин</b> \n \n Сложность - Среднее \n  \n Видео: \n  \n' f'{img}\n  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='vidh'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
        
        
        
        #упр на тур
    
    if callback.data == 'bihe':
        
        im = 'https://rutube.ru/video/25e9f520112b0504ea2be1871b682fa0/'
        
        bot.edit_message_text(  '<b>Бицепс</b> \n \n Упражнения: \n\n 1) Подтягивания узким хватом. \n  2) Подтягивания параллельным хватом. \n \n Советы: \n \n Увеличивайте нагрузку лишь тогда, когда за подход вы сделали 15 повторений по 3 подхода. \n \n Использовать дополнительный вес. \n \n' f'{im}  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='ypdr'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
        
    if callback.data == 'trih':
        
        im = 'https://www.youtube.com/watch?v=sz5hD4b9QpE'
        
        bot.edit_message_text(  '<b>Трицепс</b> \n \n Упражнения: \n 1) Боковые подтягивания. \n  2) Выход силой. \n \n Советы:  \n Лучше тренеровать трицепс на брусьях, тк она там больше задействуется  \n' f'{im}  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='ypdr'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
    if callback.data == 'plechi':
        
        im = 'https://www.youtube.com/watch?v=EXUBrWusMAI'
        
        bot.edit_message_text(  '<b>Плечи</b> \n \n Упражнения: \n 1) Подтягивание средним хватом. \n  2) Подтягивания широким хватом. \n \n Советы: \n Перед выполнением упражнений рекомендуется сделать разминку на 7–10 минут \n' f'{im}  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='ypdr'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
    if callback.data == 'press':
        
        im = 'https://www.youtube.com/watch?v=uPGL0vytsgY'
        
        bot.edit_message_text(  '<b>Пресс</b> \n \n Упражнения: \n 1) Одновременный подъём коленей. \n  2) Подтягивания параллельным хватом. \n 3) Боковые подъемы. \n \n Советы: \n Качайте пресс таким образом 2–3 раза в неделю, постепенно увеличивая число повторений каждого упражнения и частоту тренировок.  \n' f'{im}  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='ypdr'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
    if callback.data == 'spina':
        
        im = 'https://www.youtube.com/watch?v=fuhzBptJlOY'
        
        bot.edit_message_text(  '<b>Спина</b> \n \n Упражнения: \n 1) Подтягивания на турнике за голову широким хватом. \n  2) Подтягивания к груди широким хватом. \n \n Советы: \n Беритесь за перекладину пальцами от себя. \n \n Чем шире делать хват, тем сильнее нагрузка на спину. \n' f'{im}  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='ypdr'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
    if callback.data == 'yprb': # упражнения для турника
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Трицепсы', callback_data='tril1' ))
        markup.add(types.InlineKeyboardButton('Большие грудные мышцы', callback_data='bolshie'))
        markup.add(types.InlineKeyboardButton('Пресс', callback_data='pressc' ))
        markup.add(types.InlineKeyboardButton('Назад', callback_data='b'))
        bot.edit_message_text('Отлично, теперь выберете:' , callback.message.chat.id , callback.message.message_id  , reply_markup=markup )
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
        
    if callback.data == 'tril1':
        
        im = 'https://www.youtube.com/watch?v=L8mD7Hl0bHE&t=1s'
        
        bot.edit_message_text(  '<b>Трицепс</b> \n \n Упражнения: \n 1) Отжимание на брусьях \n   \n \n Советы:  \n Выполняйте правильную технику. \n\n Когда будете делать +15-20 раз начинайте отжиматься с доп весом (с небольшим и понемногу увеличивайте).  \n' f'{im}  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='yprb'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
    if callback.data == 'bolshie':
        
        im = 'https://www.youtube.com/watch?v=3OHxIrMOGLU'
        
        bot.edit_message_text(  '<b>Большие грудные мышцы</b> \n \n Упражнения: \n 1) Отжимания на брусьях с наклоном корпуса \n   \n \n Советы:  \n Выполняйте правильную технику. \n\n Когда будете делать +15-20 раз начинайте отжиматься с доп весом (с небольшим и понемногу увеличивайте).  \n' f'{im}  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='yprb'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
    if callback.data == 'pressc':
        
        im = 'https://www.youtube.com/watch?v=5b7vCESfuvM'
        
        bot.edit_message_text(  '<b>Пресс</b> \n \n Упражнения: \n 1) Подъём согнутых ног в упоре на брусьях на локтях \n   \n 2) Уголок \n   \n \n Советы:  \n Выполняйте правильную технику.   \n' f'{im}  ' , callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='yprb'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
    if callback.data == 'aldb': # элементы для турника
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Задний кувырок в упор', callback_data='zadn'))
        markup.add(types.InlineKeyboardButton('Перелёт на брусьях ноги врозь на махе вперёд', callback_data='perelnabr'))
        markup.add(types.InlineKeyboardButton('Разворот на 180', callback_data='prok'))
        markup.add(types.InlineKeyboardButton('Склепка на брусьях', callback_data='prok'))
        markup.add(types.InlineKeyboardButton('270 на махи из упора вниз', callback_data='270'))
        markup.add(types.InlineKeyboardButton('Назад', callback_data='b'))
        bot.edit_message_text('Отлично, теперь выберете: \n А-Я' , callback.message.chat.id , callback.message.message_id  , parse_mode='html', reply_markup=markup )
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
        
    if callback.data == 'zadn':
        
        img = 'https://rutube.ru/video/9a902aef812080c6db94e2e75f1e888f/'
        im = 'https://www.youtube.com/watch?v=OMaiGPnZt80'
        
        bot.edit_message_text(  '<b>Задний кувырок в упор</b> \n \n Сложность - Легко \n  \n Видео: \n  \n' f'{img}\n  ' f' \n{im}', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='aldb'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
    if callback.data == '270':
        
        img = 'https://rutube.ru/video/2f78a460d517f8f209baf240a22ae92d/'
        
        
        bot.edit_message_text(  '<b>270 на махи из упора вниз</b> \n \n Сложность - Легко \n  \n Видео: \n  \n' f'{img}\n  ', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='aldb'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
    if callback.data == 'perelnabr':
        
        img = 'https://www.youtube.com/watch?v=vobJlgFThqU&list=PL-nd7yucCdgOYFtCVvJbUK66O3RP_9UVu&index=2'
        
        
        bot.edit_message_text(  '<b>Перелёт на брусьях ноги врозь на махе вперёд</b> \n \n Сложность - Сложно \n  \n Видео: \n  \n' f'{img}\n  ', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='aldb'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
    if callback.data == 'prok':
        
        img = 'https://www.youtube.com/watch?v=uN67-9qTgrA'
        
        
        bot.edit_message_text(  '<b>Склепка на брусьях</b> \n \n Сложность - Среднее \n  \n Видео: \n  \n' f'{img}\n  ', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='aldb'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
    if callback.data == '270':
        
        img = 'https://www.youtube.com/watch?v=8NA3YZUoTgE'
        
        
        bot.edit_message_text(  '<b>Разворот на 180</b> \n \n Сложность - Среднее \n  \n Видео: \n  \n' f'{img}\n  ', callback.message.chat.id ,  callback.message.message_id  , parse_mode='html' )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Назад', callback_data='aldb'))
        
        
        bot.send_message(callback.message.chat.id, f'{reklama}\n{imgx}' , reply_markup=markup)
        
bot.polling(none_stop=True)