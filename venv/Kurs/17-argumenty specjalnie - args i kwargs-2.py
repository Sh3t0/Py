import os
#"""
def log_it(*args):

    path = r'c:\temp\log.txt'
    with open(path, "a") as f:

        for line in args:
            f.write(line)
            f.write(' ')

        f.write("\n")


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')

"""
def log_it(*args):
    #args += str(' ')
    with open(r"c:\temp\log.txt", 'a') as log_file:
        content = log_file.write(str(args))
        content = log_file.write(' ')
        content = log_file.write('\n')

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
#"""
