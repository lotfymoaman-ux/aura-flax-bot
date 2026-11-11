from fastapi import FastAPI, Request
import httpx

app = FastAPI()

TELEGRAM_BOT_TOKEN = "9179419967:AAGt265hWisGvfD1dM9yVQ1WL1JxBHQL54Q"

@app.get("/")
def home():
    return {"status": "Aura Flax System Online"}

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        if text == "/start":
            reply_text = "أهلاً بك يا مؤمن في غرفة عمليات Aura Flax. السيرفر يعمل بكفاءة!"
        elif text == "/products":
            reply_text = "جاري الاتصال بـ Supabase وجلب المنتجات..."
        else:
            reply_text = f"تم استقبال الأمر: {text}"
            
        async with httpx.AsyncClient() as client:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            await client.post(url, json={"chat_id": chat_id, "text": reply_text})
            
    return {"ok": True}
