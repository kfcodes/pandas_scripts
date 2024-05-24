from data_presentation_layer.business_logic_layer.html_logic_module.scanner_html.scanner_html_components.packing_list_header import scanner_packing_lists_header
from data_presentation_layer.business_logic_layer.html_logic_module.scanner_html.scanner_html_components.packing_list_options import packing_lists
from data_presentation_layer.business_logic_layer.html_logic_module.scanner_html.scanner_html_components.close_html import close_html
from data_presentation_layer.business_logic_layer.html_logic_module.scanner_html.scanner_html_components.pallet_list_header import scanner_pallet_list_header
from data_presentation_layer.business_logic_layer.html_logic_module.scanner_html.scanner_html_components.pallet_id_list import pallet_list
from data_presentation_layer.business_logic_layer.html_logic_module.scanner_html.scanner_html_components.packing_list_options import packing_lists
from data_presentation_layer.business_logic_layer.html_logic_module.scanner_html.scanner_html_components.pallet_info_header import scanner_info_header
from data_presentation_layer.business_logic_layer.html_logic_module.scanner_html.scanner_html_components.pallet_info import pallet_info

def packing_lists_html(list):
    start = scanner_packing_lists_header();
    middle = packing_lists(list);
    end = close_html();
    html_file = f"{start}{middle}{end}"
    return html_file

def pallet_list_html(palls):
    start = scanner_pallet_list_header();
    middle = pallet_list(palls);
    end = close_html();
    html_file = f"{start}{middle}{end}"
    return html_file

def pallet_info_html(info):
    start = scanner_info_header();
    middle = pallet_info(info);
    end = close_html();
    html_file = f"{start}{middle}{end}"
    return html_file
