import os
import sys

def office365_access():
    url = "https://office.com"
    print("Accediendo a office 365")
    os.system(f"xdg-open {url}")
office365_access()