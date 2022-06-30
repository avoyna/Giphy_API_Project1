import requests

API_KEY="QxgO5J0IGHTvyaAYaRCeDMNw7EuhW271"
ENDPOINT_trending="https://api.giphy.com/v1/gifs/trending"
ENDPOINT_search="https://api.giphy.com/v1/gifs/search"

def retrieve_data(api_key=API_KEY, issearch=False, endpoint=ENDPOINT_trending, return_records_limit=3, rating='g', search_string=""):
    result_info = []
    result_small_gif_info = []
    img_tuple=()

    if issearch:
        ENDPOINT = ENDPOINT_search
        params={"api_key":API_KEY, "limit":return_records_limit,"rating":rating, "q":search_string}
    else:
        ENDPOINT = ENDPOINT_trending
        params={"api_key":API_KEY, "limit":return_records_limit, "rating":rating}

    try:
        response = requests.get(ENDPOINT, params=params)
        response.raise_for_status()
        response_json = response.json()
        #print(response.url)
        #print(response.text)
        #print(response_json)
        for gif in response_json["data"]:
            title = gif["title"]
            url = gif["url"]
            url_fixed_height_small = gif["images"]["fixed_height"]["url"]
            height_fixed_height_small = gif["images"]["fixed_height"]["height"]
            width_fixed_height_small = gif["images"]["fixed_height"]["width"]
            input_str = title + " | " + url
            result_info.append(input_str)
            img_tuple =  url_fixed_height_small, height_fixed_height_small, width_fixed_height_small
            result_small_gif_info.append(img_tuple)

    except requests.exceptions.RequestException as e:
        print("Connection error - code {}: {}".format(response.status_code, str(e)))

    return result_info, result_small_gif_info

def show_info(result_info=[]):
    if len(result_info)>0:
        for row in result_info:
            print(row) #,"\n")

    return