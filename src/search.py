def search(keyword):

    

    with open('../output/video_ids_kangaroo_2020-11-21_17-34-21.json', 'w') as json_file:
        json.dump(video_ids, json_file)

    return search_results;

def get_video_ids(search_json):

    video_ids = []

    for search_result in search_json["items"]:
        video_ids.append(search_result["id"]["videoId"]);

    return video_ids