import requests


class TelegramBotException(Exception):
	"""Special exception type for telegram bot api"""
	pass


def getVerifyBot(url):
	r = requests.get(url + "getMe")
	if r.status_code == 200:
		data = r.json()["result"]
		return data["first_name"]
	else:
		raise TelegramBotException("Failed to verify bot, got %s error" % (r.status_code))

def getMessages(url, offset=0, limit=100, timeout=0):
	r = requests.get(url + "getUpdates", data={'offset': offset, 'limit': limit, 'timeout': timeout})
	if r.status_code == 200:
		data = r.json()["result"]
		return data
	else:
		raise TelegramBotException("Failed to check updates, got %s error" % (r.status_code))

def sendMessage(url, chat_id, text):
	r = requests.post(url + "sendMessage", data={"chat_id": chat_id, "text": text})
	if r.status_code == 200:
		data = r.json()["result"]
		return data
	else:
		raise TelegramBotException("Failed to send message to chat %s, got %s error" & (chat_id, r.status_code))
		
