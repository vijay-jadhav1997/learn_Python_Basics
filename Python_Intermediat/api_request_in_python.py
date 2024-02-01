import json
import requests
import sys

# define main fn
def main():
  if len(sys.argv) != 2:
    sys.exit("Please, enter valid arguments....")

  getData()


# define getData fn
def getData():
  response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
  data = response.json()
  # formatted_data = json.dumps(data, indent=2)

  for result in data["results"]:
    print(result["trackName"])




main()