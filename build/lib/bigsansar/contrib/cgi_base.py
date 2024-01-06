
base_template_file = '/usr/local/lib/python3.10/dist-packages/bigsansar/templates/'

def read_template(filename):
    with open(filename, 'r') as file:
        return file.read()

def render(template, **kwargs):
     # Replace placeholders with values
    for key, value in kwargs.items():
        template = template.replace('{{ ' + key + ' }}', str(value))
    return template


base_template = read_template(base_template_file + 'base.html')