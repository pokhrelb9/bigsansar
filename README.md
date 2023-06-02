## New update
* added thumbnails model field in blog system
* added sitmap system 
* added font awesome packages
* addedd javascripts system for per domains
* added custom css system per domains sites 

 
# How to get Bigsansar

Bigsansar is available open-source under the [MIT](https://en.wikipedia.org/wiki/MIT_License) license. We recommend using the latest version of Python 3.
Bigsansar is Fully based on django.
You can use
[bigsansar](https://bigsansar.com)
for install packaged.

view our tutorials in
[youtube](https://youtube.com/bigsansar)

for playlist:
[bigsansar for django](https://www.youtube.com/playlist?list=PLqdXqRSrD-LC6i7YQAaqB57FaCfWEZkth)

# Get the latest development version
The latest and greatest Bigsasnar version is the one that’s in our Git repository (our revision-control system).
This is only for experienced users who want to try incoming changes and help identify bugs before an official release.
Get it using this shell command, which requires [Git](https://git-scm.com/):

`git clone https://github.com/pokhrelb9/bigsansar.git`

You can also download a [gzipped tarball](https://pypi.org/project/Bigsansar/#files) of the development version.
This archive is updated every time we commit code.

# After you install bigsansar
Type `bigsansar init` command for **automatically** setup server .

# How to access admin pannel in local env
Go to [localhost:8000](http://localhost:8000) 

# How to change admin URL in server side with domain 
go to **VirtualHost.py** file and change **localhost:8000** with your subdomain 
## Some usefull commands:

`python3 manage.py createuser` - get unlimited users.

## templatetags for extends and include 

{% extends '<domain_name>/<page_slug>.html' %}
{% include '<domain_name>/<page_slug>.html' %}



## load blog list in templates

`{% load blogs %}
{% get_blog as bloglist %}
          {% for list in bloglist %}
          <div class="card my-4">
                <h5 class="card-header">{{list.title}} - {{ list.domain }}</h5>
            <div class="card-body">
                <p class="card-text"> {{list.body|slice:":100"}} - {{ list.publish_date }}</p>
                <a href="/blog/{{list.slug}}"
                   class="btn btn-danger">Read More</a>
            </div>
          </div>
          {% endfor %}`


## get single blog objects

`{% load blogs %}
{% get_blog_object as get_blog %}
{{ get_blog.title }}
{{ get_blog.thumbnails }}
{{ get_blog.publish_date }}
{{ get_blog.domain }}
{{ get_blog.id }}
{{ get_blog.slug }}
{{ get_blog.body | safe }}
{{ get_blog.visitor }}
`

## How many people views blog 
`{% load blogs %}
{% update_blog_visitor %}`

# get path slug 
{{ slug }}

## Load page list in templates

`{% load pages %}

{% get_pages  as listpage %}
{% for page in listpage %}
<div>
    < a href="{{ page.slug }}">{{ page.title }}</a>
</div>
{% endfor %}`


#### More variable for **page** list
* page.id
* page.domain
* page.title
* page.slug
* page.body
* page.visitor
* page.publish_date


## for single page title
* getpage.id
* getpage.domain
* getpage.title
* getpage.slug
* getpage.body
* getpage.visitor
* getpage.publish_date


## how to access domain system

* gethost.id
* gethost.user
* gethost.domain
* gethost.Description
* gethost.publish_date
* gethost.visitor
