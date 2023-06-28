import unittest
from unittest.mock import MagicMock
from bot import Bot


class BotTestCase(unittest.TestCase):
    def setUp(self):
        with open('venv/.telegramToken') as f:
            _token = f.read()
        self.bot = Bot(_token)

    def test_search_handler(self):
        update = MagicMock()
        context = MagicMock()
        self.bot._search_handler(update, context)

        update.message.reply_text.assert_called_with(
            "Please enter the video you want to search for:"
        )

    def test_search_video_handler_found(self):
        update = MagicMock()
        context = MagicMock()
        update.message.text = "Video 1"
        self.bot.send_video = MagicMock()
        self.bot._search_video_handler(update, context)

        self.bot.send_video.assert_called_with(update, context)

    def test_fallback_handler(self):
        update = MagicMock()
        context = MagicMock()
        update.message.reply_text = MagicMock()
        self.bot._fallback_handler(update, context)

        update.message.reply_text.assert_called_with(
            "Sorry, I didn't understand that command."
        )

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
