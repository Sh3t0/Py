from datetime import datetime as dt
import functools
import os

def wrapper_log_file(logged_action, log_file_path):
    print('wykonanie funkcji wrapper_log_file')
    def wrapper_with_log_to_known_file(func):
        print('wykonanie funkcji wrapper_with_log_to_known_file')
        def the_real_wrapper(path):
            print('wykonanie funkcji the_real_wrapper')
            with open(log_file_path, 'a') as f:
                f.write('{}: Action {} executed on {}\n'.format(dt.now().strftime("%Y-%m-%d %H:%M:%S"), logged_action, path))
            print('func(path)', func.__name__, path)
            return func(path)
        return the_real_wrapper
    return wrapper_with_log_to_known_file




@wrapper_log_file('FILE_CREATE',r'c:/temp/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")

@wrapper_log_file('FILE_DELETE',r'c:/temp/file_delete.txt')
def delete_file(path):
    print('Deleting log file {}'.format(path))
    os.remove(path)

create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
