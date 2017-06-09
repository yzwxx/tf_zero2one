from __future__ import print_function
import os,sys,gzip,requests
from tqdm import tqdm
from six.moves import urllib

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination, chunk_size=32*1024):
    total_size = int(response.headers.get('content-length', 0))
    with open(destination, "wb") as f:
        for chunk in tqdm(response.iter_content(chunk_size), total=total_size,
                unit='B', unit_scale=True, desc=destination):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def download_file_from_google_drive(id, destination):    
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()

    response = session.get(URL, params={ 'id': id }, stream=True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)

def download_caption(dirpath):
    data_dir = 'cvpr2016_flowers.tar.gz'
    if os.path.exists(os.path.join(dirpath, data_dir)):
        print('Found cvpr2016_flowers.tar.gz - skip')
        return

    filename, drive_id  = "cvpr2016_flowers.tar.gz", "0B0ywwgffWnLLcms2WWJQRFNSWXM"
    save_path = os.path.join(dirpath, filename)

    if os.path.exists(save_path):
        print('[*] {} already exists'.format(save_path))
    else:
        download_file_from_google_drive(drive_id, save_path)


if __name__ == '__main__':
	download_caption('.')