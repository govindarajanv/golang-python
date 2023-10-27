# access the scraping endpoint http://localhost:4000/

import time
import random
from os import path
import yaml
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
totalRandomNumber = 0

class RequestsCollector(object):
    def __init__(self):
        pass
    def collect(self):
        gauge = GaugeMetricFamily("req_per_sec", "Current rate of requests", labels=["requestsNum"])
        req_count = random.randint(1, 20)
        gauge.add_metric(['num_requests'], req_count)
        yield gauge

        count = CounterMetricFamily("total_req_per_sec", "Total throughput on this black Friday", labels=['requestsNum'])
        global totalRandomNumber
        totalRandomNumber += req_count
        count.add_metric(['num_requests'], totalRandomNumber)
        yield count

if __name__ == "__main__":
    port = 9000
    frequency = 1
    if path.exists('config.yml'):
        with open('config.yml', 'r') as config_file:
            try:
                config = yaml.safe_load(config_file)
                port = int(config['port'])
                frequency = config['scrape_frequency']
            except yaml.YAMLError as error:
                print(error)

    start_http_server(port)
    REGISTRY.register(RequestsCollector())
    while True:
        # period between collection
        time.sleep(frequency)