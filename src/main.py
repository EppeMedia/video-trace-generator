import json

from get_video_ids import get_video_ids

with open('../output/search_kangaroo_2020-11-21_17-34-21.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
video_ids = get_video_ids(data)

print(video_ids)

with open('../output/video_ids_kangaroo_2020-11-21_17-34-21.json', 'w') as json_file:
  json.dump(video_ids, json_file)