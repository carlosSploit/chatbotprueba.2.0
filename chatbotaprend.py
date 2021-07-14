# librerias usadas ------------
# pip install chatterbot
# pip install chatterbot_corpus
# pip install git+git://github.com/huggingface/transformers@59b5953d89544a66d73

# api de chatbot
from chatterbot.chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import yaml


class chatbotApren:

    def __init__(self):
        self.chat = None
        self.trainer = None

    def checkFileExistance(self, filePath):
        try:
            with open(filePath, 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False

    def init(self):
        self.chat = ChatBot(
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
        self.trainer = ListTrainer(self.chat)
        if (self.checkFileExistance("./dataset.json")):
            print("Ya no podemos entrenarlo")
        else:
            self.trainer_M()

    def trainer_M(self):
        yaml_file = open("data/dataset.yaml", 'r')
        yaml_content = yaml.load(yaml_file)
        train = []
        for key, value in yaml_content.items():
            if(key == "conversaciones"):
                train = value
        print(train)
        self.trainer.train(train)
        self.trainer.export_for_training("./dataset.json")

    def converc(self, peticion):
        repuestas = self.chat.get_response(peticion)
        return repuestas
