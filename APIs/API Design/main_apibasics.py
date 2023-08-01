from typing import Optional     # Importing library to set optional variables
from fastapi import FastAPI, Response, status, HTTPException     # Importing fastapi library, and Response to format responses of fastapi
from fastapi.params import Body # Used to store posts
from pydantic import BaseModel  # Used to define schema for input validation
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()                 # Creating a fastapi instance 

while True: # This code allows for repeated attempt to connect if not connected and breaks if connected remain connected.
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Target123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Connection Successful')
        break
    except Exception as error:
        print("Connecting to database failed")
        print('Error: ', error)
        time.sleep(2)   # If a connection fails, take a 2 second break before trying to re-reconnect

class Post(BaseModel):  # Defining schema for validation purposes
    title: str
    body: str
    published: bool = True     # Default value set to True if user doesn't provide value. This makes it an optional filled
    rating: Optional[int] = None    # This is an optional field that can take an integer or nothing if not given. 
                                    # Note, it won't take a string

# This array will be used to store posts which will be called with get
my_posts = [{"title": "title of post 1", "body": "content of post 1", "id":1},{"title":"favorite foods", "body": "I like Pizza", "id": 2}]       

def find_post(id):            # Finding a list from my_posts if list id = given id. Not id is a string when you query it in postman
    for p in my_posts:
        if p["id"]==id:
            return p

def find_index_post(id):                # extracting index of dictionary
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
        
@app.get("/")   # This decorator changes this function into a path operator. app is being called using @.
                # get is an http method used to read and return a data
                # Meaning where you will get this function when you visit the url. 
                # In this case, it is at the root meaning 
                # when you hit 'http://127.0.0.1:8000/', the function will run and return 'Hello World'
                # Note that the first matching path is seen in the browser if two path operations are identical
async def root():
    return {"message": "Hello World from Virginia"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}   # Reading back posts

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)): # all of the fields from the body is going to be
#                                              # converted into a python dictionary and stored inside 
#                                              # a variable named payload
#     print(payload)                           # This will print post in the Terminal
#     return {"new_post":f"title {payload['title']} content: {payload['body']}"}    # This will print post in Web/Postman

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post): # post is a place holder that will validate input
    # print(post)               # and used to print input in termial
    # print(post.dict())        # and used to print input in termial
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000) # Generating random id every time a post entry is made
    my_posts.append(post_dict)              # This appends post to post_placeholder which is my_posts
    return {"data": post_dict}              # This will print post in Web/Postman

@app.get("/posts/latest")                   # Order matters since if you put this function below "/posts/{id}", it will be invalid
def get_latest_post():                      # since it will throw an error since this is not an integer
    post=my_posts[-1]                       # = posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/posts/{id}")                     # Path parameters will always be string
def get_post(id: int, response: Response):                      # input validation to make input integer. That will throw an error if input is string 
    post=find_post(id)
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,          # Same output as the two rows commented out below but simpler
                            detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND        # status used to identify status codes. No need to memorize response numbers.
        # return {'message': f"post with id: {id} was not found"} # Output formatted to let reader know it is not found 
    print(post)
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id) # Getting the index

    if index == None:           # Throwing an error message if an index doesn't exist 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} does not exist')

    my_posts.pop(index) # Popping a value based on the index
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    # return {'message': f'post with id: {id} was successfuly deleted'} # We don't normally want to retun data after deleting an item

@app.put("/posts/{id}") # User requests to update a record by indicating the id
def update_post(id: int, post: Post):   # int id taken and data placed in json body taken to post place holder
    index = find_index_post(id) # Getting the index

    if index == None:           # Throwing an error message if an index doesn't exist 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} does not exist')

    post_dict = post.dict()     # Converting new data into a Python dictionary
    post_dict['id'] = id        # Generating an id column for the record being updated
    my_posts[index] = post_dict # Assigning to the id values for the other columns
    return {'message': "Updated post"}

