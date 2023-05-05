# insall pyrogram
# install openai
import re
import asyncio
import os
import openai
# from pyrogram import filters, Client
# 


class BravoSis:
    #i'm not going through basics

    def __init__(self):
        self.openai_api_key = "" # edit with your own values
        self.model = "text-davinci-003" # use any of these [text-davinci-002,text-davinci-001]
        self.mxtoken = 1080 #can decrese/increse with reaspect to result previlage


    def ai(self,query):
        openai.api_key = self.openai_api_key
        completion = openai.Completion.create(engine=self.model, prompt=query, max_tokens=self.mxtoken, n=1, stop=None,temperature=0.7)
        result = completion.choices[0].text
        return result


# wow = BravoSis()


# LeosBot = Client(name="XhatGpt",api_id=wow.api_id ,api_hash=wow.api_hash)

# @LeosBot.on_message(filters.text & ~filters.group)
# async def main(bot):
#     dumbchannel = -1001878347911
#     wow = await ai(ques)
#     dumb_test = f"#USER{newbie} #Q| {ques} |   `{wow}`"
#     await bot.send_message(dumbchannel,dumb_test)
#     await asyncio.sleep(1)
