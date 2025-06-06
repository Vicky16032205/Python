from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

@app.get('/')
def function():
    return {"data":{"name" : "Vicky Kumar Gupta"}}

@app.get('/about')
def about():
    return {'Student' : 'G.L. BAJAJ'}

# this is taking parameterized values in the url.

@app.get('/blog/unpublished')
def unpublished():
    return {"data" : "all unpublished blogs"}

@app.get('/blog/{id}')
def show(id: int):
    return {"data" : id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {"data":('1' , '2' , '3')}


# Query Parameters will be written down here.

@app.get('/blog') # this will be taking limit in the browser url and will perform functions.
# the url will be like this, say localhost:8000/blog?limit=50&published= true, then it will come here and check conditions in this function.
def func(limit, published: bool):
    if published:
        return {"data":f'{limit} published blog list from the database.'}
    else:
        return {"data":f'{limit}  blog list'}


# what the above function is doing will be done same here but without user interventions.

@app.get('/blog?limit=10&published=true')    #this query will search for blogs and will print only 10 values having unpublished == true.
def func():
    return {"data":'blog list'}





# From here on we will study about the post-operation in FastAPI.
# This is done using the pydantic library from where we will be importing the BaseModel library.

class Blog(BaseModel):
    title : str
    body: str
    published : Optional[bool]

@app.post('/create')
def create_blog(blog : Blog):
    return {'blog' : f"Blog is created with Blog title as {blog.title}"}