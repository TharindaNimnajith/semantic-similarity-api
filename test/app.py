# importing typing module
# defines a standard notation for python function and variable type annotations
# notation can be used for documenting code in a concise, standard format
from typing import Optional

# importing uvicorn library
# it is a lightning-fast ASGI server implementation, using uvloop and httptools
# ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to
# provide a standard interface between async-capable Python web servers, frameworks, and applications
import uvicorn
# importing fastapi framework
# a web framework for building apis with python
from fastapi import FastAPI
# importing RedirectResponse from fastapi responses package
# returns an http redirect
from fastapi.responses import RedirectResponse
# importing BaseModel class from pydantic library
# used to create a new model by parsing and validating input data from keyword arguments
from pydantic import BaseModel


# creating Item class inheriting BaseModel
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# creating an application instance
app = FastAPI()


# redirecting to swagger docs
@app.get('/')
async def root():
    return RedirectResponse(url='/docs')


# a simple http get api for testing purposes
@app.get('/hello')
async def root():
    return {
        'message': 'Hello World'
    }


# a simple http get api with path parameters for testing purposes
@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {
        'item_id': item_id
    }


# a simple http post api for testing purposes
@app.post('/items/')
async def create_item(item: Item):
    return item


# running the application on a local development server
if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=8000)
