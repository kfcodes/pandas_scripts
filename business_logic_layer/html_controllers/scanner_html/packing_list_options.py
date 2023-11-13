def packing_lists(list):
    html = ""
    
    for row in list.iterrows():

        id = row[1]["packing_list_id"]
        name = row[1]["packing_list_name"]

        html = f"""
        {html}
        <a href="/packing_list/{id}"
            <button>
                {name} 
            </button>
        </a>
        </br>
        """

    return html
