import bs4
import urllib

post_params = {
    
        }
post_args = urllib.urlencode(post_params)

url = 'https://console.api.ai/api-client/#/agent/0290e0b9-b5ad-4f34-b089-512123e725b4/entities'
fp = urllib.urlopen(url, post_args)
soup = bs4(fp)