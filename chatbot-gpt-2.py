# librerias usadas ------------
# pip install streamlit-nightly==0.69.3.dev20201025 libreria traductora
# pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
# pip install git+git://github.com/huggingface/transformers@59b5953d89544a66d73

# api de chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chat = ChatBot('cctmx')

# print(date.split("\n"))
# train = ["Hola", "Hola", "Qué tal", "Muy buenas, encantado de saludarte", "Hola, muy bien", "Saludos", "Hola", "Hola", "Saludos", "Hola, ¿cómo estás?", "Bien", "Hola, ¿cómo te va?", "Fino filipino", "Genial, muchas gracias", "Muy bien, gracias. ¿Y tú?", "Hola, ¿cómo te va?", "Bien", "Hola, ¿cómo te va?", "Genial", "Hola, ¿cómo te va?", "Normal, pero podría irme mejor.", "Hola, ¿cómo te va?", "No muy bien.", "¿Cómo estás?", "Bien.", "Yo, genial, ¿y tú?", "Muy bien, gracias.", "Deseando hablar un rato.", "Fino filipino, ¿y tú?", "Un placer conocerte.", "Gracias.", "Igualmente,", "¿Cómo estas?", "Supongo que bien.",
#          "¿Cómo estas?", "Supongo que bien. ¿Y tú como estás?", "Hola, encantado de conocerte.", "Gracias. Igualmente.", "Es un placer conocerte.", "Gracias. Igualmente.", "¡Buenos dias!", "Gracias por su amabilidad.", "Buenos dias. Qué tal", "Buenos dias.", "¿Qué pasa?", "No mucho.", "¿Qué pasa?", "No es para tanto.", "¿Qué pasa?", "Nada interesante, ¿y tú que cuentas?", "¿Qué pasa?", "No mucho.", "¿Qué pasa?", "Nada interesante, gracias. ¿Y qué cuentas tú?", "Buenas noches!", "Buenas noches", "Cómo te ha ido? ", "Bien y a ti", "¿Cómo has estado?", "Bien, gracias a Dios", "¿Qué has hecho últimamente?", "Algo de deporte y tú ?"]
trainer = ChatterBotCorpusTrainer(chat)
trainer.train("./dataset.yml")

while True:
    peticion = input('Tu: ')
    repuestas = chat.get_response(peticion)
    print('bot: ', repuestas)
