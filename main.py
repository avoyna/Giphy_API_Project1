from API_Connection import connect_API_giphy, show_files_tkinter


if __name__ == '__main__':
    return_records_limit = 5
    find_str = input("Type string to find {return_records_limit} images in Giphy (or leave blank to see trending pictures)): ")
    if find_str == "":
        retrieved_info, retrieved_small_gif_info = connect_API_giphy.retrieve_data(return_records_limit=return_records_limit)
    else:
        retrieved_info, retrieved_small_gif_info = connect_API_giphy.retrieve_data(issearch=True,
                                                                                   search_string=find_str,
                                                                                   return_records_limit=return_records_limit)
    connect_API_giphy.show_info(retrieved_info)

    show_files_tkinter.show_giphy_image(retrieved_small_gif_info)
