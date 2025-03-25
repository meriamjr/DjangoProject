import requests
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from chatbot.models import Conversation

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            # Récupération et décodage du JSON envoyé dans la requête
            data = json.loads(request.body)
            user_message = data.get("message")

            if not user_message:
                return JsonResponse({"error": "No message provided"}, status=400)

            # Structure du message selon le modèle Llama 3
            message_payload = {
                "model": "llama3",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                    {"role": "assistant", "content": ""}
                ]
            }

            # Appel à l'API Ollama
            response = requests.post(
                "http://localhost:11434/api/chat",
                json=message_payload,
                headers={'Content-Type': 'application/json'}
            )

            # Vérification du statut de la réponse
            if response.status_code == 200:
                full_message = ""
                # Lire chaque morceau dans la réponse
                for chunk in response.iter_lines(decode_unicode=True):
                    if chunk: # Ignorer les lignes vides
                        try:
                            # Charger chaque fragment comme JSON
                            chunk_data = json.loads(chunk)
                            if "message" in chunk_data and "content" in chunk_data["message"]:
                                full_message += chunk_data["message"]["content"]
                        except json.JSONDecodeError:
                            print("Erreur de déchiffrement JSON pour le fragment :", chunk)

                # Sauvegarder la conversation dans la base de données
                conversation = Conversation(
                user_message=user_message,
                bot_response=full_message
                )
                conversation.save() # Enregistrer l'objet dans la base de données

                # Retourner le message complet au client
                return JsonResponse({"bot_response": full_message})
            else:
                # Gérer une réponse non réussie
                return JsonResponse(
                    {"error": "Failed to fetch response from API",
                "status_code": response.status_code},
                status=500
                )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        except requests.RequestException as e:
            return JsonResponse({"error": str(e)}, status=500)

    # Retourner une erreur pour les méthodes autres que POST
    return JsonResponse({"error": "Invalid request method"}, status=405) 

def chat_view(request):
    return render(request, "chat-form.html")
