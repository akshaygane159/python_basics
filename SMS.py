# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 19:37:36 2019

@author: akshay_gane
"""

from twilio.rest import Client

auth_token = "b245d300f93ebb77c1b86c94370fb1f6"
account_sid = "ACa90361f19c2e141f6ee21668bc73b0cb"
client = Client(account_sid, auth_token)

message = client.messages.create(
        to = "+918928296698",
        from_ = "+12055574908",
        body = "Hello there. Its me here! Guess who?"
                                     )

print(message.sid)
#
"""
call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+918928296698',
                        from_='+12055574908'
                    )

print(call.sid)
"""
#