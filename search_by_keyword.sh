# Our youtube API key
API_KEY="AIzaSyDlrOVHZ8stkQCS52a1qf2f06zrvwnVPGw"

# Get keyword from shell
KEYWORD=$1

# Timestamp function
timestamp() {
  date +"%Y-%m-%d_%H-%M-%S"
}

curl \
  "https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&q=${KEYWORD}&key=${API_KEY}" \
  --header 'Accept: application/json' \
  --compressed \
  > output/search_"$KEYWORD"_$(timestamp).json
