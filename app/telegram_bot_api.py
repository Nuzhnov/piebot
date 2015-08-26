import requests
BOT_TOKEN = "102692493:AAER0KPlCo8pNzy6p9y1xmG47oxUrLOu4z4"
URL = "https://api.telegram.org/bot%s/" % BOT_TOKEN

class TelegramBotException(Exception):
	"""Special exception type for telegram bot api"""
	pass


def getVerifyBot():
	r = requests.get(URL + "getMe")
	if r.status_code == 200:
		data = r.json()["result"]
		return data["first_name"]
	else:
		raise TelegramBotException("Failed to verify bot, got %s error" % (r.status_code))

def getMessages(offset=0, limit=100, timeout=0):
	r = requests.get(URL + "getUpdates", data={'offset': offset, 'limit': limit, 'timeout': timeout})
	if r.status_code == 200:
		data = r.json()["result"]
		return data
	else:
		raise TelegramBotException("Failed to check updates, got %s error" % (r.status_code))

def sendMessage(chat_id, text):
	r = requests.post(URL + "sendMessage", data={"chat_id": chat_id, "text": text})
	if r.status_code == 200:
		data = r.json()["result"]
		return data
	else:
		raise TelegramBotException("Failed to send message to chat %s, got %s error" & (chat_id, r.status_code))
		
