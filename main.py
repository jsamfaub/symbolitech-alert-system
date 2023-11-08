#!/usr/bin/env python

import os
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
os.chdir(script_directory)

from functions import *
import controllers

if __name__ == "__main__":
    success_rate_controller=controllers.SuccessRateController('success_data.json')
    url_status_controller=controllers.UrlStatusController('status_data.json')
    urls=[] #add a list of url strings
    
    test_urls(urls, success_rate_controller, url_status_controller)
