from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

# Blog code reads from top to bottom
#@app.get('/blog/all')
#def get_all_blogs():
#    return {'message': 'All blogs provided'}

@router.get(
    '/all',
    summary = 'Retrieve all blogs',
    description = 'This api call is for fetching all blogs.',
    response_description = 'The list of available blogs.'
    )
def get_all_blogs(page = 1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}

@router.get('/{id}/comments/{comment_id}', tags = ['comment'], summary = 'Retrieve a blog comment',)
def get_comments(id : int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    This is for retrieving a comment of a blog

    - **id** = The users ID mandatory path parameters
    - **comment_id** = the id of a specific comment mandatory path parameters
    - **valid** optional query parameter
    - **username** The users name - optional query parameter
    """
    return{'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}', summary = 'Retrieve the type of blog',)
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}

@router.get('/{id}', status_code= status.HTTP_200_OK, summary = 'Retrieve a blog by blog ID')
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
