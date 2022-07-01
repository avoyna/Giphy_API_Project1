import os, sys
from API_Connection import connect_API_giphy, show_files_tkinter
from dotenv import load_dotenv


if __name__ == '__main__':
# uploading enviromental variables from ".env" file
    load_dotenv()

    return_records_limit = 5
    API_KEY = os.getenv("GIPHY_API_KEY")
    if (API_KEY==None):
        sys.exit("Can't load GIPHY API_KEY")
    find_str = input("Type string to find {} images in Giphy (or leave blank to see trending pictures): ".format(return_records_limit))
    if find_str == "":
        retrieved_info, retrieved_small_gif_info = connect_API_giphy.retrieve_data(api_key=API_KEY,
                                                                                   return_records_limit=return_records_limit)
    else:
        retrieved_info, retrieved_small_gif_info = connect_API_giphy.retrieve_data(api_key=API_KEY,
                                                                                   issearch=True,
                                                                                   search_string=find_str,
                                                                                   return_records_limit=return_records_limit)
    connect_API_giphy.show_info(retrieved_info)

    show_files_tkinter.show_giphy_image(retrieved_small_gif_info)
