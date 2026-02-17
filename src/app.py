
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# import uvicorn
import asgi
import os

from workers import Response, WorkerEntrypoint
class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return await self.env.ASSETS.fetch(request)


app = FastAPI()

# Mount static files
# app.mount("../dist/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "../dist/static")), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "../dist/templates"))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Serve the portfolio homepage."""
    return templates.TemplateResponse("index.html", {"request": request})

# if __name__ == "__main__":
#     uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)
