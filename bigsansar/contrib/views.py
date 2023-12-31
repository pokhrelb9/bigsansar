
from bigsansar.contrib.cgi_base import read_template


def index_page():
    return read_template('templates/admin/login.html')


def about_page():
    return "<h1>About Us</h1><p>This is the About Us page.</p>"

def contact_page():
    return "<h1>Contact Us</h1><p>You can reach us at contact@example.com.</p>"



def not_found_page():
    return read_template('templates/404.html')