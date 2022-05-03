from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def index():
    return {'message': "Hello World"}

# Blog code reads from top to bottom
@app.get('/blog/all')
def get_all_blogs():
    return {'message': 'All blogs provided'}

@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message': f'Blog with id {id}'}
