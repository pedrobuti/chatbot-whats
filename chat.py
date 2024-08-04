# Chatbot python

from twilio.rest import Client

# Autenticação do twilio
# sid da conta
# auth_token da conta
client = Client(sid_conta, auth_token_conta)

# Envio de mensagem
message = client.messages.create(
    body = "Mensagem automática teste", # mensagem a ser enviada
    from_= "whatsapp twilio", # Número do Twilio
    to = "seu whatsapp para teste" # Número do destinatário
)
