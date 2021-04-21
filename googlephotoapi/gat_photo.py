from gphotospy import authorize
from gphotospy.album import *
from gphotospy.media import *
CLIENT_SECRET_FILE = 'client_secret.json'

service = authorize.init(CLIENT_SECRET_FILE)

album_manager = Album(service)

print(album_manager)