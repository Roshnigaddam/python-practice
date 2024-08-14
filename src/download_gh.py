#10. Request library for rest calls 

#Please develop two python functions to download GitHub Activity History files using Python3 requests library. 

#End Point = https://data.gharchive.org/2015-01-01-{0..23}.json.gz

#API Documentation can be found here = https://www.gharchive.org/

#I want you guys to develop 2 functions. 

#1. Download files function 

#def download_gh():
   #Download File of 2023 March 01 10AM into your computer filesystem 
   #Return fully qualified path of downloaded file from your computer filesystem
#   End_Point = https://data.gharchive.org/2015-01-01-{0..23}.json.gz
   
import requests
import os

import os
import wget

def download_gh(date,hour):
    # endpoint
    end_point = f"https://data.gharchive.org/{date}-{hour}.json.gz"
    
    # Define the local path to save the file
    local_filename = f"{date}-{hour}.json.gz"
    local_path = os.path.join('/Users/roshnigaddam/Downloads/selectiva/python/', local_filename)

    # Send a GET request to the URL
    response2 = requests.get(end_point, stream=True)
    print(response2)
    
    # Check if the request was successful
    if response2.status_code == 200:
        with open(local_path, 'wb') as f:
            for chunk in response2.iter_content(chunk_size=8192):
                f.write(chunk)
        return local_path
    else:
        raise Exception(f"Failed to download the file: {response2.status_code}")


download_gh(date='2023-03-01', hour=10)




