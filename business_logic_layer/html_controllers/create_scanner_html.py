from business_logic_layer.html_controllers.scanner_packing_lists_header import scanner_packing_lists_header
from business_logic_layer.html_controllers.scanner_packing_lists_list import packing_lists
from business_logic_layer.html_controllers.close_html import close_html

def create_packing_list_html():
    start = scanner_packing_lists_header();
    middle = packing_lists();
    end = close_html();
    
    html_file = f"{start}{middle}{end}"

    return html_file
