
import site
import os

def copy_file_from_pip_lib(source_file):
    # Find the site-packages directory where the package is installed
    site_packages = site.getsitepackages()[0]
    
    # Construct the full path to the installed package directory
    
    package_dir = os.path.join(site_packages, 'bigsansar')
    
    # Construct the full path to the source file in the package directory
    source_path = os.path.join(package_dir, source_file)
    
    # Construct the full path to the destination folder in the home directory
    # destination_path = os.path.expanduser(os.path.join("~", destination_folder))
    return source_path
