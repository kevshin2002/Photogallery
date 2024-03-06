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
    # title: str = None
    # description: str = None
    # src: str = None
    title: str 
    description: str 
    src: str 

images = {
    
}  # Stores images as 
             # {
             #   img_id: {"title": "example", "description": "desc", "str": "url"}
             #                                                                               }

@app.get('/', response_class=HTMLResponse)
def get_home(request: Request) -> HTMLResponse:
    """
    Handles the getting of data, you should be passing the data with the main.html.

    """
    return views.TemplateResponse("main.html", {"request": request, "images": images})
    

@app.post("/{img_id}")
def post_image(img_id: int, img_data: Image):
    # add data
    
    post_status = False
    size_before = len(images)
    
    images.update({img_id: img_data})

    # Checks if data size is increased and if src is empty
    if len(images) == (size_before + 1) and len(list(images.get(img_id))[2][1]) != 0:
        post_status = True

    """
    Handles the posting of an image source URL associated with a given image ID.
    :param img_id: The ID of the image to which the source URL is to be associated.
    :param img_data: The image data received in the request body, including the source URL.
    :return: A boolean value indicating success or failure of the operation.
    """
    return post_status

@app.put("/{img_id}")
def modify_image(img_id: int, img_data: Image):
    #modify data
    
    images.update({img_id: img_data})


    pass

@app.delete('/image/{img_id}')
def delete_img(img_id: int):
    images.pop(img_id)

    pass





fake_image1 = Image(title="title1",description="desc 2", src="url1")
fake_image_1_updated = Image(title="title1 updated",description="desc2 updated", src="url1 updated")

fake_image2 = Image(title="title2",description="desc2", src="url2")
print(post_image(1, fake_image1))

# modify_image(1, fake_image_1_updated)
# post_image(2, fake_image2)
# delete_img(1)
print(images)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8007, reload=True)
