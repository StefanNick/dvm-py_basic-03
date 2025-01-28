import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)

login = os.getenv('login')
password = os.getenv('password')


text_mail = 'Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!\n\
\n\
%website% — это новая версия онлайн-курса по программированию.\n\
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.\n\
\n\
Как будет проходить ваше обучение на %website%?\n\
\n\
→ Попрактикуешься на реальных кейсах.\n\
Задачи от тимлидов со стажем от 10 лет в программировании.\n\
→ Будешь учиться без стресса и бессонных ночей.\n\
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.\n\
→ Подготовишь крепкое резюме.\n\
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.\n\
\n\
Регистрируйся → %website%\n\
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'

site_url = 'https://dvmn.org/profession-ref-program/stefanidi.n/zQK2Q/'
friend_name = 'Pete'
my_name = 'Nickolay'

text_mail = text_mail.replace('%website%', site_url)
text_mail = text_mail.replace('%friend_name%', friend_name)
text_mail = text_mail.replace('%my_name%', my_name)

email_to = 'stefan001@yandex.ru'
email_from = 'devmanorg@yandex.ru'


letter ='From: {email_from}\n\
To: {email_to}\n\
Subject: Приглашение!\n\
Content-Type: text/plain; charset="UTF-8";\n\
\n\
'.format(email_from = email_from, email_to = email_to ) + text_mail

letter = letter.encode("UTF-8")

server.login(login, password)

server.sendmail(email_from, email_to, letter)

server.quit()