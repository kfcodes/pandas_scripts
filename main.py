from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from presentation_layer.packing_list_controllers.get_packing_list_data_controllers import get_all_packing_lists
from presentation_layer.packing_list_controllers.get_packing_list_data_controllers import get_packing_list
from presentation_layer.packing_list_controllers.get_packing_list_data_controllers import get_pallet_info

import os
from dotenv import load_dotenv
load_dotenv(".env")

sheet = os.getenv("SHEETINPUT");

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def scanner_packing_lists():
    html_data = get_all_packing_lists();
    return HTMLResponse(content=html_data, status_code=200)

@app.get("/packing_list/{id}", response_class=HTMLResponse)
async def scanner_packing_list(id):
    html_data = get_packing_list(id);
    return HTMLResponse(content=html_data, status_code=200)

@app.get("/pallet/{id}", response_class=HTMLResponse)
async def scanner_pallet_info(id):
    html_data = get_pallet_info(id);
    return HTMLResponse(content=html_data, status_code=200)
