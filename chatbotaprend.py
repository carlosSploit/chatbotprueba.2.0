# librerias usadas ------------
# pip install chatterbot
# pip install chatterbot_corpus
# pip install git+git://github.com/huggingface/transformers@59b5953d89544a66d73
# -*- coding:utf-8 -*-

# api de chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import yaml
#import sys
#import unicodedata

chat = None
trainer = None


def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False


def init():
    global chat
    global trainer
    chat = ChatBot(
        "Elena",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database="botData.sqlite3",
        logic_adapter=[
            {
                'default_response': 'No te endiendoo disculpa, pero que deberia responder,si fueras tu .',
                'maximum_similarity_threshold': 0.90
            }
        ]
    )
    trainer = ListTrainer(chat)
    if (checkFileExistance("./dataset.json")):
        print("Ya no podemos entrenarlo")
    else:
        trainer_M()


def trainer_M():
    global trainer
    yaml_file = open("data/dataset.yaml", 'r')
    yaml_content = yaml.load(yaml_file)
    train = []
    for key, value in yaml_content.items():
        if(key == "conversaciones"):
            auxvalue = []  # cadena de carapteres que ara de auxiliar
            # mantenimiento de caracteres - tildes - Ñ etc
            for val in value:
                try:
                    auxvalue.append(val.upper().encode(
                        "cp1252").decode().title())
                except UnicodeDecodeError:
                    auxvalue.append(val)
            # ----------------------------------------------
            train = auxvalue

    trainer.train(train)
    trainer.export_for_training("./dataset.json")


def converc(peticion):
    global chat
    repuestas = chat.get_response(peticion)
    return repuestas


# init()
#print(converc("porque eres muy guapo"))
