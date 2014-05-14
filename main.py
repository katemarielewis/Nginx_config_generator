__author__ = 'kate'

def check_port(port):
    if port.isdigit():
        print("You entered", port)
    elif port=="help":
        pass
    elif port=="exit":
        pass
    else:
        port=input("Please enter an integer for the port: ")
        check_port(port)




import os
def check_root_directory(root_directory):
    if os.path.isdir(root_directory):
        print("You entered the directory", root_directory)
    elif root_directory=="help":
        pass
    elif root_directory=="exit":
        pass
    else:
        root_directory=input("Please enter a valid directory for the root directory of the site: ")
        check_root_directory(root_directory)



extensions=[".com",".com.au",".net",".gov"]

def check_extensions(site_url):
    for x in extensions:
        if x==(site_url[-(len(x))::]):
            print("You entered the site URL", site_url)
        elif site_url=="help":
            pass
        elif site_url=="exit":
            pass
        else:
            site_url=input("Please enter a valid URL for the site to be displayed on: ")
            check_extensions(extensions)


def run_script():
    port=input("What port would you like to listen on?")
    check_port(port)
    root_directory=input("What is the root directory of the site?")
    check_root_directory(root_directory)
    site_url=input("What URL should the site be displayed on?")
    check_extensions(site_url)