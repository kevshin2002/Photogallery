from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

app = FastAPI()

static_files = StaticFiles(directory='public')
views = Jinja2Templates(directory="public/views")

app.mount('/public', static_files, name='public')
app.mount("/imgs", StaticFiles(directory="public/imgs"), name="imgs")
app.mount("/css", StaticFiles(directory="public/css"), name="css")
app.mount("/js", StaticFiles(directory="public/js"), name="js")

class Image(BaseModel):
    title: str = None
    description: str = None
    src: str = None

images = {}  # Stores images as 
             # {
             #   img_id: {"title": "example", "description": "desc", "src": "url"}
             #                                                                               }

@app.get('/', response_class=HTMLResponse)
def get_home(request: Request) -> HTMLResponse:
    """
    Handles the getting of data, you should be passing the data with the main.html.

    """
    pass

@app.post("/{img_id}")
def post_image(img_id: int, img_data: Image):
    """
    Handles the posting of an image source URL associated with a given image ID.
    :param img_id: Position of ID.
    :param img_data: The image data received in the request body, including the source URL.
    :return: A boolean value indicating success or failure of the operation.
    """
    pass

@app.put("/{img_id}")
def modify_image(img_id: int, img_data: Image):
    pass

@app.delete('/image/{img_id}')
def delete_img(img_id: int):
    pass

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8007, reload=True)
