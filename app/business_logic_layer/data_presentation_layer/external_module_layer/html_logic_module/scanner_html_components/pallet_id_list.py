def pallet_list(pallets):
    html = ""
    
    for row in pallets.iterrows():
        html = f"""
            {html}
                    {row[1]['pallet_id']} 
            </br>
        """

    html = html + """
            </ul>
                <form method='post' action='/pallet'>
                    <input id='id' name='id' value=''>
                </form>
                <script>
                    window.onload = function() { document.getElementById('id').focus(); }
                </script>
            """

    return html
