from fastapi import FastAPI, Request
import requests

app = FastAPI()


@app.post("/proxy-post")
async def proxy_post(req: Request):
    try:
        body = await req.json()
        target_url = body["url"]
        wp_user = body["user"]
        wp_pass = body["password"]
        payload = body["data"]

        headers = {"Content-Type": "application/json"}
        response = requests.post(
            target_url, auth=(wp_user, wp_pass), json=payload, headers=headers
        )
        return {"status": response.status_code, "response": response.text}

    except Exception as e:
        return {"error": "Problem processing request", "detail": str(e)}
