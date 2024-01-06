from bigsansar.contrib.cgi_base import read_template, base_template_file,base_template,render


def index_page():
   
    template =  read_template(base_template_file + 'admin/login.html')
    content =  render(template, title="Index Page", content="Welcome to the Index Page!")
    return render(base_template, title="My Page", body=content)


def about_page():
    return "<h1>About Us</h1><p>This is the About Us page.</p>"

def contact_page():
    return "<h1>Contact Us</h1><p>You can reach us at contact@example.com.</p>"



def not_found_page():
    return read_template(base_template_file + 'templates/404.html')