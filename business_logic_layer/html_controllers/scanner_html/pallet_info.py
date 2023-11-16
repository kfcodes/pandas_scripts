def pallet_info(info):
    
    for row in info.iterrows():

        id = row[1]["id"]
        weight = row[1]["GrossWeight"]
        height = row[1]["GrossHeight"]
        size = row[1]["PalletType"]
    
        html = f"""

                    <H1>
                        {id} 
                    </H1>
                    <h3>
                        {size} 
                    </h3>
                    <h4>
                        {height} (cm) 
                    </h4>
                    <h4>
                        {weight} (kg) 
                    </h4>

                    </br>

                    <a href="/load_pallet/{id}"
                        <button>
                            LOAD PALLET
                        </button>
                    </a>

        """

        return html
