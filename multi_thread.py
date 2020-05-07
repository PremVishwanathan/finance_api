import threading
from queue import Queue
from Crawler.spider import *
from Crawler.domain import *
from Crawler.Main import *

Project_name= 'sec.gov'
Homepage='https://www.sec.gov/about.shtml/'
Domain_name = get_domain_name(Homepage)
Queue_file = Project_name + '/queue.txt'
Crawled_file = Project_name + '/crawled.txt'
Number_of_threads = 4
queue = Queue()
Spider(Project_name, Homepage, Domain_name)

def create_spiders():
    for _ in range(Number_of_threads):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
        
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

def create_jobs():
    for link in file_to_set(Queue_file):
        queue.put(link)
    queue.join()
    crawl()

def crawl():
    queue_links = file_to_set(Queue_file)
    if len(queue_links) > 0:
        print(str(len(queue_links)) + ' links in queue')
        create_jobs()
        
create_spiders()
crawl()