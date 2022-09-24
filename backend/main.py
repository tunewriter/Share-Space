import json
import os

import yaml

from fastapi import FastAPI, Request
from supabase import create_client, Client
from pydantic import BaseModel

app = FastAPI()
config = yaml.safe_load(open('backend/config.yml'))


names = ["maya", "alex"]
keys = ["abcd", "1234"]
logged = False

url = config['SUPABASE_URL']
key = config['SUPABASE_KEY']

supabase: Client = create_client(url, key)


class Note(BaseModel):
    cave_key: str
    data: str


@app.get("/")
async def home():
    data = {
        "page": "Home Page"
    }
    return data


@app.post("/add/")
async def save_name(name: str):
    names.append(name)


@app.post("/addnote/")
async def save_name(note: Note):
    note_dict = {
        'cave_key': note.cave_key,
        'data': note.data
    }
    supabase.table("Notes").insert(note_dict).execute()
    return note


# sending list with GET
@app.get("/notes/{key}")
async def send_notes(key: str):
    notes = supabase.table("Notes").select("id", "created", "data").eq('cave_key', key).execute()
    print(notes)
    return {json.dumps(notes.data)}


@app.get("/check/{key}")
async def check(key: str):
    if key in keys:
        logged = True
        return {'True'}
    return {'False'}


# sending list with GET
@app.get("/names/")
async def show_names():
    return {json.dumps(names)}


# sending string with GET
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {f"Hello {name}"}
