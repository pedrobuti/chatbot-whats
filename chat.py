# Chatbot python

from twilio.rest import Client

# Autenticação do twilio
account_sid = "sua conta sid"
auth_token = "seu auth token"
client = Client(account_sid, auth_token)

# Envio de mensagem
message = client.messages.create(
     body = "Mensagem automática teste", # mensagem a ser enviada
     from_= "whatsapp twilio", # Número do Twilio
     to = "seu whatsapp" # Número do destinatário
 )
