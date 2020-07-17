from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            from chatterbot.trainers import ChatterBotCorpusTrainer
            from chatterbot import ChatBot


            chatbot = ChatBot('Abdulkayyum')

            # Create a new trainer for the chatbot
            trainer = ChatterBotCorpusTrainer(chatbot)

            # Train based on the english corpus
            trainer.train("chatterbot.corpus.turkish")
            trainer.train("chatterbot.corpus.turkish.ai")
            trainer.train("chatterbot.corpus.turkish.botprofile")
            trainer.train("chatterbot.corpus.turkish.emotion")
            trainer.train("chatterbot.corpus.turkish.food")
            trainer.train("chatterbot.corpus.turkish.greetings")
        except:
            raise CommandError('Shits happen')
