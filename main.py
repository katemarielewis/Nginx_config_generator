__author__ = 'kate'

def check_port(port):
    if port.isdigit():
        print("You entered", port)
    elif port=="help":
        print("This is a help message")
        port=input("Please enter an integer for the port: ")
        check_port(port)
    elif port=="exit":
        pass
    else:
        port=input("Please enter an integer for the port: ")
        check_port(port)
    return port


import os
def check_root_directory(root_directory):
    if os.path.isdir(root_directory):
        print("You entered the directory", root_directory)
    elif root_directory=="help":
        print("This is a help message")
        root_directory=input("Please enter a valid directory for the root directory of the site: ")
        check_root_directory(root_directory)
    elif root_directory=="exit":
        pass
    else:
        root_directory=input("Please enter a valid directory for the root directory of the site: ")
        check_root_directory(root_directory)
    return root_directory


extensions=[".com",".com.au",".net",".gov"]

def check_extensions(site_url):
    valid_extension=False
    for x in extensions:
        if x==(site_url[-(len(x))::]):
            valid_extension=True
            break
    if valid_extension==True:
        print("You entered the site URL", site_url)
    elif site_url=="help":
        print("This is a help message")
        site_url=input("Please enter a valid URL for the site to be displayed on: ")
        check_extensions(site_url)
    elif site_url=="exit":
        pass
    else:
        site_url=input("Please enter a valid URL for the site to be displayed on: ")
        check_extensions(site_url)
    return site_url

def check_php_fpm(php_fpm):
    configured_tcp_unix=""
    if php_fpm=="Y":
       configured_tcp_unix=input("is it configured to use tcp port or unix socket? Please answer using tcp/unix ")
       configured_tcp_unix=check_configured_tcp_unix(configured_tcp_unix)
    elif php_fpm=="help":
        print("This is a help message")
        input_php_fpm=input("please use Y/N to answer: ")
        check_php_fpm(input_php_fpm)
    elif php_fpm=="exit":
        pass
    elif php_fpm=="N":
        print("you entered: N")
    else:
        input_php_fpm=input("please use Y/N to answer: ")
        check_php_fpm(input_php_fpm)
    return php_fpm, configured_tcp_unix

def check_configured_tcp_unix(configured_tcp_unix):
    if configured_tcp_unix=="tcp":
        configured_tcp_unix="127.0.0.1:9000"
    elif configured_tcp_unix=="help":
        print("This is a help message")
        configured_tcp_unix=input("please use tcp/unix to answer: ")
        configured_tcp_unix=check_configured_tcp_unix(configured_tcp_unix)
    elif configured_tcp_unix=="exit":
        pass
    elif configured_tcp_unix=="unix":
        configured_tcp_unix="/var/run/php-fpm.sock"
    else:
        configured_tcp_unix=input("please use tcp/unix to answer: ")
        configured_tcp_unix=check_configured_tcp_unix(configured_tcp_unix)
    return configured_tcp_unix


def check_php_files(php_files):
    php_fpm=""
    configured_tcp_unix=""
    if php_files=="Y":
        php_fpm=input("will the site use php-fpm? Please answer using Y/N ")
        php_fpm, configured_tcp_unix=check_php_fpm(php_fpm)
    elif php_files=="help":
        print("This is a help message")
        php_files=input("Please answer using Y/N: ")
        check_php_files(php_files)
    elif php_files=="exit":
        pass
    elif php_files=="N":
        print("you entered: N")
    else:
        php_files=input("Please answer using Y/N: ")
        check_php_files(php_files)
    return php_files, php_fpm, configured_tcp_unix


def run_script():
    port=input("What port would you like to listen on? ")
    port=check_port(port)
    root_directory=input("What is the root directory of the site? ")
    root_directory=check_root_directory(root_directory)
    site_url=input("What URL should the site be displayed on? ")
    site_url=check_extensions(site_url)
    php_files=input("Will the site serve php files? Please answer using Y/N ")
    php_files, php_fpm, configured_tcp_unix=check_php_files(php_files)
    print("server {")
    print("\tlisten "+port+";")
    print("\tserver_name "+ site_url+";")
    print("\troot "+ root_directory+";")
    print("\n")
    print("\tautoindex on;")
    if php_files=="Y":
        print("\tindex index.php;")
        print("\n")
        print("\tlocation / {")
        print("\n")
        print("\t\ttry_files $uri $uri/ /index.php;")
        print("\n")
        print("\t\tlocation = /index.php {")
        print("\t\t\tfastcgi_pass\t"+ configured_tcp_unix+";")
        print("\t\t\tfastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;")
        print("\t\t\tinclude\t\tfastcgi_params;")
        print("\t\t}")
        print("\t}")
        print("\n")
        print("\tlocation ~ \.php$ {")
        print("\t\treturn 444;")
        print("\t}")
    else:
        print("\tindex index.html;")
    print("}")


run_script()


