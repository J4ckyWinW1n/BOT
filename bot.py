# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from vk_api import VkUpload
import requests
import vk, urllib.request
import wikipedia
wikipedia.set_lang("RU")
import datetime, time


def main():
    session = requests.Session()
    login, password = '89520089626', 'Urfreedomisalieqwerty1234'
    vk_session = vk_api.VkApi(login, password)

    attachments =[]

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    for event in longpoll.listen():

        del attachments[:]

#future valakas=[https://vk.com/photo-65249820_456277908?rev=1,https://pp.userapi.com/c846416/v846416863/28637/ot9bO0EhbJ0.jpg]
        
        today = datetime.datetime.today()
        now = str(today.strftime("%H:%M"))

        if '22:54' == str(now):
            upload = VkUpload(vk_session)
            VALAKAS = ['https://pp.userapi.com/c847016/v847016524/2f9ff/TJEE25JMXTA.jpg']
            image_url = random.choice(VALAKAS)
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachments.append(
            'photo{}_{}'.format(photo['owner_id'], photo['id'])
                )
            vk.messages.send(user_id=188815177, attachment=','.join(attachments))
            vk.messages.send(user_id=225332749, attachment=','.join(attachments))
            vk.messages.send(user_id=292563182, attachment=','.join(attachments))
            vk.messages.send(chat_id=3, attachment=','.join(attachments))
            time.sleep(70)
            del attachments [:]


        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print('Новое сообщение:')
            if 'Привет' in event.text.split() or 'привет' in event.text.split() or 'Прив' in event.text.split() or 'прив' in event.text.split(): #Если написали заданную фразу
                hello= ['Здравствуй, солнышко&#127773;','Приветики&#127773;','Прив)','Хай','Привет']
                if event.from_user: #Если написали в ЛС
                    vk.messages.send(user_id=event.user_id, message=random.choice(hello))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message=random.choice(hello))

            if ('Кто' in event.text.split() or 'кто' in event.text.split()) and ('ты' in event.text.split() or 'ты?' in event.text.split()): #Если написали заданную фразу
                if event.from_user: #Если написали в ЛС
                    vk.messages.send(user_id=event.user_id, message='Я ИИ спроектированный русским хакером-школьником которому нечего делать!')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='Я ИИ спроектированный русским хакером-школьником которому нечего делать!')

            if 'Шо?' in event.text.split() or 'Каво?' in event.text.split() or 'шо?' in event.text.split() or 'каво?' in event.text.split() or 'Шо' in event.text.split() or 'Каво' in event.text.split() or 'шо' in event.text.split() or 'каво' in event.text.split():
                if event.from_user: 
                    vk.messages.send(user_id=event.user_id, message='Не слишу')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='Не слишу')

            if ('Как' in event.text.split() or 'как' in event.text.split()) and ('дела' in event.text.split() or 'дела?' in event.text.split() or 'настроение' in event.text.split() or 'настроение?' in event.text.split()):
                business=['У меня всё как всегда чики-брики!', 'Замечательно', 'Норм', 'Всё кул']
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message=random.choice(business))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message=random.choice(business))

            if 'Круто' in event.text.split() or 'круто' in event.text.split() or 'Прикольно' in event.text.split() or 'прикольно' in event.text.split():
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message='да')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='да')

            if ('Лол' in event.text.split() or 'лол' in event.text.split() or 'LOL' in event.text.split() or 'кек' in event.text.split() or 'Кек' in event.text.split() or 'kek' in event.text.split()):
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message='лол&#127770;')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='лол&#127770;')

            if 'Спокойной' in event.text.split() or 'спокойной' in event.text.split() and 'ночи' in event.text.split():
                night = ['Спокойной ночи, зайка&#128007;&#128536;', 'Споки', 'Спи уже!']
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message=random.choice(night))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message=random.choice(night))

            if ('Что' in event.text.split() or 'Как' in event.text.split() or 'что' in event.text.split() or 'как' in event.text.split()) and ('думаешь' in event.text.split() or 'думаешь?' in event.text.split()):
                mind = ['Думаю да','Думаю нет']
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message=random.choice(mind))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message=random.choice(mind))

            if 'Тупая' in event.text.split() or 'тупая' in event.text.split() or 'Шлюха' in event.text.split() or 'шлюха' in event.text.split() or 'Дура' in event.text.split() or 'дура' in event.text.split() or 'Сука' in event.text.split() or 'сука' in event.text.split() or 'Тупая!' in event.text.split() or 'тупая!' in event.text.split() or 'Шлюха!' in event.text.split() or 'шлюха!' in event.text.split() or 'Дура!' in event.text.split() or 'дура!' in event.text.split() or 'Сука!' in event.text.split() or 'сука!' in event.text.split():
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message='Сам такой&#128545;')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='Сам такой&#128545;')

            if 'Сколько' in event.text.split() or 'сколько' in event.text.split():
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message = random.randint(0,100))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message = random.randint(0,100))

            if 'кей-поп' in event.text.split() or 'Кей-поп' in event.text.split() or 'Гей-поп' in event.text.split() or 'Кей' in event.text.split() or 'кей' in event.text.split():
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message='УБЕРИТЕ ОТ МЕНЯ ЭТУ ЕРЕСЬ&#128545;&#128545;&#128545;')
                elif event.from_chat: 
                    vk.messages.send(chat_id=event.chat_id, message='УБЕРИТЕ ОТ МЕНЯ ЭТУ ЕРЕСЬ&#128545;&#128545;&#128545;')

            if ('Лер' in event.text.split() or 'Лера' in event.text.split() or 'Лер,' in event.text.split() or 'Лера,' in event.text.split()) and ('симпампулькина' in event.text.split() or 'красотка' in event.text.split() or 'супер' in event.text.split() or 'СУПЕР!' in event.text.split() or 'супер!' in event.text.split()) and ('ты' in event.text.split() or 'Ты' in event.text.split()):
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message='Божечки-Кошечки, спасибо, Лапуля&#128561;&#128536;&#128525;')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message='Божечки-Кошечки, спасибо, Лапуля&#128561;&#128536;&#128525;') 

            if ('Спасибо' in event.text.split() or 'спасибо' in event.text.split() or 'Спасибо,' in event.text.split() or 'спасибо,' in event.text.split()) and ('Лера' in event.text.split() or 'Лер' in event.text.split()):
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message = 'Пожалуйста&#128521;')
                if event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message = 'Пожалуйста&#128521;')



            if ((event.text.split()[0] == 'Лер,' or event.text.split()[0] == 'Лер' or event.text.split()[0] == 'Лера' or event.text.split()[0] == 'Лера,') and event.text.split()[1] == 'выбери' and 'или' in event.text.split()) and not 'жопу' in event.text.split():

                choice1=[]
                choice2=[]
                for i in range(2, len(event.text.split())-2):
                    if event.text.split()[i] != 'или':
                        choice1.append(event.text.split()[i])
                    if event.text.split()[i] =='или':
                        break
                for i in range(event.text.split().index('или')+1,len(event.text.split())):
                    choice2.append(event.text.split()[i])
                choice = [choice1, choice2]
                sentence = ' '.join(random.choice(choice))
                sentence = 'Я думаю ' + sentence
                
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message = sentence)
                if event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message = sentence)


            if ('Что' in event.text.split() or 'что' in event.text.split() or 'Кто' in event.text.split() or 'кто' in event.text.split()) and ('такое' in event.text.split() or 'такой' in event.text.split() or 'такая' in event.text.split() or 'такие' in event.text.split() or 'значит' in event.text.split()) and ('Лер,' in event.text.split() or 'Лер' in event.text.split() or 'лер' in event.text.split() or 'лер,' in event.text.split() or 'Лера' in event.text.split() or 'Лера,' in event.text.split()):
                question = []
                if 'такой' in event.text.split():
                    wordforwiki = 'такой'
                if 'такая' in event.text.split():
                    wordforwiki = 'такая'
                if 'такое' in event.text.split():
                    wordforwiki = 'такое'
                if 'такие' in event.text.split():
                    wordforwiki = 'такие'
                if 'значит' in event.text.split():
                    wordforwiki = 'значит'
                for i in range(event.text.split().index(wordforwiki)+1, len(event.text.split())):
                    question.append(event.text.split()[i])
                question = ' '.join(question)
                if event.from_user:
                    vk.messages.send(user_id=event.user_id, message=str(wikipedia.summary(question)))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, message=str(wikipedia.summary(question)))


            if 'Хочу' in event.text.split() or 'Хачу' in event.text.split() or 'хочу' in event.text.split() or 'хачу' in event.text.split() :

                upload = VkUpload(vk_session)
                want = ['http://risovach.ru/upload/2018/09/mem/chernyy-vlastelin_187957114_orig_.jpg', 'http://risovach.ru/upload/2018/10/mem/negr-gey_189531438_orig_.jpg']

                image_url = random.choice(want)
                image = session.get(image_url, stream=True)
                photo = upload.photo_messages(photos=image.raw)[0]
                attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))

                if event.from_user:
                    vk.messages.send(user_id=event.user_id, attachment=','.join(attachments))
                elif event.from_chat:
                    vk.messages.send(user_id=event.user_id, attachment=','.join(attachments))
                del attachments [:]

            if 'сиськи' in event.text.split() or 'Сиськи' in event.text.split() or 'Жопу' in event.text.split() or 'жопу' in event.text.split() or 'Киску' in event.text.split() or 'киску' in event.text.split() or 'Писку' in event.text.split() or 'писку' in event.text.split() or (('Слава' in event.text.split() or 'слава' in event.text.split()) and ('Украине' in event.text.split() or 'Украине!' in event.text.split() or 'украине' in event.text.split())):

                upload = VkUpload(vk_session)
                url = ['https://pp.userapi.com/c846417/v846417401/8364f/N6xC0vvsJsI.jpg']

                image_url = random.choice(url)
                image = session.get(image_url, stream=True)
                photo = upload.photo_messages(photos=image.raw)[0]
                attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))

                if event.from_user:
                    vk.messages.send(user_id=event.user_id, attachment=','.join(attachments), message='ЧЕВО?!&#128563;')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, attachment=','.join(attachments), message='ЧЕВО?!&#128563;')
                del attachments [:]

            if ('Лер,' in event.text.split() or 'Лер' in event.text.split() or 'Лера,' in event.text.split() or 'Лера' in event.text.split()) and 'покажи' in event.text.split() and 'свой' in event.text.split() and 'кустарник' in event.text.split() and 'смородины' in event.text.split():
                upload = VkUpload(vk_session)
                picib=['https://b.radikal.ru/b33/1811/3a/b78218144c32.jpg','https://b.radikal.ru/b08/1811/78/2c0b06976846.jpg','https://c.radikal.ru/c19/1811/4e/3f76b0cb988c.jpg','https://c.radikal.ru/c28/1811/bf/5a5fddaff1d9.jpg','https://c.radikal.ru/c31/1811/3f/030b9b7e3fca.jpg','https://b.radikal.ru/b15/1811/c3/65d4035b98e7.jpg','https://d.radikal.ru/d09/1811/04/47af49e0ab00.jpg','https://a.radikal.ru/a31/1811/25/b5a343dfc384.jpg','https://a.radikal.ru/a05/1811/27/332d49161edd.jpg','https://b.radikal.ru/b08/1811/d2/c9de4cb464e2.jpg','https://d.radikal.ru/d11/1811/4a/94b3017b122b.jpg','https://d.radikal.ru/d14/1811/66/ec49ced7d367.jpg','https://c.radikal.ru/c13/1811/6d/70d313e6c982.jpg','https://d.radikal.ru/d06/1811/f9/159a29ec4d9e.jpg','https://a.radikal.ru/a28/1811/2d/1563899967da.jpg','https://c.radikal.ru/c18/1811/68/783144d58bd9.jpg','https://a.radikal.ru/a11/1811/ec/228f51c70653.jpg','https://c.radikal.ru/c39/1811/ee/c15f5fc5cc81.jpg','https://d.radikal.ru/d17/1811/57/fb5d16ea5b7c.jpg','https://a.radikal.ru/a04/1811/ac/6f864fdb9435.jpg','https://d.radikal.ru/d16/1811/58/04aed5e20539.jpg','https://c.radikal.ru/c38/1811/f3/15acfb911e65.jpg','https://d.radikal.ru/d31/1811/30/f84d640c6754.jpg','https://d.radikal.ru/d34/1811/05/c3ce43504400.jpg','https://d.radikal.ru/d02/1811/b3/7e3babc447cf.jpg','https://a.radikal.ru/a05/1811/57/9a0f94169bec.jpg','https://d.radikal.ru/d08/1811/dc/43b476bf1baf.jpg','https://d.radikal.ru/d35/1811/a1/1221012c0b29.jpg','https://b.radikal.ru/b13/1811/b4/575211e47bff.jpg','https://c.radikal.ru/c09/1811/f9/15b1d21593c1.jpg','https://c.radikal.ru/c40/1811/07/f1ab186fbc75.jpg','https://c.radikal.ru/c42/1811/db/039668255e35.jpg','https://d.radikal.ru/d30/1811/9e/786842b5bed9.jpg','https://a.radikal.ru/a05/1811/71/00da382b2cf9.jpg','https://c.radikal.ru/c17/1811/12/9b474f21a826.jpg','https://c.radikal.ru/c00/1811/46/e39a64a143b8.jpg','https://b.radikal.ru/b41/1811/f3/473b6f4c0d41.jpg','https://d.radikal.ru/d03/1811/77/b086c4b5a9fb.jpg','https://d.radikal.ru/d40/1811/be/bbdef7adc5ad.jpg','https://c.radikal.ru/c23/1811/b9/4d77cd9a94a2.jpg','https://d.radikal.ru/d17/1811/cf/9d38b7710748.jpg','https://b.radikal.ru/b39/1811/5f/212a036bb70b.jpg','https://a.radikal.ru/a33/1811/c1/400b24899cf1.jpg','https://d.radikal.ru/d01/1811/fc/49e1d05013c4.jpg', 'https://c.radikal.ru/c19/1811/a7/552421d5ca17.jpg', 'https://a.radikal.ru/a15/1811/0f/9113fb2724e9.jpg', 'https://a.radikal.ru/a33/1811/23/6d775a7a9d0a.jpg', 'https://c.radikal.ru/c14/1811/df/f5d65ba29540.jpg', 'https://a.radikal.ru/a35/1811/5d/b5b9a5d85744.jpg', 'https://a.radikal.ru/a04/1811/24/b03da97090a1.jpg', 'https://a.radikal.ru/a16/1811/82/820d725ab8bc.jpg', 'https://a.radikal.ru/a34/1811/82/a26bf7abfde8.jpg', 'https://b.radikal.ru/b12/1811/ab/709b5190cf88.jpg', 'https://b.radikal.ru/b24/1811/9b/0004804a7d15.jpg', 'https://b.radikal.ru/b29/1811/2e/6e625fc4791d.jpg', 'https://d.radikal.ru/d07/1811/6a/9b413a092f99.jpg', 'https://d.radikal.ru/d03/1811/fa/2a23319834f5.jpg', 'https://a.radikal.ru/a00/1811/2a/e8484200fcfb.jpg', 'https://d.radikal.ru/d12/1811/c8/eddb1a80fa77.jpg', 'https://b.radikal.ru/b42/1811/f2/de13b46292b4.jpg', 'https://a.radikal.ru/a04/1811/a7/64b03a1928e6.jpg', 'https://a.radikal.ru/a16/1811/c1/f0d823720696.jpg', 'https://a.radikal.ru/a22/1811/f7/80edc34df1d5.jpg', 'https://b.radikal.ru/b35/1811/13/65ac7bc57846.jpg', 'https://b.radikal.ru/b12/1811/e0/53ffaeb96e40.jpg', 'https://a.radikal.ru/a15/1811/db/5e5fe7eb4b7f.jpg', 'https://a.radikal.ru/a01/1811/87/ceb7f5465b6a.jpg', 'https://c.radikal.ru/c29/1811/28/5075ce72f866.jpg', 'https://b.radikal.ru/b16/1811/d9/efbdecc1e946.jpg', 'https://a.radikal.ru/a28/1811/ce/6df729c239ad.jpg', 'https://d.radikal.ru/d43/1811/2a/7cae6bc0de05.jpg', 'https://a.radikal.ru/a11/1811/e0/45af3f92f86a.jpg', 'https://b.radikal.ru/b23/1811/a2/336872ac759f.jpg', 'https://a.radikal.ru/a19/1811/f8/4a17d1d8d057.jpg', 'https://d.radikal.ru/d19/1811/fc/4ba9f8a75c81.jpg', 'https://b.radikal.ru/b12/1811/44/c5d9ea4194e5.jpg', 'https://c.radikal.ru/c43/1811/e6/06f199179071.jpg', 'https://c.radikal.ru/c11/1811/43/21aa88291a2c.jpg', 'https://a.radikal.ru/a39/1811/29/4c7aa0f51c33.jpg', 'https://a.radikal.ru/a17/1811/55/39d112e03fd6.jpg', 'https://a.radikal.ru/a10/1811/7c/d0877038f212.jpg', 'https://d.radikal.ru/d32/1811/18/9b1a5a06a712.jpg', 'https://c.radikal.ru/c25/1811/08/6436013214df.jpg', 'https://b.radikal.ru/b22/1811/8b/05e8c072786f.jpg', 'https://a.radikal.ru/a15/1811/74/e028a18b9436.jpg', 'https://d.radikal.ru/d27/1811/89/4e4c4d711abf.jpg', 'https://d.radikal.ru/d20/1811/81/974ae73e1e0f.jpg', 'https://a.radikal.ru/a23/1811/46/f31f3e1d7670.jpg', 'https://c.radikal.ru/c16/1811/9a/3537f9c72f12.jpg', 'https://b.radikal.ru/b23/1811/b0/9e6a5c6aa279.jpg', 'https://b.radikal.ru/b25/1811/c6/7e756e813f6f.jpg', 'https://a.radikal.ru/a28/1811/6a/d38835dbd420.jpg', 'https://a.radikal.ru/a21/1811/83/68832341f061.jpg', 'https://a.radikal.ru/a05/1811/cd/9008d7ea9283.jpg', 'https://c.radikal.ru/c17/1811/fa/2bd9459f3b12.jpg', 'https://c.radikal.ru/c29/1811/91/a2523010c539.jpg', 'https://b.radikal.ru/b07/1811/13/7b057783f82c.jpg', 'https://c.radikal.ru/c35/1811/2c/50422e94fc77.jpg', 'https://a.radikal.ru/a25/1811/b5/19e1aff6b194.jpg', 'https://c.radikal.ru/c08/1811/ac/f7c0e3a3c84f.jpg', 'https://c.radikal.ru/c14/1811/9a/b2a977ceb0d1.jpg', 'https://d.radikal.ru/d17/1811/d0/8ac6d79afed0.jpg', 'https://a.radikal.ru/a14/1811/bf/61792071b3dd.jpg', 'https://b.radikal.ru/b41/1811/c0/addb1c7d4a18.jpg', 'https://b.radikal.ru/b19/1811/02/966b7e2d83d3.jpg', 'https://c.radikal.ru/c37/1811/00/ae9472070376.jpg', 'https://b.radikal.ru/b21/1811/ac/ba3d7c67abe9.jpg', 'https://c.radikal.ru/c15/1811/1d/cb6d448ff68b.jpg', 'https://a.radikal.ru/a21/1811/89/4defee7510b3.jpg', 'https://b.radikal.ru/b07/1811/c4/824014a3c401.jpg', 'https://b.radikal.ru/b04/1811/8a/4d2435be5f48.jpg', 'https://d.radikal.ru/d19/1811/0a/f3030ad827c3.jpg', 'https://b.radikal.ru/b37/1811/2f/d387644c9dc4.jpg', 'https://d.radikal.ru/d30/1811/4b/eda9aaa21d24.jpg', 'https://a.radikal.ru/a43/1811/f0/815aafe59005.jpg', 'https://c.radikal.ru/c01/1811/5f/40a1fbf37bb6.jpg', 'https://d.radikal.ru/d41/1811/dc/90164cefc17c.jpg', 'https://b.radikal.ru/b03/1811/b1/1676422b3a58.jpg', 'https://b.radikal.ru/b14/1811/49/dc1c08d7e68a.jpg', 'https://a.radikal.ru/a17/1811/f0/8dfb199080c6.jpg', 'https://b.radikal.ru/b10/1811/c7/7cc7fe4fb1d7.jpg', 'https://d.radikal.ru/d12/1811/50/700eba2ffaa4.jpg', 'https://a.radikal.ru/a00/1811/e9/b7bc4b049923.jpg', 'https://d.radikal.ru/d40/1811/41/65baea75abb8.jpg', 'https://a.radikal.ru/a24/1811/94/9154169a381b.jpg', 'https://d.radikal.ru/d17/1811/6d/abfb4d6b70ff.jpg', 'https://d.radikal.ru/d20/1811/85/d71992835209.jpg', 'https://d.radikal.ru/d23/1811/09/70efd8136471.jpg', 'https://a.radikal.ru/a32/1811/6e/c38523dbd552.jpg', 'https://c.radikal.ru/c25/1811/59/0f1da2832996.jpg', 'https://b.radikal.ru/b38/1811/61/e811957c2fca.jpg', 'https://b.radikal.ru/b12/1811/f5/f16e414192a4.jpg', 'https://a.radikal.ru/a15/1811/2f/33de507f678c.jpg', 'https://d.radikal.ru/d37/1811/b6/88652c3021fa.jpg', 'https://a.radikal.ru/a15/1811/da/de07c127602e.jpg', 'https://a.radikal.ru/a08/1811/38/eb9d6a5a8b4f.jpg', 'https://c.radikal.ru/c36/1811/95/a897740767e9.jpg', 'https://c.radikal.ru/c10/1811/54/3deb57e420df.jpg', 'https://c.radikal.ru/c13/1811/87/f35c5dfb8d15.jpg', 'https://d.radikal.ru/d07/1811/99/222a5b83f632.jpg', 'https://d.radikal.ru/d34/1811/27/ed3c33d5c6f2.jpg', 'https://a.radikal.ru/a40/1811/9c/954e044be16d.jpg', 'https://d.radikal.ru/d28/1811/21/bd79f32dde0d.jpg', 'https://c.radikal.ru/c11/1811/1e/ada0d9325b45.jpg', 'https://a.radikal.ru/a14/1811/e2/18720f0dbbc1.jpg', 'https://c.radikal.ru/c01/1811/fb/a3998412c4f0.jpg', 'https://d.radikal.ru/d04/1811/a2/315027647183.jpg', 'https://b.radikal.ru/b34/1811/15/d7d6b4b8d2de.jpg', 'https://a.radikal.ru/a31/1811/ee/a0f896772505.jpg', 'https://b.radikal.ru/b14/1811/bb/f39e1f5d7d86.jpg', 'https://b.radikal.ru/b36/1811/e8/7c53812f5e44.jpg', 'https://c.radikal.ru/c20/1811/ac/3d062ad67878.jpg', 'https://d.radikal.ru/d13/1811/1c/1a52376166d0.jpg', 'https://c.radikal.ru/c10/1811/e3/a8f27ddda546.jpg', 'https://c.radikal.ru/c32/1811/24/99caa8d656fc.jpg', 'https://a.radikal.ru/a31/1811/ef/e5a26fd32b99.jpg', 'https://d.radikal.ru/d15/1811/3e/4e5b0a510941.jpg', 'https://d.radikal.ru/d11/1811/86/3e502ef04266.jpg', 'https://d.radikal.ru/d04/1811/db/bb65644653de.jpg', 'https://b.radikal.ru/b02/1811/81/395fb35a9c22.jpg', 'https://a.radikal.ru/a14/1811/c7/f847b8073807.jpg', 'https://b.radikal.ru/b07/1811/09/63efd34397f5.jpg', 'https://a.radikal.ru/a19/1811/02/cd1dba58a672.jpg', 'https://c.radikal.ru/c00/1811/21/f0afac3e00ea.jpg', 'https://c.radikal.ru/c43/1811/f9/b9ee23941c25.jpg', 'https://d.radikal.ru/d02/1811/7c/d62c3307a7f1.jpg', 'https://b.radikal.ru/b02/1811/e4/bbbd46f838f7.jpg', 'https://a.radikal.ru/a14/1811/66/74e50d1c787e.jpg', 'https://c.radikal.ru/c32/1811/73/a8e7fc673a94.jpg']

                image_url = random.choice(picib)
                image = session.get(image_url, stream=True)
                photo = upload.photo_messages(photos=image.raw)[0]
                attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))

                if event.from_user:
                    vk.messages.send(user_id=event.user_id, attachment=','.join(attachments), message='Держи, зайка!&#127815;&#127815;&#127815;')
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, attachment=','.join(attachments), message='Держи, зайка!&#127815;&#127815;&#127815;')
                del attachments [:]

            if 'Юри' in event.text.split() or 'юри' in event.text.split() or 'Юрей' in event.text.split() or 'юрей' in event.text.split():
                upload = VkUpload(vk_session)
                yuri = ['http://b.radikal.ru/b26/1811/24/d875d31139ed.jpg', 'http://a.radikal.ru/a37/1811/8d/7e753fcb998f.jpg', 'http://a.radikal.ru/a00/1811/ba/9f1189150b2c.jpg', 'http://d.radikal.ru/d18/1811/af/76710f6d443e.jpg', 'http://b.radikal.ru/b11/1811/9c/1ee8ff1e732c.jpg', 'http://d.radikal.ru/d14/1811/00/472b9153934a.jpg', 'http://c.radikal.ru/c01/1811/96/c8f2ee4c75c7.jpg', 'http://b.radikal.ru/b04/1811/20/9a83424173b3.jpg', 'http://c.radikal.ru/c03/1811/c1/51dbe8d223a9.jpg', 'http://d.radikal.ru/d26/1811/01/854325f9550c.jpg', 'http://a.radikal.ru/a19/1811/01/057fbbd03c8b.jpg', 'http://d.radikal.ru/d37/1811/8e/cb91fd4e1576.jpg', 'http://a.radikal.ru/a12/1811/53/c0850140498b.jpg', 'http://c.radikal.ru/c34/1811/1c/87c445fba3c9.jpg', 'http://b.radikal.ru/b36/1811/42/d664884d4a11.jpg', 'http://b.radikal.ru/b33/1811/b9/dd29ff2c57ac.jpg', 'http://c.radikal.ru/c16/1811/b4/f8eed61ca0fd.jpg', 'http://b.radikal.ru/b19/1811/4b/e6f22f8dcbe9.jpg', 'http://b.radikal.ru/b41/1811/58/d7ffa6011147.jpg', 'http://c.radikal.ru/c25/1811/0b/714247a4ab47.jpg', 'http://d.radikal.ru/d19/1811/7c/5d138e12f9e6.jpg', 'http://d.radikal.ru/d12/1811/f0/eab0cd237e45.jpg', 'http://c.radikal.ru/c40/1811/65/14efafc1606a.jpg', 'http://c.radikal.ru/c42/1811/1b/f7fe352b44c4.jpg', 'http://a.radikal.ru/a36/1811/f3/3cf539e5f3b5.jpg', 'http://a.radikal.ru/a05/1811/bf/0bb0c6c955a4.jpg', 'http://d.radikal.ru/d42/1811/98/efe9bd57333b.jpg', 'http://b.radikal.ru/b01/1811/51/b54bdba42dda.jpg', 'http://d.radikal.ru/d00/1811/9b/d64f4e537b34.jpg', 'http://d.radikal.ru/d38/1811/39/c3935dc3f14f.jpg', 'http://d.radikal.ru/d16/1811/46/6c093b537d6c.jpg', 'http://a.radikal.ru/a28/1811/90/a59e3bcf2598.jpg', 'http://a.radikal.ru/a40/1811/6b/2cb3cc1060f0.jpg', 'http://d.radikal.ru/d40/1811/a9/29bfe9ed2249.jpg', 'http://a.radikal.ru/a09/1811/41/efcf9e094e04.jpg', 'http://c.radikal.ru/c27/1811/fb/baf1636844d6.jpg', 'http://b.radikal.ru/b11/1811/45/7d71c9903ea1.jpg', 'http://d.radikal.ru/d04/1811/28/f0cbf0e79e6d.jpg', 'http://d.radikal.ru/d26/1811/30/0f626d2212f1.jpg', 'http://a.radikal.ru/a20/1811/19/bf8fa489987f.jpg', 'http://c.radikal.ru/c19/1811/c4/58d5aa4b1c1d.jpg', 'http://c.radikal.ru/c22/1811/75/457676bf2c3d.jpg', 'http://b.radikal.ru/b34/1811/2c/dc331faa2470.jpg', 'http://b.radikal.ru/b37/1811/96/546453fb8b02.jpg', 'http://d.radikal.ru/d02/1811/ab/c9a168b0210d.jpg', 'http://a.radikal.ru/a14/1811/f9/a2f120c94ddf.jpg', 'http://d.radikal.ru/d36/1811/b7/0d7cb67bae49.jpg', 'http://a.radikal.ru/a11/1811/59/91e06ce13cb0.jpg', 'http://b.radikal.ru/b14/1811/d5/d84445f82870.jpg', 'http://b.radikal.ru/b22/1811/a2/cc33cb703227.jpg', 'http://b.radikal.ru/b26/1811/db/1d3222bec67a.jpg', 'http://c.radikal.ru/c34/1811/6d/3e3a28087e3b.jpg', 'http://d.radikal.ru/d28/1811/9c/746dfbdab8db.jpg', 'http://b.radikal.ru/b21/1811/f4/e20d08efb55c.jpg', 'http://d.radikal.ru/d43/1811/1e/e5a12496323d.jpg', 'http://d.radikal.ru/d27/1811/60/196ed01464e7.jpg', 'http://a.radikal.ru/a21/1811/2e/54dcf38fde2b.jpg', 'http://a.radikal.ru/a33/1811/30/0b432b6d48e8.jpg', 'http://b.radikal.ru/b07/1811/c7/1409063306be.jpg', 'http://c.radikal.ru/c11/1811/0c/28c5e924db39.jpg', 'http://b.radikal.ru/b10/1811/b8/2f274f22ddf9.jpg', 'http://d.radikal.ru/d22/1811/b1/6b6c8acb9440.jpg', 'http://c.radikal.ru/c35/1811/ad/965e0e0cc43b.jpg', 'http://d.radikal.ru/d25/1811/83/37e9d2279cc2.jpg', 'http://b.radikal.ru/b37/1811/f5/92ab97188c85.jpg', 'http://c.radikal.ru/c22/1811/eb/6f3e30ff9497.jpg', 'http://a.radikal.ru/a15/1811/54/f35d2cd88443.jpg', 'http://a.radikal.ru/a34/1811/0d/dd8307928419.jpg', 'http://d.radikal.ru/d21/1811/c9/f53124de8def.jpg', 'http://c.radikal.ru/c05/1811/03/c0d1e24f8a3a.jpg', 'http://b.radikal.ru/b14/1811/43/e1b719a51d8b.jpg', 'http://c.radikal.ru/c18/1811/27/2f9bc8b0d225.jpg', 'http://d.radikal.ru/d20/1811/41/d9a5a20f1603.jpg', 'http://d.radikal.ru/d04/1811/ac/28c1e59e71c9.jpg', 'http://a.radikal.ru/a32/1811/75/f1c36ad33ccc.jpg', 'http://d.radikal.ru/d01/1811/d8/088e470a28e4.jpg', 'http://d.radikal.ru/d09/1811/fa/b406c50a80d6.jpg', 'http://b.radikal.ru/b03/1811/54/a128af93b757.jpg', 'http://c.radikal.ru/c06/1811/f7/e2831e1254c8.jpg', 'http://b.radikal.ru/b09/1811/0d/98d5655e8371.jpg', 'http://d.radikal.ru/d03/1811/de/50304a370268.jpg', 'http://c.radikal.ru/c31/1811/c0/3ec8e4d6f1db.jpg', 'http://d.radikal.ru/d21/1811/b9/618ba9d81d20.jpg', 'http://d.radikal.ru/d05/1811/18/28a8de233530.jpg', 'http://a.radikal.ru/a42/1811/3a/b8ecda3a7b5d.jpg', 'http://d.radikal.ru/d21/1811/05/86e955b69b97.jpg', 'http://b.radikal.ru/b04/1811/95/a1484e5ce5d9.jpg', 'http://a.radikal.ru/a23/1811/36/dbc22de9dff0.jpg', 'http://d.radikal.ru/d16/1811/9b/8fa824fa4cf1.jpg', 'http://b.radikal.ru/b10/1811/fe/f157950a3f5b.jpg', 'http://a.radikal.ru/a04/1811/c9/30f6e73f1de9.jpg', 'http://a.radikal.ru/a37/1811/b5/fca4cbafbcea.jpg', 'http://d.radikal.ru/d31/1811/01/8545ae451dad.jpg', 'http://b.radikal.ru/b40/1811/36/289d5f57097a.jpg', 'http://c.radikal.ru/c33/1811/0d/41cee927aa36.jpg', 'http://d.radikal.ru/d21/1811/5b/16c888486060.jpg', 'http://b.radikal.ru/b05/1811/9d/654db95b6cc0.jpg', 'http://a.radikal.ru/a33/1811/8f/528c6291a44b.jpg', 'http://b.radikal.ru/b01/1811/72/fdda2915c20f.jpg', 'http://b.radikal.ru/b38/1811/73/939d75f72e29.jpg', 'http://d.radikal.ru/d17/1811/04/28d566dcfdab.jpg', 'http://c.radikal.ru/c35/1811/38/a8f479dc62c0.jpg', 'http://b.radikal.ru/b29/1811/78/f09420a21264.jpg', 'http://c.radikal.ru/c03/1811/11/674790594728.jpg', 'http://d.radikal.ru/d06/1811/33/bcdd9d35f7ab.jpg', 'http://b.radikal.ru/b34/1811/e0/2c3097f9ef8c.jpg', 'http://b.radikal.ru/b08/1811/00/066085a3ed8d.jpg', 'http://b.radikal.ru/b11/1811/c4/653886ab96e6.jpg', 'http://c.radikal.ru/c39/1811/12/1b03b6565f87.jpg', 'http://b.radikal.ru/b08/1811/ba/312d3abb591c.jpg', 'http://d.radikal.ru/d01/1811/70/26fb3c4fdcef.jpg', 'http://c.radikal.ru/c10/1811/18/4261e9904412.jpg', 'http://c.radikal.ru/c13/1811/27/256c2cbe8723.jpg', 'http://d.radikal.ru/d31/1811/74/a5e60e514f7a.jpg', 'http://d.radikal.ru/d00/1811/1e/bedc3c4e3311.jpg', 'http://a.radikal.ru/a38/1811/9f/35ff70adf9e5.jpg', 'http://b.radikal.ru/b02/1811/6d/e49dc8efeb97.jpg', 'http://d.radikal.ru/d34/1811/c8/5ad93d72ae91.jpg', 'http://a.radikal.ru/a08/1811/30/d1a6bca167e9.jpg', 'http://c.radikal.ru/c27/1811/a3/bb7c1fd1e940.jpg', 'http://a.radikal.ru/a39/1811/3a/4727485cae0a.jpg', 'http://d.radikal.ru/d04/1811/ca/995ee4d3a0ea.jpg', 'http://a.radikal.ru/a26/1811/ff/1b49672be374.jpg', 'http://d.radikal.ru/d38/1811/0e/5aae5dfc41e5.jpg', 'http://a.radikal.ru/a32/1811/1a/9f0b27d1ca7f.jpg', 'http://d.radikal.ru/d16/1811/60/62fea163dde0.jpg', 'http://b.radikal.ru/b25/1811/30/b6f7881903bd.jpg', 'http://c.radikal.ru/c09/1811/9f/95ab9a09d8fe.jpg', 'http://d.radikal.ru/d12/1811/f5/1f80e9a35cbf.jpg', 'http://d.radikal.ru/d12/1811/fc/66373ca5497e.jpg', 'http://d.radikal.ru/d15/1811/83/b0290e60d3ec.jpg', 'http://c.radikal.ru/c43/1811/72/da2bbe757eef.jpg', 'http://c.radikal.ru/c27/1811/e2/1f65b3724ccf.jpg', 'http://c.radikal.ru/c11/1811/61/f80df5b5c363.jpg', 'http://a.radikal.ru/a20/1811/f8/4d8326c3ec75.jpg', 'http://a.radikal.ru/a07/1811/40/b7f3951c7378.jpg', 'http://c.radikal.ru/c26/1811/dd/8be07c2a9a8f.jpg', 'http://c.radikal.ru/c00/1811/ff/9bae404f7639.jpg', 'http://c.radikal.ru/c41/1811/02/a0ed0f7f6678.jpg', 'http://a.radikal.ru/a25/1811/63/239f27c73d7d.jpg', 'http://a.radikal.ru/a28/1811/8c/b0f594c02186.jpg', 'http://b.radikal.ru/b37/1811/93/e6f7d6cead0a.jpg', 'http://d.radikal.ru/d20/1811/62/600d81d46755.jpg', 'http://a.radikal.ru/a24/1811/06/c4ceba5bd72c.jpg', 'http://d.radikal.ru/d17/1811/d1/9978b5e36e1c.jpg', 'http://d.radikal.ru/d20/1811/20/1f5ea08abcf1.jpg', 'http://c.radikal.ru/c04/1811/29/c35512167821.jpg', 'http://a.radikal.ru/a03/1811/5b/50251e625576.jpg', 'http://a.radikal.ru/a32/1811/0d/7aaed0804451.jpg', 'http://c.radikal.ru/c10/1811/d9/edc5ad4925fa.jpg', 'http://b.radikal.ru/b18/1811/ac/2c0156ccc800.jpg', 'http://a.radikal.ru/a36/1811/f8/51a7e8a3f6ca.jpg', 'http://b.radikal.ru/b01/1811/de/25ab5d289d31.jpg', 'http://b.radikal.ru/b23/1811/1c/f5646507b457.jpg', 'http://d.radikal.ru/d32/1811/52/710cd45250fe.jpg', 'http://a.radikal.ru/a15/1811/b4/864ac286b3f5.jpg', 'http://c.radikal.ru/c38/1811/79/48fe6b66e2d7.jpg', 'http://b.radikal.ru/b31/1811/2f/b2a19b8711bb.jpg', 'http://c.radikal.ru/c24/1811/d4/803410159fe8.jpg', 'http://a.radikal.ru/a37/1811/2c/90dcb55e7d77.jpg', 'http://a.radikal.ru/a21/1811/e7/5aeca6040e60.jpg', 'http://c.radikal.ru/c30/1811/47/31f439f99071.jpg', 'http://a.radikal.ru/a06/1811/07/10c90b8da8b5.jpg', 'http://b.radikal.ru/b43/1811/58/13d1761d61d1.jpg', 'http://c.radikal.ru/c18/1811/ac/eed0a5da02cf.jpg', 'http://a.radikal.ru/a39/1811/8e/df6c9c25b024.jpg', 'http://a.radikal.ru/a17/1811/3a/3f8b1b1d3c18.jpg', 'http://a.radikal.ru/a38/1811/0d/16f0d4175808.jpg', 'http://a.radikal.ru/a04/1811/cd/eefdf5f0324e.jpg', 'http://c.radikal.ru/c41/1811/d5/8bafe530a6f1.jpg', 'http://c.radikal.ru/c16/1811/3c/5597282774bc.jpg', 'http://b.radikal.ru/b09/1811/39/f34f7fff414d.jpg', 'http://b.radikal.ru/b09/1811/83/d82c07caa37d.jpg', 'http://b.radikal.ru/b22/1811/52/fc997ac9a1ea.jpg', 'http://b.radikal.ru/b15/1811/7f/4a2614a820a4.jpg', 'http://d.radikal.ru/d18/1811/21/792cf11c8063.jpg', 'http://a.radikal.ru/a26/1811/e4/a1ed1ec49a95.jpg', 'http://b.radikal.ru/b30/1811/81/a8ea6f5975fa.jpg', 'http://d.radikal.ru/d13/1811/c1/383a438fef98.jpg', 'http://a.radikal.ru/a16/1811/35/10a7004f3de9.jpg', 'http://d.radikal.ru/d10/1811/13/397ffce87f75.jpg', 'http://a.radikal.ru/a32/1811/3a/84fa919c9acd.jpg', 'http://c.radikal.ru/c16/1811/76/502ca8195980.jpg', 'http://c.radikal.ru/c09/1811/5d/7844bd947c91.jpg', 'http://b.radikal.ru/b27/1811/c4/c8d371754c0e.jpg', 'http://d.radikal.ru/d34/1811/f9/25bde24102e7.jpg', 'http://c.radikal.ru/c33/1811/be/624feade62ca.jpg', 'http://a.radikal.ru/a11/1811/b7/0bd3694c3df0.jpg', 'http://a.radikal.ru/a30/1811/24/c50a7046006c.jpg', 'http://a.radikal.ru/a14/1811/e8/bbd9ffccf87e.jpg', 'http://d.radikal.ru/d07/1811/d3/e3aee4a72240.jpg', 'http://d.radikal.ru/d16/1811/9b/29dfe512eb5e.jpg', 'http://c.radikal.ru/c10/1811/db/b5b0492f6290.jpg', 'http://c.radikal.ru/c13/1811/fb/053ee6314f6d.jpg', 'http://a.radikal.ru/a41/1811/1b/b725ae4e9778.jpg', 'http://c.radikal.ru/c06/1811/8e/74ef4ae297ba.jpg', 'http://c.radikal.ru/c34/1811/1c/02f795c6e3ef.jpg', 'http://d.radikal.ru/d18/1811/bb/b50f1de2a7d8.jpg', 'http://d.radikal.ru/d21/1811/fb/7fd58dc9bd15.jpg', 'http://c.radikal.ru/c24/1811/f7/59091f0bb526.jpg', 'http://a.radikal.ru/a23/1811/01/8ad892b89bb8.jpg', 'http://d.radikal.ru/d11/1811/a2/a33b0bae0c39.jpg', 'http://d.radikal.ru/d19/1811/96/4cd393a5df5a.jpg', 'http://d.radikal.ru/d32/1811/4d/fc81c1cdf3ef.jpg', 'http://b.radikal.ru/b41/1811/d6/ed49429d52fe.jpg', 'http://a.radikal.ru/a25/1811/e2/44842d8ddcd0.jpg', 'http://c.radikal.ru/c00/1811/c0/34bacce49085.jpg', 'http://a.radikal.ru/a31/1811/13/04337c717454.jpg', 'http://c.radikal.ru/c00/1811/74/0ae0d3c86ad6.jpg', 'http://d.radikal.ru/d27/1811/b0/952f710ded43.jpg', 'http://a.radikal.ru/a21/1811/92/3827f2896463.jpg', 'http://d.radikal.ru/d24/1811/c6/4b16d3a7fb81.jpg', 'http://b.radikal.ru/b17/1811/37/4dd71b9ccf82.jpg', 'http://b.radikal.ru/b07/1811/a7/92e1bb36c113.jpg', 'http://b.radikal.ru/b39/1811/7c/f6675acfc602.jpg', 'http://c.radikal.ru/c13/1811/ed/d78c671e07de.jpg', 'http://c.radikal.ru/c22/1811/f8/3cecedce0b60.jpg', 'http://c.radikal.ru/c25/1811/88/3b3ee8712e7e.jpg', 'http://a.radikal.ru/a38/1811/a3/a15ee46c880f.jpg', 'http://b.radikal.ru/b31/1811/64/2d7c583fa8f4.jpg', 'http://d.radikal.ru/d06/1811/a9/bbe99582ffcf.jpg', 'http://b.radikal.ru/b24/1811/5f/95852722d201.jpg', 'http://a.radikal.ru/a36/1811/37/7571da3dcaf9.jpg', 'http://a.radikal.ru/a39/1811/c7/86d96b9d6f49.jpg', 'http://d.radikal.ru/d08/1811/5f/b201edcc0f07.jpg', 'http://a.radikal.ru/a01/1811/6a/b44760f160e0.jpg', 'http://d.radikal.ru/d00/1811/fd/2dd30d65c8fb.jpg', 'http://b.radikal.ru/b23/1811/69/6b94bc09b2de.jpg', 'http://d.radikal.ru/d06/1811/d1/5824e29109b0.jpg', 'http://d.radikal.ru/d00/1811/57/0b4dbfbf7300.jpg', 'http://d.radikal.ru/d03/1811/06/c594894cd0cf.jpg', 'http://b.radikal.ru/b31/1811/5e/0330192fcfb0.jpg']

                image_url = random.choice(yuri)
                image = session.get(image_url, stream=True)
                photo = upload.photo_messages(photos=image.raw)[0]
                attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))

                if event.from_user:
                    vk.messages.send(user_id=event.user_id, attachment=','.join(attachments), message='&#127770;')
                if event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, attachment=','.join(attachments), message='&#127770;')
                del attachments [:]

            if ('Лера,' in event.text.split() or 'Лера' in event.text.split() or 'Лер,' in event.text.split() or 'Лер' in event.text.split()) and 'посвяти' in event.text.split() and 'меня' in event.text.split() and 'в' in event.text.split() and 'свою' in event.text.split() and 'религию' in event.text.split():
                upload = VkUpload(vk_session)
                neko = ['https://a.radikal.ru/a17/1811/94/c9eab9267526.png', 'https://c.radikal.ru/c03/1811/f9/af86fb472662.png', 'https://c.radikal.ru/c25/1811/08/749f878fdd1f.jpg', 'https://d.radikal.ru/d00/1811/7a/2d2b507c1d15.jpg', 'https://a.radikal.ru/a02/1811/a2/8203d5526c17.jpg', 'https://d.radikal.ru/d14/1811/c6/ce6409e816a0.png', 'https://a.radikal.ru/a02/1811/c2/95a2b6bcad99.png', 'https://a.radikal.ru/a10/1811/10/d50749ef8f36.jpg', 'https://c.radikal.ru/c22/1811/27/71b6af305a13.jpg', 'https://a.radikal.ru/a03/1811/23/ec5cf6dd8c71.png', 'https://c.radikal.ru/c12/1811/06/9ec0ba55f013.png', 'https://a.radikal.ru/a39/1811/fc/94c328021940.jpg', 'https://a.radikal.ru/a01/1811/38/ad3e8add5225.png', 'https://b.radikal.ru/b27/1811/7a/0959769ba6a2.jpg', 'https://b.radikal.ru/b43/1811/b0/89879ae6f498.png', 'https://b.radikal.ru/b05/1811/99/b6a839ee2f73.jpg', 'https://c.radikal.ru/c12/1811/ba/0a831c723c5e.jpg', 'https://c.radikal.ru/c01/1811/80/6d21f71fcccd.png', 'https://b.radikal.ru/b22/1811/b6/ae4494f1b874.jpg', 'https://a.radikal.ru/a01/1811/7c/f3a185d72d30.jpg', 'https://c.radikal.ru/c17/1811/6c/0c3666ad722a.jpg', 'https://a.radikal.ru/a14/1811/15/e0b2bb602f62.jpg', 'https://d.radikal.ru/d12/1811/41/4ff2e931a819.jpg', 'https://c.radikal.ru/c28/1811/3b/fb63f1035ac5.jpg', 'https://d.radikal.ru/d15/1811/73/00fb2d39e237.jpg', 'https://b.radikal.ru/b12/1811/ac/2fd6e3c69266.jpg', 'https://d.radikal.ru/d01/1811/0a/13b696cd5695.png', 'https://c.radikal.ru/c23/1811/33/dd21576bfcc8.jpg', 'https://a.radikal.ru/a05/1811/9e/e226f3a2a868.jpg', 'https://c.radikal.ru/c36/1811/d1/2b4d12bb07e6.jpg', 'https://d.radikal.ru/d24/1811/2d/506512f4be8e.jpg', 'https://b.radikal.ru/b18/1811/72/d175a8015cd6.png', 'https://d.radikal.ru/d16/1811/be/758c3e49206b.jpg', 'https://c.radikal.ru/c13/1811/79/4dfaada37a1a.jpg', 'https://a.radikal.ru/a10/1811/8b/ec2e89f79190.jpg', 'https://c.radikal.ru/c42/1811/64/d7be09df5462.jpg', 'https://a.radikal.ru/a36/1811/37/54c96ff8fb8c.png', 'https://c.radikal.ru/c12/1811/a4/cd0a953392fc.png', 'https://b.radikal.ru/b13/1811/82/69eb86d60516.jpg', 'https://b.radikal.ru/b07/1811/7a/e0c6010a5e48.png', 'https://a.radikal.ru/a14/1811/d0/a7b6d14c4690.jpg', 'https://c.radikal.ru/c07/1811/59/02bc993169c6.jpg', 'https://a.radikal.ru/a11/1811/1b/cb91f8bcf28a.png', 'https://b.radikal.ru/b00/1811/21/a91eb15731c2.png', 'https://d.radikal.ru/d31/1811/35/7a9a5580e559.jpg', 'https://c.radikal.ru/c00/1811/0a/97106ac7e8b8.jpg', 'https://c.radikal.ru/c06/1811/d9/12415bb8261f.jpg', 'https://d.radikal.ru/d13/1811/2c/f97b97a74b0e.png', 'https://d.radikal.ru/d35/1811/88/21d53a3b33fb.jpg', 'https://b.radikal.ru/b07/1811/50/b463db15f2c3.jpg', 'https://a.radikal.ru/a40/1811/11/b48defad5778.png', 'https://d.radikal.ru/d28/1811/00/c15a9a4c27af.jpg', 'https://a.radikal.ru/a00/1811/7b/c7ffbd85e376.jpg', 'https://c.radikal.ru/c22/1811/91/15a8098a14fc.jpg', 'https://c.radikal.ru/c10/1811/1c/ee4516bb6b83.jpg', 'https://b.radikal.ru/b32/1811/12/4549d8513ed0.jpg', 'https://c.radikal.ru/c14/1811/e5/afc528abab86.jpg', 'https://d.radikal.ru/d27/1811/95/a042a6c891b6.jpg', 'https://d.radikal.ru/d33/1811/0b/a37a532f322d.jpg', 'https://b.radikal.ru/b15/1811/2b/beff06a644bc.jpg', 'https://a.radikal.ru/a18/1811/83/81ee1e057d23.jpg', 'https://c.radikal.ru/c00/1811/8a/d89903408e76.jpg', 'https://a.radikal.ru/a22/1811/a1/28d5439d1eae.jpg', 'https://c.radikal.ru/c10/1811/01/6ffe89c41952.png', 'https://d.radikal.ru/d17/1811/d1/b1e3a7001442.jpg', 'https://a.radikal.ru/a42/1811/ec/2f59558f7581.jpg', 'https://c.radikal.ru/c40/1811/93/b2d490eb20d9.jpg', 'https://a.radikal.ru/a08/1811/df/d35c0b3ff7d6.jpg', 'https://a.radikal.ru/a40/1811/45/379d292a5686.png', 'https://b.radikal.ru/b19/1811/25/4d031564d3ba.jpg', 'https://a.radikal.ru/a16/1811/5d/498cbe772159.jpg', 'https://a.radikal.ru/a23/1811/70/ab198164fb92.jpg', 'https://a.radikal.ru/a04/1811/d0/151c5bf6bb8e.jpg', 'https://b.radikal.ru/b04/1811/49/cb961b42c3a2.png', 'https://c.radikal.ru/c11/1811/6d/0748ded8a7c8.jpg', 'https://a.radikal.ru/a08/1811/7f/5d2673aed796.jpg', 'https://b.radikal.ru/b05/1811/6f/8822faccaefc.jpg', 'https://a.radikal.ru/a37/1811/d0/86bc7f114264.jpg', 'https://c.radikal.ru/c00/1811/b7/e35826dd41ab.png', 'https://b.radikal.ru/b41/1811/b5/6333d654cb83.jpg', 'https://c.radikal.ru/c36/1811/ff/db53ddede9f5.png', 'https://b.radikal.ru/b24/1811/74/ee58a167016d.jpg', 'https://c.radikal.ru/c32/1811/d3/9eefd898c07e.jpg', 'https://c.radikal.ru/c26/1811/6c/18daec6d237a.jpg', 'https://b.radikal.ru/b10/1811/d5/39bda4e5f984.jpg', 'https://a.radikal.ru/a12/1811/38/76690e67ee89.jpg', 'https://b.radikal.ru/b19/1811/ff/ce067dd43d70.png', 'https://a.radikal.ru/a22/1811/11/750182d5d243.jpg', 'https://c.radikal.ru/c30/1811/83/1339d5644a93.jpg', 'https://b.radikal.ru/b20/1811/a6/5071620fa98c.png', 'https://c.radikal.ru/c25/1811/22/5d81d743461a.png', 'https://c.radikal.ru/c37/1811/a5/190bb1826d84.jpg', 'https://b.radikal.ru/b06/1811/3c/8b927790db62.jpg', 'https://c.radikal.ru/c08/1811/68/aa2a8d49b776.png', 'https://c.radikal.ru/c30/1811/08/a75fbf50e47b.png', 'https://d.radikal.ru/d41/1811/f0/314d35d48556.png', 'https://d.radikal.ru/d22/1811/89/e573e70bc769.png', 'https://d.radikal.ru/d05/1811/89/9df5b4b89b56.png', 'https://c.radikal.ru/c30/1811/91/8879a8d18507.png', 'https://c.radikal.ru/c08/1811/3e/c0840faf11be.png', 'https://d.radikal.ru/d01/1811/e4/8903d4edcbe9.png', 'https://b.radikal.ru/b26/1811/f5/9d135ee010b0.png', 'https://c.radikal.ru/c31/1811/52/87315640792d.png', 'https://a.radikal.ru/a30/1811/a8/11e5e1e43b3a.jpg', 'https://a.radikal.ru/a27/1811/93/dd9f8a558499.png', 'https://b.radikal.ru/b30/1811/d1/d4ef243c9e95.jpg', 'https://c.radikal.ru/c17/1811/c3/d25f391223ac.png', 'https://d.radikal.ru/d26/1811/4b/cd5d286c1763.jpg', 'https://b.radikal.ru/b39/1811/51/5020bc846d2c.jpg', 'https://d.radikal.ru/d32/1811/eb/bb31c4423e9c.jpg', 'https://a.radikal.ru/a09/1811/34/6c21a93976ff.png', 'https://c.radikal.ru/c12/1811/f9/873df19d0dc8.jpg', 'https://d.radikal.ru/d43/1811/5b/4ac3bdc43b84.jpg', 'https://b.radikal.ru/b27/1811/9b/cc2070b385c8.jpg', 'https://d.radikal.ru/d21/1811/a6/64e668137f16.jpg', 'https://b.radikal.ru/b39/1811/8c/d5e9c8f9b625.jpg', 'https://a.radikal.ru/a07/1811/69/d7206893ddab.jpg', 'https://a.radikal.ru/a20/1811/f2/88364319878a.jpg', 'https://a.radikal.ru/a22/1811/74/b0da62388ec9.jpg', 'https://b.radikal.ru/b31/1811/df/886e8daf0992.jpg', 'https://d.radikal.ru/d43/1811/cc/5f46d0ee52fc.jpg', 'https://b.radikal.ru/b03/1811/03/dd310acac32c.jpg', 'https://b.radikal.ru/b05/1811/70/97339e575739.jpg', 'https://b.radikal.ru/b43/1811/03/2278bfb580dc.jpg', 'https://b.radikal.ru/b26/1811/96/a818488b6adb.jpg', 'https://c.radikal.ru/c23/1811/23/91c7830fea1a.jpg', 'https://a.radikal.ru/a25/1811/81/727f13361125.png', 'https://a.radikal.ru/a31/1811/ff/377fc0f39f0d.png', 'https://c.radikal.ru/c25/1811/1e/91e71c07ce57.jpg', 'https://b.radikal.ru/b05/1811/eb/a76c844d596b.png', 'https://c.radikal.ru/c33/1811/af/10d192323ff3.jpg', 'https://c.radikal.ru/c01/1811/77/190e34a85655.jpg', 'https://b.radikal.ru/b13/1811/34/b060d3086c82.jpg', 'https://a.radikal.ru/a16/1811/85/ec80401b6978.png', 'https://a.radikal.ru/a02/1811/30/5ca1a56a8e24.png', 'https://a.radikal.ru/a27/1811/02/d95e64039709.png', 'https://d.radikal.ru/d20/1811/2f/47a103e02e56.jpg', 'https://c.radikal.ru/c36/1811/e0/37c26aeb0167.jpg', 'https://d.radikal.ru/d29/1811/70/ad5a7f3bfb4f.jpg', 'https://c.radikal.ru/c22/1811/a3/f6ac14a28a05.png', 'https://a.radikal.ru/a00/1811/16/f93e276331b7.jpg', 'https://c.radikal.ru/c18/1811/c0/a04ce2837d12.jpg', 'https://d.radikal.ru/d21/1811/29/61ab029e80e3.jpg', 'https://a.radikal.ru/a12/1811/93/17b0f8cda140.jpg', 'https://c.radikal.ru/c34/1811/e9/50180747a978.jpg', 'https://c.radikal.ru/c36/1811/fa/95a4a9e7989b.jpg', 'https://d.radikal.ru/d14/1811/ea/e620083c20e5.jpg', 'https://d.radikal.ru/d32/1811/d8/c2e33c0aa208.jpg', 'https://b.radikal.ru/b16/1811/f0/fed106d302ce.jpg', 'https://c.radikal.ru/c28/1811/c5/4b7b15094cfb.jpg', 'https://b.radikal.ru/b09/1811/48/a0e38f821fd1.png', 'https://b.radikal.ru/b03/1811/9b/56f59b536280.jpg', 'https://b.radikal.ru/b20/1811/f3/77df594e2f2e.jpg', 'https://d.radikal.ru/d23/1811/17/843737c645bd.jpg', 'https://c.radikal.ru/c13/1811/60/96f336b800ac.png', 'https://d.radikal.ru/d41/1811/03/c8c8f3e1a384.jpg', 'https://b.radikal.ru/b03/1811/50/e8f2e7da207f.png', 'https://d.radikal.ru/d34/1811/70/015ca5b0e976.jpg', 'https://a.radikal.ru/a36/1811/47/8609106a4008.png', 'https://c.radikal.ru/c26/1811/78/ec76a2b2871d.png', 'https://c.radikal.ru/c20/1811/61/e94833840af6.jpg', 'https://c.radikal.ru/c23/1811/f1/0e9bb9bfff72.jpg', 'https://a.radikal.ru/a00/1811/9f/27f8e392c38c.png', 'https://b.radikal.ru/b12/1811/05/df6736c758bc.png', 'https://c.radikal.ru/c26/1811/7b/0b7e02e40624.png', 'https://c.radikal.ru/c38/1811/a9/37224c3f72ea.jpg', 'https://d.radikal.ru/d22/1811/37/102a36cf4133.jpg', 'https://c.radikal.ru/c06/1811/bf/ee6222d8e401.jpg', 'https://c.radikal.ru/c31/1811/0f/3c216003f510.png', 'https://c.radikal.ru/c11/1811/df/97a67797f491.png', 'https://a.radikal.ru/a32/1811/46/e26939c2f5da.png', 'https://d.radikal.ru/d11/1811/eb/38d6e19afe51.png', 'https://b.radikal.ru/b23/1811/6a/605323bc8915.jpg', 'https://b.radikal.ru/b07/1811/cc/874d9b070e43.jpg', 'https://c.radikal.ru/c19/1811/eb/18f3ee7dc978.jpg', 'https://a.radikal.ru/a13/1811/e4/2c3d7687e65b.jpg', 'https://d.radikal.ru/d02/1811/da/06c0300782d9.png', 'https://c.radikal.ru/c39/1811/d8/26bc6cc03ee9.jpg', 'https://b.radikal.ru/b17/1811/ee/15b7bbe3db8d.jpg', 'https://a.radikal.ru/a22/1811/de/32d931a4cd9e.png', 'https://d.radikal.ru/d35/1811/eb/68a83d0098d3.jpg', 'https://d.radikal.ru/d09/1811/cd/e92ef76db8ba.jpg', 'https://b.radikal.ru/b43/1811/a1/614de9a0ad0a.png', 'https://a.radikal.ru/a17/1811/c4/bee5d8a7e8a4.png', 'https://b.radikal.ru/b29/1811/2c/7a31efd01bae.jpg', 'https://c.radikal.ru/c23/1811/b8/ffa99cb11ff5.jpg', 'https://c.radikal.ru/c31/1811/63/6d4317fed731.jpg', 'https://a.radikal.ru/a34/1811/a6/9e8dbe1bf4ad.jpg', 'https://c.radikal.ru/c37/1811/38/ff644b81bb96.jpg', 'https://d.radikal.ru/d34/1811/d7/1f941ef5f50b.jpg', 'https://d.radikal.ru/d08/1811/98/60b4a0938866.jpg', 'https://c.radikal.ru/c01/1811/69/c67954d0c1e0.jpg', 'https://c.radikal.ru/c23/1811/66/45ae8b2a0c7a.jpg', 'https://c.radikal.ru/c04/1811/19/0baa5bce5a91.png', 'https://a.radikal.ru/a43/1811/82/e31ef9ace9b6.png', 'https://d.radikal.ru/d24/1811/91/6578c05578ce.jpg', 'https://d.radikal.ru/d02/1811/80/f296f9f77159.jpg', 'https://c.radikal.ru/c15/1811/f9/74b1daf650bc.jpg', 'https://c.radikal.ru/c13/1811/0a/88aec5e70300.jpg', 'https://d.radikal.ru/d23/1811/34/e88308fa3596.png', 'https://b.radikal.ru/b39/1811/82/8db81a03156d.jpg', 'https://d.radikal.ru/d08/1811/bf/85d0a3e9dc0b.jpg', 'https://b.radikal.ru/b14/1811/7c/e573087e4051.jpg', 'https://c.radikal.ru/c30/1811/bc/ee62c7e7cb4b.jpg', 'https://a.radikal.ru/a37/1811/7b/c3d87947b318.jpg', 'https://d.radikal.ru/d15/1811/fb/4b0351fd48c2.jpg', 'https://d.radikal.ru/d04/1811/f6/2969390e1c92.png', 'https://a.radikal.ru/a26/1811/f7/8b40f00bff58.jpg', 'https://a.radikal.ru/a24/1811/0f/5bcd325258f1.png', 'https://d.radikal.ru/d30/1811/2f/fa4d0ae37eb2.jpg', 'https://b.radikal.ru/b37/1811/4e/6c699a20c9ab.jpg', 'https://b.radikal.ru/b15/1811/10/a74d750c8f40.jpg', 'https://b.radikal.ru/b21/1811/5c/5a616ca84ca5.jpg', 'https://d.radikal.ru/d38/1811/87/beaa5c9eeff8.jpg', 'https://b.radikal.ru/b06/1811/9f/145e671ff00f.jpg', 'https://d.radikal.ru/d13/1811/04/001c4a6702e3.jpg', 'https://b.radikal.ru/b00/1811/bb/1a4806039daf.jpg', 'https://d.radikal.ru/d07/1811/ee/0ea0da4b3700.jpg', 'https://a.radikal.ru/a33/1811/42/6c3f349261c0.jpg', 'https://c.radikal.ru/c21/1811/1a/44a4f7f36590.jpg', 'https://d.radikal.ru/d24/1811/a9/6041b660a69b.jpg', 'https://b.radikal.ru/b40/1811/4e/41c718dade71.jpg', 'https://c.radikal.ru/c03/1811/18/d3d7c4fb6d42.jpg', 'https://a.radikal.ru/a19/1811/0e/f8d1f03f518a.jpg', 'https://b.radikal.ru/b31/1811/4e/eb40e23bb3a3.jpg', 'https://b.radikal.ru/b23/1811/0d/51b8212ad106.jpg', 'https://c.radikal.ru/c39/1811/c0/815c47180655.jpg', 'https://b.radikal.ru/b17/1811/b6/6fcb91e6643f.jpg', 'https://a.radikal.ru/a33/1811/14/80b7e418402a.jpg', 'https://a.radikal.ru/a30/1811/51/c479c3255b69.jpg', 'https://c.radikal.ru/c12/1811/09/28496e1ec873.jpg', 'https://c.radikal.ru/c24/1811/ef/414e157afe1b.jpg', 'https://b.radikal.ru/b40/1811/19/f96eabaacf3f.jpg', 'https://b.radikal.ru/b03/1811/c8/9505d38a9c9b.jpg', 'https://b.radikal.ru/b10/1811/b8/8d2546d6fdff.jpg', 'https://a.radikal.ru/a13/1811/24/a000736e6131.jpg', 'https://a.radikal.ru/a39/1811/0e/fa6eb342d212.jpg', 'https://b.radikal.ru/b02/1811/46/25c90275c8b1.jpg', 'https://d.radikal.ru/d39/1811/19/d78128557ad4.jpg', 'https://c.radikal.ru/c02/1811/5f/e0a1d3fb0d2a.jpg', 'https://b.radikal.ru/b22/1811/dd/792b83b2fb01.jpg', 'https://d.radikal.ru/d07/1811/5e/c77986825733.jpg', 'https://d.radikal.ru/d42/1811/91/9152de853bc6.jpg', 'https://a.radikal.ru/a30/1811/f7/a19d719c2620.jpg', 'https://a.radikal.ru/a36/1811/a9/9df704341087.jpg', 'https://b.radikal.ru/b43/1811/21/dadcafa9c4cf.jpg', 'https://c.radikal.ru/c40/1811/f6/984c2fcc1021.jpg', 'https://c.radikal.ru/c43/1811/32/66e7ac404b2b.jpg', 'https://b.radikal.ru/b41/1811/1b/4cfd40acacf4.jpg', 'https://b.radikal.ru/b32/1811/4e/dc9e52214342.jpg', 'https://d.radikal.ru/d00/1811/2d/22d3814ae4ac.jpg', 'https://b.radikal.ru/b14/1811/b2/228fe889f14e.jpg', 'https://c.radikal.ru/c39/1811/5f/d07f9fccbbc7.jpg', 'https://a.radikal.ru/a27/1811/ac/b6b83f4e00f8.jpg', 'https://a.radikal.ru/a15/1811/7c/a0d6680359aa.jpg', 'https://d.radikal.ru/d41/1811/83/bae6481cd559.jpg', 'https://d.radikal.ru/d00/1811/ae/741db71a2336.jpg', 'https://a.radikal.ru/a22/1811/fb/5db86bc0fb58.jpg', 'https://d.radikal.ru/d26/1811/59/2d637a14558b.jpg', 'https://c.radikal.ru/c20/1811/39/b1e4cd69e27a.jpg', 'https://d.radikal.ru/d12/1811/54/9b30c50b5e5e.jpg', 'https://d.radikal.ru/d15/1811/b1/fa7712f88693.jpg', 'https://d.radikal.ru/d22/1811/32/38d10f5bd4ea.jpg', 'https://d.radikal.ru/d09/1811/b3/6afdc3c9e810.jpg', 'https://c.radikal.ru/c41/1811/76/055d055b637f.jpg', 'https://a.radikal.ru/a23/1811/c0/ecb60df8a529.jpg', 'https://a.radikal.ru/a11/1811/64/21caff9a4401.jpg', 'https://a.radikal.ru/a42/1811/33/0bdde63101f7.jpg', 'https://c.radikal.ru/c24/1811/be/0a0b9d44af16.jpg', 'https://c.radikal.ru/c02/1811/41/0ef6ad0ae16b.jpg', 'https://c.radikal.ru/c06/1811/f7/a10ec777019e.png', 'https://b.radikal.ru/b38/1811/e9/4d7c88784fb1.jpg', 'https://d.radikal.ru/d19/1811/ef/584e828c914c.jpg', 'https://b.radikal.ru/b42/1811/87/320b14edd951.jpg', 'https://c.radikal.ru/c23/1811/44/d02949ee17f3.jpg', 'https://c.radikal.ru/c14/1811/b1/070908af231e.png', 'https://c.radikal.ru/c02/1811/41/d9752267cce8.jpg', 'https://a.radikal.ru/a18/1811/06/164ef6e3353e.jpg', 'https://b.radikal.ru/b35/1811/d9/7beed618feed.png', 'https://a.radikal.ru/a41/1811/a4/70bfd03b5c86.jpg', 'https://d.radikal.ru/d00/1811/02/626401207819.jpg', 'https://a.radikal.ru/a08/1811/9b/626eebedfa67.jpg', 'https://d.radikal.ru/d30/1811/b3/8f6d62b04b64.jpg', 'https://b.radikal.ru/b11/1811/91/470997317f1e.jpg', 'https://d.radikal.ru/d18/1811/11/ae805ee46368.jpg', 'https://c.radikal.ru/c31/1811/e0/94f23e76261b.jpg', 'https://c.radikal.ru/c22/1811/be/6bd382187c34.jpg', 'https://d.radikal.ru/d10/1811/6b/a14c1b61e432.jpg', 'https://c.radikal.ru/c29/1811/8a/a22692c6caba.jpg', 'https://d.radikal.ru/d42/1811/ed/0f0b90c8ce6d.jpg', 'https://a.radikal.ru/a33/1811/b3/4374a294efd3.jpg', 'https://a.radikal.ru/a12/1811/6f/a045de15da1c.jpg', 'https://c.radikal.ru/c24/1811/f5/2eb1289f8599.jpg', 'https://c.radikal.ru/c31/1811/6d/04591c785607.jpg', 'https://a.radikal.ru/a25/1811/c5/44647a582df8.jpg', 'https://b.radikal.ru/b39/1811/fe/1eb92dfc00d1.png', 'https://a.radikal.ru/a30/1811/5d/e3e6267da44b.png', 'https://c.radikal.ru/c41/1811/50/8d469fbbbc09.jpg', 'https://a.radikal.ru/a25/1811/45/55cc8e5567d9.jpg', 'https://a.radikal.ru/a01/1811/65/8f001fe486e8.jpg', 'https://b.radikal.ru/b24/1811/ee/91c753c220e2.jpg', 'https://c.radikal.ru/c30/1811/e3/817d3293013d.jpg']

                image_url = random.choice(neko)
                image = session.get(image_url, stream=True)
                photo = upload.photo_messages(photos=image.raw)[0]
                attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))

                if event.from_user:
                    vk.messages.send(user_id=event.user_id, attachment=','.join(attachments), message='Муррр&#128571;&#128008;&#128062;')
                if event.from_chat:
                    vk.messages.send(chat_id=event.chat_id, attachment=','.join(attachments), message='Муррр&#128571;&#128008;&#128062;')
                del attachments [:]

 

            if event.from_me:
                print('От меня для: ', end='')
            elif event.to_me:
                print('Для меня от: ', end='')

            if event.from_user:
                print(event.user_id)

            print('Текст: ', event.text)
            print()

        elif event.type == VkEventType.USER_TYPING:
            print('Печатает ', end='')

            if event.from_user:
                print(event.user_id)

        elif event.type == VkEventType.USER_ONLINE:
            print('Пользователь', event.user_id, 'онлайн', event.platform)

        elif event.type == VkEventType.USER_OFFLINE:
            print('Пользователь', event.user_id, 'оффлайн', event.offline_type)

        else:
            print(event.type, event.raw[1:])


if __name__ == '__main__':
    main()
