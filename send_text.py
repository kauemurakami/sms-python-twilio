from twilio.rest import Client
#em twilio exite uma pasta cahamada rest que possui uma classe Client


#caso não fizessemos a importação dessa maneira, poderiamos fazer
# from twilio import rest 
# client = res.Client(account_sid, auth_token) #construindo objeto cliente
 

# Your Account SID from twilio.com/console
account_sid = "xxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "xxxxxxxxxxxx"
client = Client(account_sid, auth_token) #construindo objeto cliente

message = client.messages.create(
    to="+5511941595034", #destinatario 
    from_="+15017250604", #meu
    body="Hello from Python!")

print(message.sid)