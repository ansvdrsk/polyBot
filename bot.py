import os
import glob
from pytube.extract import playlist_id
from telegram import InputFile, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CallbackContext
from utils import search_download_youtube_video
from loguru import logger


class Bot:
    MENU, SEARCH = range(2)

    def __init__(self, token):
        self.updater = Updater(token, use_context=True)
        self.updater.dispatcher.add_handler(ConversationHandler(
            entry_points=[MessageHandler(Filters.text, self._menu_handler)],
            states={
                self.MENU: [MessageHandler(Filters.regex('^Search$'), self._search_handler)],
                self.SEARCH: [MessageHandler(Filters.text, self._search_video_handler)],
            },
            fallbacks=[MessageHandler(Filters.text, self._fallback_handler)]
        ))

    def start(self):
        self.updater.start_polling()
        logger.info(f'{self.__class__.__name__} is up and listening to new messages....')
        self.updater.idle()

    def _menu_handler(self, update, context):
        menu_options = [['Search']]
        reply_markup = ReplyKeyboardMarkup(menu_options, one_time_keyboard=True)
        update.message.reply_text("Please select an option:", reply_markup=reply_markup)
        return self.MENU

    def _search_handler(self, update, context):
        update.message.reply_text("Please enter the video you want to search for:")
        return self.SEARCH

    def _search_video_handler(self, update, context):
        video_name = update.message.text
        video_path = search_download_youtube_video(video_name)
        video_path = video_path.replace(" ", "")
        if video_path:
            self.send_video(update, context)
        else:
            update.message.reply_text("Sorry, I couldn't find the requested video.")
        return ConversationHandler.END

    def _fallback_handler(self, update, context):
        update.message.reply_text("Sorry, I didn't understand that command.")
        return ConversationHandler.END

    def send_video(self, update, context):
        script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
        video_files = glob.glob(os.path.join(script_directory, '*.mp4'))

        if video_files:
            for file in video_files:
                video = open(file, 'rb')
                video_title = os.path.splitext(os.path.basename(file))[0]  # Extract the video title from the file name

                context.bot.send_video(
                    chat_id=update.effective_chat.id,
                    video=video,
                    caption=video_title
                )

                video.close()
                os.remove(file)
        else:
            update.message.reply_text("Sorry, no video files found.")


if __name__ == '__main__':
    with open('venv/.telegramToken') as f:
        _token = f.read()

    my_bot = Bot(_token)
    my_bot.start()
