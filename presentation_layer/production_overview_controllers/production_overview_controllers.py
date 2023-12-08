from data_access_layer.read_database_functions import read_to_dataframe, read_selected_data_to_dataframe, read_selection_to_list
from data_access_layer.write_database_functions import db
from business_logic_layer.html_logic_module.scanner_html.scanner_html_controllers import packing_lists_html, pallet_list_html, pallet_info_html

import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def get_production_overview():
    try:
        html = """
                <!DOCTYPE html>
                <html>
                    <head>
                        <title>Production Overview</title>
                    </head>
                    <body>
                        <h1>Current Production</h1>
                        <form action="" onsubmit="sendMessage(event)">
                            <input type="text" id="messageText" autocomplete="off"/>
                            <button>Send</button>
                        </form>
                        <ul id='messages'>
                        </ul>
                        <script>
                            var ws = new WebSocket("ws://localhost:8000/production_overview");
                            ws.onmessage = function(event) {
                                var messages = document.getElementById('messages')
                                var message = document.createElement('li')
                                var content = document.createTextNode(event.data)
                                message.appendChild(content)
                                messages.appendChild(message)
                            };
                            function sendMessage(event) {
                                var input = document.getElementById("messageText")
                                ws.send(input.value)
                                input.value = ''
                                event.preventDefault()
                            }
                        </script>
                    </body>
                </html>

                """
        return html
    except Exception as ex:
        print("Data could not be processed: \n", ex)

# html_data = packing_lists_html(packing_lists);

