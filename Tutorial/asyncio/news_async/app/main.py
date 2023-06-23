from fastapi import FastAPI

import os
import sys
import urllib.request

import json
import asyncio


app = FastAPI()

@app.get("/")
def read_root():
    client_id = ""
    client_secret = ""
    encText = urllib.parse.quote("IT 신기술")
    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        json_objs = json.loads(response_body.decode('utf-8'))

        json_objs = json_objs['items']

        title_list = []

        for obj in json_objs:
            change_obj = obj['title']
            change_obj.replace('&apos;', "")
            title_list.append(change_obj)
            
        return title_list
    else:
        return("Error Code: " + rescode)

