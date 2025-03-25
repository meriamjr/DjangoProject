from django.contrib import admin
from chatbot.models import Conversation

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user_message','bot_response' ,'timestamp' )

# Enregistrement du modèle Conversation dans l'admin avec la configuration ConversationAdmin
admin.site.register(Conversation, ConversationAdmin) 
