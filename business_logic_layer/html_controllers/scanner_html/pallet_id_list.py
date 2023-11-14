def pallet_list(pallets):
    html = ""
    
    for row in pallets.iterrows():

        html = f"""
            {html}
                        {row[1]['pallet_id']} 
            </br>
        """

        html = f"{html} </ul>"
    return html
