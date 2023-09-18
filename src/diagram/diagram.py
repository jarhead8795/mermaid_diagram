import weather_api

MERMAID_FILE = 'weather_diagram.md'
MERMAID_HEADER = "```mermaid\ngraph LR;"


def generate_mermaid_markdown(zip_code, country_code = None, api_key = None): 
    """
    Uses the weather_api to get weather data for the given zip code
    and generates the mermaid markdown and writes it to a file in the local folder
    
    Args:
        zip_code (str) : The zip code
        country_code (str): Country code (Optional)
        api_key (str): A valid API key for the weather api.
    Returns:
        None
    """
    location_info = weather_api.get_location(zip_code, country_code, api_key = api_key)
    lat = location_info.get('lat')
    lon = location_info.get('lon')
    data = weather_api.get_weather_forecast(lat = lat, lon = lon, api_key = api_key)

    mermaid_md = []

    for parent, children in data.items():
        _get_children(children, parent, mermaid_md)

    _write_mermaid_md(mermaid_md)


def _get_children(children, parent: str, mermaid_md):
    """
    Helper function to extract parent child relationship 
    from the provided JSON data which is then used to generate 
    a mermaid diagram.

    This function uses recursion to get the data from all nodes.
    
    Args:
        children (dict | list | str) : data to be extracted
        parent (str) : This is the parent value of the node relationship 
        mermaid_md (list) : This holds the extracted data

    Returns:
        None
    """
    if isinstance(children, dict):
        for k, v in children.items():
            chain = f"{parent}-->"
            chain += f"{parent}_{k}-->"
            if isinstance(v, dict):
                _get_children(v, chain)
            else:
                if isinstance(v, list):
                    counter = 0
                    for _ in v:
                        _get_children(_, chain)
                        counter +=1
                else:
                    v = str(v).replace(' ','_')  # replace spaces with underscore to prevent syntax errors on render
                    chain += f"{v};"
                    mermaid_md.append(chain)
    else:
        if isinstance(children, list):
            counter = 0
            for _ in children:
                parent =f"{parent}_{counter}"
                _get_children(_, parent, mermaid_md)
        else:
            children = str(children).replace(' ','_')  # replace spaces with underscore to prevent syntax errors on render
            chain = f"{parent}-->"
            chain += f"{children};"
            mermaid_md.append(chain)


def _write_mermaid_md(mermaid_data):
    """
    Writes the mermaid data to a file in the local folder
    
    Args:
        mermaid_data (list) : List containing the mermaid markdown
        
    Returns:
        None
    """
    try:
        with open(MERMAID_FILE, 'w') as fp:
            fp.write("%s\n" % MERMAID_HEADER)
            for _ in mermaid_data:
                fp.write("    %s\n" % _)
    
    except Exception as e:
        print(f"Failed to write file to disk. error is {e}")
        return
    
    print(f"Output written to {MERMAID_FILE}")