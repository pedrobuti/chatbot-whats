# Chatbot python

from twilio.rest import Client

# Autenticação do twilio
account_sid = "ACccc647a594091aafc40d71bf026728f8"
auth_token = "d4f328f962fa4860fed3181f65d745a9"
client = Client(account_sid, auth_token)

# Envio de mensagem
message = client.messages.create(
    body = "Mensagem automática teste", # mensagem a ser enviada
    from_= "whatsapp:+14155238886", # Número do Twilio
    to = "whatsapp:+554498503107" # Número do destinatário
)
