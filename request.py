import requests
import asyncio

url_api = "http://127.0.0.1:8000"

async def main():
    _post = requests.post(f"{url_api}/url", json={
        "target_url": "http://blogshistory.ru"
    })

    print (f"{"="*20}\nPOST: \nstatus code:{_post.status_code}\nresult: {_post.content}\n{"="*20}")

    
    _get = requests.get(f"http://127.0.0.1:8000/{_post.json()['key']}")

    print (f"GET: \nstatus code:{_get.status_code}\nheaders: {_get.headers}")


if __name__ == "__main__":
    asyncio.run(main())