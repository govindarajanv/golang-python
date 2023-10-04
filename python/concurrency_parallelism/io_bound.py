# reference: https://realpython.com/python-concurrency/
import requests
import time
import concurrent.futures
import threading
import asyncio
import aiohttp

# multithreading
thread_local = threading.local()

# Sync version
def download_site_sync(url, session):
    with session.get(url) as response:
        #print(f"Read {len(response.content)} from {url}")
        pass

def download_all_sites_sync(sites):
    with requests.Session() as session:
        for url in sites:
            download_site_sync(url, session)

# multithreading
def get_session_mt():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site_mt(url):
    
    session = get_session_mt()
    with session.get(url) as response:
        #print(f"Read {len(response.content)} from {url}")
        pass

def download_all_sites_mt(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site_mt, sites)

# multiprocessing
def download_site_mp(url):
    session = requests.Session()
    with session.get(url) as response:
        #print(f"Read {len(response.content)} from {url}")
        pass


def download_all_sites_mp(sites):
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(download_site_mp, sites)

# async
async def download_site_async(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))
        #pass


async def download_all_sites_async(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site_async(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

def download(func,sites,asyncio_flag = False):
    start_time = time.time()
    if not asyncio_flag:
        func(sites)
    else:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(func(sites))
    duration = time.time() - start_time
    print(f"{func.__name__}: Downloaded {len(sites)} in {duration} seconds")

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    download(download_all_sites_sync,sites)
    download(download_all_sites_mt,sites)
    download(download_all_sites_mp,sites)
    download(download_all_sites_async,sites,True)