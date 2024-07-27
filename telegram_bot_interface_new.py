import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from telegram.ext import ApplicationBuilder, ContextTypes, Application
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow import keras

async def start(update: Update, context: CallbackContext) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Send me a picture!')

async def photo_handler(update: Update, context: CallbackContext) -> None:
    #add disease names in the order you are training them
    disease_names = {'Tinea Ringworm Candidiasis and other Fungal Infections': 0,'Urticaria Hives': 1}
    photo = update.message.photo[-1]
    file_id = photo.file_id
    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive('image.jpg')
    img_path = "image.jpg"
    model = keras.models.load_model("model_test.keras")
    img = image.load_img(img_path, target_size=(300, 300))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 300
    pred = model.predict(img_array)
    result = np.argmax(pred[0])
    print(result)
    print([i for i,j in disease_names.items() if j == result])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str([i for i,j in disease_names.items() if j == result][0]))
    os.remove("image.jpg")

def main():
    application = Application.builder().token('6234021791:AAEECiivMqB2qnAdsCWZCRY0MnpbzPa53Kw').build()
    
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    photo_handle = MessageHandler(filters.PHOTO, photo_handler)
    application.add_handler(photo_handle)
    
    application.run_polling()

if __name__ == '__main__':
    main()
