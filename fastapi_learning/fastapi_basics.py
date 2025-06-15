from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def function():
    return {'main': {'Welcome to fastapi'}}

@app.get('/about')
def about():
    return {'Student' : 'G.L. BAJAJ'}