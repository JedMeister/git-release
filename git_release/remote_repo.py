from exceptions import GitReleaseError

import requests

class RemoteRepo:
    def __init__(self, url: str, repo: str):
        self.url = url

    def get_releases(self):

