from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from . import handlers


def main(token):
    # updater
    updater = Updater(token)

    # dispatcher
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(CommandHandler('start', handlers.start))

    # message handlers
    dispatcher.add_handler(MessageHandler(Filters.text('🛍 Shop'), handlers.shop))
    dispatcher.add_handler(MessageHandler(Filters.text('🛒 Cart'), handlers.cart))
    dispatcher.add_handler(MessageHandler(Filters.text('📞 Contact'), handlers.contact))
    dispatcher.add_handler(MessageHandler(Filters.text('📝 About'), handlers.about))

    # callback query handlers
    dispatcher.add_handler(CallbackQueryHandler(pattern='contact:number', callback=handlers.phone_number))
    dispatcher.add_handler(CallbackQueryHandler(pattern='contact:email', callback=handlers.email))

    # brend callback query handlers
    dispatcher.add_handler(CallbackQueryHandler(pattern='brend:', callback=handlers.brend))
    dispatcher.add_handler(CallbackQueryHandler(pattern='phone:', callback=handlers.phone))
    dispatcher.add_handler(CallbackQueryHandler(pattern='cart:', callback=handlers.add_cart))

    # close
    dispatcher.add_handler(CallbackQueryHandler(pattern='close', callback=handlers.close))

    # clear cart
    dispatcher.add_handler(CallbackQueryHandler(pattern='clear', callback=handlers.clear))

    # start polling
    updater.start_polling()
    updater.idle()

