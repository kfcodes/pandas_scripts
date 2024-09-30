from physical_layer.data_access_layer.read_database_functions import read_selection_to_list, read_to_list_index
from fastapi.encoders import jsonable_encoder

import os
from dotenv import load_dotenv
load_dotenv(".env")

async def get_production_review_information():
    try:
        review_data = read_to_list_index(f"{os.getenv('GETPRODUCTIONREVIEWSUMMARY')}")
        review_array = []
        for key, val in review_data.items():
            review_array.append(val)
        review_array = jsonable_encoder(review_array)
        return review_array
    except Exception as ex:
        print("Data could not be processed: \n", ex)
