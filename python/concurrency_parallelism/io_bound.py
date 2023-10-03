# reference: https://realpython.com/python-concurrency/
import requests
import time
import concurrent.futures
import threading
import asyncio
import aiohttp

thread_local = threading.local()

def download_site_sync(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites_sync(sites):
    with requests.Session() as session:
        for url in sites:
            download_site_sync(url, session)

async def download_site_async(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites_async(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

def download(func,sites):
    start_time = time.time()
    func(sites)
    duration = time.time() - start_time
    print(f"{func.__name__}: Downloaded {len(sites)} in {duration} seconds")

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    download(download_all_sites_sync,sites)