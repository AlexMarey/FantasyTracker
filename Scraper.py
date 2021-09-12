from requests import get
from requests.exceptions import RequestException
from contextlib import closing

class Scraper():
    def __init__(self):
        return

    def simple_get(self, url):
        """
        Attempts to get the content of the url by making an HTTP GET request. 
        If the content-type of response is some kind of HTML/XML, 
        return the text content, otherwise it returns None
        """
        try:
            with closing(get(url, stream=True)) as resp: 
                if self.is_good_response(resp):
                    return resp.content
                else: 
                    return None
        except RequestException as e: 
            log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None


    def is_good_response(self, resp):
        """
        Returns true if the response is HTML.
        Returns false otherwise
        """
        content_type = resp.headers['Content-Type'].lower()
        return(resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)


    def log_error(self, e): 
        """
        Prints error messages.
        """
        print(e)