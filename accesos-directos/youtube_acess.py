import os
import sys

def youtube_access():
    url = "https://youtube.com"
    print("Accediendo a youtube.com")
    os.system(f"xdg-open {url}")
youtube_access()