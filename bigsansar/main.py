#!/usr/bin/python3

import os
from bigsansar.contrib.urls import path_handlers
from bigsansar.contrib.views import not_found_page
import cgitb

cgitb.enable()

def main():
    
    # Set the content type to HTML
    print("Content-type: text/html\n")

     # Get the path from the environment
    path = os.environ.get('PATH_INFO', '')
    # Define the URL path handlers

    # Call the appropriate handler based on the path
    page_content = path_handlers.get(path, not_found_page)()

    # Print the HTML response
    print(page_content)

if __name__ == "__main__":
    main()
