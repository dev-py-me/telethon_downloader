import os

from logger import logger

def get_env(name, message, cast=str):
	if name in os.environ:
		logger.info(f'{name} : {os.environ[name]}')
		return os.environ[name].strip()
	else:
		logger.info(f'{name} : {message}')
		return message




# Define some variables so the code reads easier
SESSION = os.environ.get('TG_SESSION', 'bottorrent')
api_id = get_env('TG_API_ID', 'Enter your API ID: ', 7712824)
api_hash = get_env('TG_API_HASH', 'Enter your API hash: ','2d3673e18b462f8032c4eea2f50b9f52')
bot_token = get_env('TG_BOT_TOKEN', 'Enter your Telegram BOT token: ','2073401563:AAFOL_jXMsqIhZCVPt2gqE4mrwy0MJTykI0')
TG_AUTHORIZED_USER_ID = get_env('TG_AUTHORIZED_USER_ID', False)
TG_DOWNLOAD_PATH = get_env('TG_DOWNLOAD_PATH', '/content/download')
TG_DOWNLOAD_PATH_TORRENTS = get_env('TG_DOWNLOAD_PATH_TORRENTS', '/content/watch')
YOUTUBE_LINKS_SOPORTED = get_env('YOUTUBE_LINKS_SOPORTED', 'youtube.com,youtu.be')
YOUTUBE_FORMAT = get_env('YOUTUBE_FORMAT', 'bestvideo+bestaudio/best')  #best
TG_UNZIP_TORRENTS = get_env('TG_UNZIP_TORRENTS', False)
TG_PROGRESS_DOWNLOAD = get_env('TG_PROGRESS_DOWNLOAD', False)
TG_FOLDER_BY_AUTHORIZED = get_env('TG_FOLDER_BY_AUTHORIZED', False)

TG_MAX_PARALLEL = int(os.environ.get('TG_MAX_PARALLEL',4))
TG_DL_TIMEOUT = int(os.environ.get('TG_DL_TIMEOUT',3600))
YT_DL_TIMEOUT = int(os.environ.get('TG_DL_TIMEOUT',7200))

PATH_TMP = os.path.join(TG_DOWNLOAD_PATH,'/content/tmp')
PATH_COMPLETED = os.path.join(TG_DOWNLOAD_PATH,'completed')
PATH_YOUTUBE = os.path.join(TG_DOWNLOAD_PATH,'youtube')

PATH_CONFIG = '/config/config.ini'

YOUTUBE = 'youtube'
