from gphotospy import authorize
from gphotospy.media import Media
from gphotospy.media import CONTENTFILTER, MEDIAFILTER, FEATUREFILTER
from gphotospy.media import date, date_range
from gphotospy.album import Album
from googleapiclient.errors import HttpError
import requests, os

def checkexits(destination_folder:str, file_name:str):
    
    if os.path.isfile(os.path.join(destination_folder, file_name)):
        print ("File exist : %s" %(file_name))
        return False
    
    #print ("File not exist")
    return True

def download_file(url:str, destination_folder:str, file_name:str):
    if checkexits(destination_folder, file_name):
        response = requests.get(url)
        if response.status_code == 200:
            print('Downloading file {0}'.format(file_name))
            with open(os.path.join(destination_folder, file_name), 'wb') as f:
                f.write(response.content)
                f.close()
            

# Select secrets file
CLIENT_SECRET_FILE = "client_secret.json"

# Get authorization and return a service object
service = authorize.init(CLIENT_SECRET_FILE)

# Init the media manager
media_manager = Media(service)

# Set default behaviors (don't show archived media)
media_manager.show_archived(False)

# Get iterator over the list of media
print("Getting a list of media...")
media_iterator = media_manager.list()

destination_folder = r'/data/images/'

for media_image in media_iterator:
    #print(media_image)
    
    #print(media_image.get("filename"))
    #print(media_image.get("productUrl"))
    #print(media_image.get("baseUrl"))
    #print(media_image.get("mimeType"))
    
    file_name = media_image.get('filename')
    download_url = media_image.get('baseUrl') + '=d'
    
    download_file(download_url, destination_folder, file_name)
    
print("Download Success")
    
#next(media_iterator).get("filename"))