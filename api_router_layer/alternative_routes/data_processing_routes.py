from fastapi import APIRouter
import os
from presentation_layer.data_controller_layer.data_processing_controllers.database_data import process_db_file
from presentation_layer.data_controller_layer.data_processing_controllers.label_data import process_label_file
from presentation_layer.data_controller_layer.data_processing_controllers.product_components import process_components_file
from presentation_layer.data_controller_layer.data_processing_controllers.po_data import process_po_files
from presentation_layer.data_controller_layer.data_processing_controllers.schedule_data import process_schedule_file

data_processing_router = APIRouter();

sheet = os.getenv("SHEETINPUT");

@data_processing_router.get("/process_files/process_db_file")
async def process_db_file_function():
    process_db_file()
    return {"message": "files processed"}
@data_processing_router.get("/process_files/process_label_file")
async def process_label_file_function():
    process_label_file();
    return {"message": "files processed"}
@data_processing_router.get("/process_files/process_components_file")
async def process_db_components_function():
    process_components_file();
    return {"message": "files processed"}
@data_processing_router.get("/process_files/process_po_file")
async def process_po_file_function():
    process_po_files();
    return {"message": "files processed"}
@data_processing_router.get("/process_files/process_schedule_file")
async def process_schedule_file_function():
    process_schedule_file(sheet);
    return {"message": "files processed"}
