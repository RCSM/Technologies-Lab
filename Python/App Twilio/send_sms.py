from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

str = '''
txt msg ::: Hey Hooman! I am a twilio bot, you can trust me ;)
'''

message = client.messages.create(to = my_cell, from_ = my_twilio, body = str)