def pallet_list(pallets):

    html = ""
    html = """
             <hr>
             <form method='post' action='/pallet'>
                  <table>
                    <tr>
                      <td><input id='id' name='id' value=''></td>
                    </tr>
                  </table>
                  <input type='submit' name='submit' value='Submit'>
                </form>
                <script>
                  window.onload = function() { document.getElementById('id').focus(); }
                </script>
            """
    
    for row in pallets.iterrows():
        html = f"""
            {html}
                    {row[1]['pallet_id']} 
            </br>
        """

    html = html + """
             <hr>
            </ul>
            """

    return html
