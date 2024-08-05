from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configurações Botpress
BOTPRESS_API_URL = 'http://localhost:3000/api/v1/bots/botpress_bot/converse/{user_id}/secured'
BOTPRESS_AUTH_TOKEN = 'token autenticação'

# Configurações API
WHATSAPP_API_URL = 'https://graph.facebook.com/v13.0/your_whatsapp_business_number/messages'
WHATSAPP_ACCESS_TOKEN = 'token autenticação'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Extrai informações da mensagem recebida
    user_id = data['contacts'][0]['wa_id']
    incoming_msg = data['messages'][0]['text']['body']

    # Envia mensagem para o Botpress
    response = requests.post(
        BOTPRESS_API_URL.format(user_id=user_id),
        json={'type': 'text', 'text': incoming_msg},
        headers={'Authorization': f'Bearer {BOTPRESS_AUTH_TOKEN}'}
    )

    # Obtem resposta do Botpress
    bot_response = response.json()
    message = bot_response.get('text', 'Desculpe, não entendi sua mensagem.')

    # Envia resposta ao usuário
    send_whatsapp_message(user_id, message)
    return jsonify({'status': 'success'}), 200

def send_whatsapp_message(user_id, message):
    # Envia mensagem do WhatsApp Business
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {WHATSAPP_ACCESS_TOKEN}'
    }
    payload = {
        'messaging_product': 'whatsapp',
        'to': user_id,
        'text': {'body': message}
    }
    response = requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
    return response

if __name__ == '__main__':
    app.run(debug=True)
