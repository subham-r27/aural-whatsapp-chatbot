from fastapi import FastAPI, Request

from responses import *
from sheets import store_lead
from whatsapp import send_whatsapp_message
from config import VERIFY_TOKEN

app = FastAPI()


def get_response(msg):

    msg = msg.lower()

    if "hi" in msg or "hello" in msg:
        return GREETING
    elif "product" in msg:
        return PRODUCTS
    elif "sample" in msg:
        return SAMPLES
    elif "price" in msg:
        return PRICING
    elif "company" in msg:
        return COMPANY
    elif "contact" in msg:
        return CONTACT
    else:
        return DEFAULT


@app.get("/webhook")
def verify_webhook(hub_mode: str = None,
                   hub_verify_token: str = None,
                   hub_challenge: str = None):

    if hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)

    return "Verification failed"


@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    try:

        message = data["entry"][0]["changes"][0]["value"]["messages"][0]

        phone = message["from"]
        text = message["text"]["body"]

        store_lead(phone, text)

        reply = get_response(text)

        send_whatsapp_message(phone, reply)

    except:
        pass

    return {"status": "ok"}