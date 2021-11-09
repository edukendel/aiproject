from django.http import HttpResponse
from django.shortcuts import render

import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('ChatBot')

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)
 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)

def chat(request):
    return render(request,'index.html')


def get_bot_reply(request) :
    msg=request.GET.get('msg','')
    print("msg",msg)
    reply = chatbot.get_response(msg)
    return HttpResponse(reply)

