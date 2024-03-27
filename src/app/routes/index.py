import tensorflow_hub as hub
from fastapi import FastAPI
from src.shared.classes.AskBot import AskBot
from src.app.controller.post.ChatBot import ChatBot
from src.app.controller.delete.DeleteBot import DeleteBot
from src.app.controller.get.AllBots import AllBots
from src.app.controller.post.CreateBot import CreateBot
from src.shared.classes.BotModel import BotModel

routes = FastAPI()

def load_model():
    return hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

model = load_model()

@routes.post('/chatbots')
async def create_bots(bot_model: BotModel):
    response = CreateBot.create(bot_model.unique_id, bot_model.actions, bot_model.responses)
    return {'data': response}

@routes.get('/chatbots')
async def get_all_bots():
    response = AllBots.create()
    return {'data': response}

@routes.delete('/chatbots/{id}')
async def delete_bot(id: str):
    response = DeleteBot.create(id)
    return {'data': response}

@routes.post('/chatbots/{id}/ask')
async def ask_bot(id: str, user_message: AskBot):
    response = ChatBot.create(id, user_message.message, model)
    return {'data': response}