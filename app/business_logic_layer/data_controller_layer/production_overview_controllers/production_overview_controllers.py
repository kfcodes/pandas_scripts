from physical_layer.data_access_layer.read_database_functions import read_to_dataframe, read_selected_data_to_dataframe, read_selection_to_list
from physical_layer.data_access_layer.write_database_functions import db
from business_logic_layer.external_module_controllers.html_logic.scanner_html_components import packing_lists_html, pallet_list_html, pallet_info_html

import os
from dotenv import load_dotenv
load_dotenv("../.env")

def update_production_overview():
    try:

        html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Update Production Overview</title>

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

        <script>
            var ws = new WebSocket(`ws://localhost:8000/current_production`);
            ws.onmessage = function(event) {
                var new_products = document.getElementById('product')
                var new_product = document.createElement('H4')
                var content = document.createTextNode(event.data)
                new_product.appendChild(content)
                new_products.appendChild(new_product)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>

    </head>
    <body>

    <div class="container mt-3">
        <h1>Current Production</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" class="form-control" id="messageText" autocomplete="off"/>
            <button class="btn btn-outline-primary mt-2">Send</button>
        </form>
        <hr>
        <H2 id='product' class="mt-5">
        </H2>
    </div>

    </body>
</html>
"""

        return html
    except Exception as ex:
        print("Data could not be processed: \n", ex)

def get_production_overview():
    try:
        html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Production Overview</title>

           <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
           <!-- Jquery CDN import  -->

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>

        <script>
            var ws = new WebSocket(`ws://localhost:8000/current_production`);
            ws.onmessage = function(event) {
                var content = document.createTextNode(event.data)
                get_data(content)
            }
            async function get_data(product) {
              const response = await fetch(`http://localhost:8000//${product}`);
              const product_data = await response.json();
              console.log(product_data);
            }

            </script>

    </head>
    <body>

    <div class="container mt-3">
        <h1>Current Production</h1>
        <hr>
    </div>
    
    </body>
</html>
"""
        return html
    except Exception as ex:
        print("Data could not be processed: \n", ex)

# html_data = packing_lists_html(packing_lists);

def get_product_overview(product):
    try:
        product_information = get_label_data(f"{os.getenv('GETPRODUCTIONOVERVIEW')}{product}")
        outline = create_small_label_outline()
        body = create_small_label_data(label_info, 1)
        label_data = outline + body
        print_small_label(label_data)
        return 
    except Exception as ex:
        print("Data could not be processed: \n", ex)
        set_current_product = new_product;
