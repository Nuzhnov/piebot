import piebot.app.telegram_bot_api
import unittest

class BaseTest(unittest.TestCase):

	def test_add(self):
		self.assertEqual(100, 100 + 20)

if __name__ == '__main__':
	unittest.main()