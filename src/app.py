from fastapi import FastAPI, HTTPException
from schemas import PostCreate 
from db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession 
from contextlib import asynccontextmanager 

@asynccontextmanager 
async def lifespan(app: FastAPI): 
    await create_db_and_tables() 
    yield

app = FastAPI(lifespan = lifespan)

text_posts = {
    1: {"title": "New_post", "content": "cool test post"},
    2: {"title": "Launch_note", "content": "first release is live"},
    3: {"title": "Bug_fix", "content": "patched the login crash"},
    4: {"title": "Feature_drop", "content": "added dark mode"},
    5: {"title": "User_story", "content": "power users love the speed"},
    6: {"title": "Hot_update", "content": "performance improved by 30 percent"},
    7: {"title": "Community", "content": "thanks for the amazing feedback"},
    8: {"title": "Behind_the_scenes", "content": "rewrote the core engine"},
    9: {"title": "Roadmap", "content": "next up is offline support"},
    10: {"title": "Milestone", "content": "one thousand active users"}
}


@app.get("/posts")
def get_all_posts():
    return text_posts 


@app.get("/posts/{id}") 
def get_post(id: int): 
    if id not in text_posts: 
        raise HTTPException(status_code=404, detail = "Post not found") 
    return text_posts.get(id) 


@app.post("/posts") 
def create_post(post: PostCreate): 
    new_post = {"title": post.title, "content": post.content} 
    text_posts[max(text_posts.keys()) + 1] = {"title": post.title, "content": post.content}
    return new_post 

