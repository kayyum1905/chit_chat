import json

from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.ext.django_chatterbot import settings


class ChatPageView(TemplateView):
    template_name = 'chat_app/chat_page.html'


def chat_json(request):
    if request.is_ajax():
        data = {'msg_': request.POST.get('msg_')}
        msg_ = data['msg_']
        print('msg_: ', msg_)
        chatbot = ChatBot('Abdulkayyum')

        trainer = ChatterBotCorpusTrainer(chatbot)

        # trainer.train("chatterbot.corpus.turkish")
        trainer.train("chatterbot.corpus.turkish.ai")
        trainer.train("chatterbot.corpus.turkish.botprofile")
        trainer.train("chatterbot.corpus.turkish.emotion")
        trainer.train("chatterbot.corpus.turkish.food")
        trainer.train("chatterbot.corpus.turkish.greetings")

        bot_response = chatbot.get_response(str(msg_))
        print('bot_response: ', bot_response)

    return JsonResponse(bot_response)

class ChatPageViewApi(View):

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'name': self.chatterbot.name
        })
