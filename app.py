from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles       # Used for making static resources available to server
from fastapi.templating import Jinja2Templates # Used for templatizied HTML
import uvicorn

# Here, you're creating an instance of FastAPI. 
# This is like starting up your FastAPI toolkit and getting it ready to use. 
# We call this instance app, and it's what you'll use to create different parts of your web application.
app = FastAPI() 

# Specify where the static files are located. This is the name of your folder.
static_files = StaticFiles(directory='public') 
views = Jinja2Templates(directory="public/views")

# Mount the static files directory to /public, this is where your other files will access the sources.
app.mount('/public', static_files, name='public')

# We modulate the different kinds of files so it's easier for us to navigate them
app.mount("/imgs", StaticFiles(directory="public/imgs"), name="imgs")
app.mount("/css", StaticFiles(directory="public/css"), name="css")
app.mount("/js", StaticFiles(directory="public/js"), name="js")


@app.get('/', response_class=HTMLResponse)
def get_home(request: Request) -> HTMLResponse:
    """
    Get the homepage
    :param request: the request object
    :return: the homepage
    """
    return HTMLResponse(content=views.get_template("home.html").render(), status_code=200)


@app.post("/")
def check_email_exists(user: User) -> str:
    return(Auth.verify_availability(user.username, user.email))

@app.put('/website/customer/{img_id}')
def put_user(user:User, user_id: str, request: Request) -> dict:
    session = sessions.get_session(request)
    session['username'] = user.username
    return {'success': Auth.update_user(user_id, user.first_name, user.last_name, user.email, user.username, Security.encrypt(user.password))}

@app.delete('/customer/{img_id}')
def delete_user(user_id:int) -> dict:
    return {'success': Auth.delete_user(user_id)}


if __name__ == "__main__":
    # We can specify what ports to run, and you can change this.
    # You would access this at 127.0.0.`:8007 or localhost:8007

    # reload = True allows us to make changes to our code without constantly rerunning the code.
    uvicorn.run("app:app", host="127.0.0.1", port=8007, reload=True)