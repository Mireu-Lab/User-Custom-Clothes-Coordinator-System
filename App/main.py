from fastapi import FastAPI
import uvicorn

from fastapi.responses import RedirectResponse

app=FastAPI()

@app.get("/", tags=["Docs"])
async def docs():
    return RedirectResponse("http://www.mireu.xyz/")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)