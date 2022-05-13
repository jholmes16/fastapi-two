from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from exceptions import StoryException
from router import blog_get, blog_post, user, article
from db import models
from db.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message': "Hello World"}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc:StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )

# Testing catching customizing all exceptions
#@app.exception_handler(HTTPException)
#def custom_handler(request: Request, exc: StoryException):
#    return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(engine)