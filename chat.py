# Chatbot python

from twilio.rest import Client

# Autenticação do twilio
account_sid = "id twilio"
auth_token = "token de autorização"
client = Client(account_sid, auth_token)

# Envio de mensagem
message = client.messages.create(
    body = "Mensagem automática teste", # mensagem a ser enviada
    from_= "whatsapp twilio", # Número do Twilio
    to = "seu whatsapp para teste" # Número do destinatário
)
