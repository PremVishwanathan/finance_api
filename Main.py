import os


# Creating folders for each link available
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)
        
#create_project_dir("Demo")

#Create queue and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#Creating new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
    
#create_data_files('demo', 'https://demo.com/')

#Adding data to files
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        
#Delete data from file
def delete_file_content(path):
    with open(path, 'w'):
        pass

#Converting file content into a set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#Writing set values into a file
def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)