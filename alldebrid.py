import httpx
from dotenv import load_dotenv
import os

load_dotenv()
APP_NAME = os.getenv('APP_NAME')
ALLDEBRID_TOKEN = os.getenv('ALLDEBRID_TOKEN')

class AllDebrid():
    def unlockLink(link):
        api_url = f"https://api.alldebrid.com/v4/link/unlock?agent={APP_NAME}&apikey={ALLDEBRID_TOKEN}&link={link}"
        r = httpx.get(api_url)
        content = r.json()
        if content['status'] == "success":
            if "infos" in content['data']  and "error" in content['data']['infos'][0]:
                return {"status": "error", "message": "{}:{}".format(content['data']['infos'][0]['error']['code'], content['data']['infos'][0]['error']['message'])}
            else:
                return {"status": "success", "message": content['data']['link']}
        else :
            return {"status": "error", "message": content['error']['message']}