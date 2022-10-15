from twilio.rest import Client

account_sid = "AC1c6a2e7e8a90209ac3e14e4c5ff29bf8"
auth_token = "9d14b743b7fdbbe8ff4e15e1610dcc01"
client = Client(account_sid, auth_token)
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
arr = ['+919373951257',  '+917588531912', '+918696025851']
# '+918696025851',
for num in arr:
    call = client.api.account.calls.create(
        to=num,
        from_='+18336857171',
        url='http://demo.twilio.com/docs/classic.mp3')

    print(call.sid)
