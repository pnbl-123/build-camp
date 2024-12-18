import json
from firebase_functions import https_fn
import getpass
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

@https_fn.on_request()
def langchain(req: https_fn.Request) -> https_fn.Response:
    model = ChatOpenAI(model="gpt-4o-mini")
    messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

    output = model.invoke(messages)
    return https_fn.Response(output.content,mimetype="text/plain")
    
