from fastapi import FastAPI, Request
from supabase import create_client, Client
from pydantic import BaseModel

import json
import yaml


app = FastAPI()
config = yaml.safe_load(open('backend/config.yml'))

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

    data = supabase.table("Caves").select("cave_key", count="estimated").eq('cave_key', key).execute()
    if data.count:
        logged = True
        return {'True'}
    return {'False'}


# delete note
@app.delete("/delete_note/{cave_key}/{note_id}")
async def delete_note(cave_key: str, note_id: int):
    supabase.table("Notes").delete().eq("id", note_id).eq("cave_key", cave_key).execute()
    return {
        "ok": True
    }
