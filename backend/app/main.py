from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

import json
import os.path

import random
import string

app = FastAPI()

origins = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "https://fantastic-panda-338891.netlify.app/",
    "http://syncave.com",
    "http://www.syncave.com",
    "https://syncave.com",
    "https://www.syncave.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')

supabase: Client = create_client(url, key)

# TODO: Handling invalid data with HTTPExceptions


class Note(BaseModel):
    cave_key: str
    data: str


@app.get("/")
async def home():
    data = {
        "page": "Home Page"
    }
    return data


@app.post("/addnote/")
async def save_note(note: Note):
    note_dict = {
        'cave_key': note.cave_key,
        'data': note.data
    }
    supabase.table("Notes").insert(note_dict).execute()
    return note


# get list of notes with GET
@app.get("/notes/{key}")
async def get_notes(key: str):
    notes = supabase.table("Notes").select("id", "created", "data").eq('cave_key', key).execute()
    print("notes", notes)
    return {json.dumps(notes.data)}


@app.get("/check/{key}")
async def check(key: str):
    res = supabase.table("Caves").select("*", count="estimated").eq('cave_key', key).execute()
    print(res.count)
    if res.count:
        board_name = res.data[0]['cave_name']
        return {'state': 'true',
                'name': board_name}
    return {'state': 'false',
            'name': ''}


# delete note
@app.delete("/delete_note/{cave_key}/{note_id}")
async def delete_note(cave_key: str, note_id: int):
    supabase.table("Notes").delete().eq("id", note_id).eq("cave_key", cave_key).execute()
    return {
        "ok": True
    }


def random_key(n):
    # get random password pf length 8 with letters, digits, (+ string.punctuation)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(n))


class Cave(BaseModel):
    creator_name: str
    cave_name: str


# create cave
@app.post("/createcave/")
async def create_cave(cave: Cave):
    print(cave)
    #  generate random cave_key with 8 letters/digits
    key = random_key(8)
    cave_dict = {
        'cave_name': cave.cave_name,
        'creator_name': cave.creator_name,
        'cave_key': key
    }
    supabase.table("Caves").insert(cave_dict).execute()
    return {"key": key}


class Feedback(BaseModel):
    email: str
    text: str


# save feedback
@app.post("/feedback/")
async def get_feedback(feedback: Feedback):
    print(feedback)
    feedback_dict = {
        'email': feedback.email,
        'text': feedback.text,
    }
    supabase.table("Feedback").insert(feedback_dict).execute()
    return {"ok": True}