import app.telegram_bot_api as tele
import config_test
import unittest

class ApiTest(unittest.TestCase):

	def setUp(self):
		self.url = config_test.URL
		self.bot_name = config_test.BOT_NAME
		self.chat_id = config_test.CHAT_ID

	def test_connection(self):
		self.assertEqual(tele.getVerifyBot(self.url), self.bot_name)

	def test_get_updates(self):
		data = tele.getMessages(self.url)
		self.assertTrue(data)

	def test_send_message(self):
		text_string = "this is the test text"
		data = tele.sendMessage(self.url, self.chat_id, text_string)
		self.assertEquals(text_string, data["text"])


if __name__ == '__main__':
	unittest.main()