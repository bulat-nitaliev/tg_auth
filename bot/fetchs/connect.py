import aiohttp
import os


class Http:
    url_http:str = 'http://backend:8000'

    async def get(self, url, headers:dict={}):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers) as response:
                return await response.json()
            
    async def post(self, url:str, headers:dict, data:dict):
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers, data=data) as response:
                return await response.json()
            
    async def delete(self, url:str, headers:dict):    
        async with aiohttp.ClientSession() as session:
            async with session.delete(url=url, headers=headers) as response:
                return  {'result': 'success'}
            
http = Http()


async def register(data:dict)->None:
    url = http.url_http + '/api/users/'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            # return await response.json()
            content_type = response.headers.get('Content-Type')
            if content_type == 'application/json':
                data = await response.json()
                print(data)
            else:
                html_content = await response.text()
                # print(html_content)


async def login(data:dict)->None:
    
    url = http.url_http + '/api/token/'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            return await response.json()

async def islam(data:dict, access_token)->None:
    url = http.url_http + '/api/islam/'
    print(url)
    
    headers={'Authorization': f'Bearer {access_token["access"]}',
        'accept': 'application/json'
    }
    return await http.post(url=url,headers=headers, data=data)


