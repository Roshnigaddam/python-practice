#2. unittest function for download function (You can use any library, I would recommend pytest)
#def test_download_gh():
   #Implement Assertion 



import pytest
import os
from download_gh import download_gh


def test_download_gh():
    
    expected_path = '/Users/roshnigaddam/Downloads/selectiva/python/2023-03-01-10.json.gz'
    
    # remove exising file for testing
    if os.path.exists(expected_path):
        os.remove(expected_path)
    
    result = download_gh(date='2023-03-01', hour=10)
    print(result)
    
    #check if the download_gh() function returns the expected value
    assert result == expected_path
    
    #check successfull file download
    assert os.path.exists(expected_path)
    
    