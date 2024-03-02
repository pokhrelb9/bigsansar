## New update
* customize admin pannel with side bar nav and add some function 
* now you can install bigsansar package in to ubuntu and all setup with on command lines 
* bigsansar init no longer support in future 


 
# How to get Bigsansar

Bigsansar is available open-source under the [MIT](https://en.wikipedia.org/wiki/MIT_License) license. We recommend using the latest version of Python 3.
Bigsansar is Fully based on django and linux ubuntu.  You can use [bigsansar](https://bigsansar.com) for install packaged.
You can use
[bigsansar](https://bigsansar.com)
for install packaged.

view our tutorials in
[youtube](https://youtube.com/bigsansar)

for playlist:
[bigsansar for django](https://www.youtube.com/playlist?list=PLqdXqRSrD-LC6i7YQAaqB57FaCfWEZkth)




# Get the latest development version



The latest and greatest Bigsasnar version is the one that’s in our Git repository (our revision-control system). This is only for experienced users who want to try incoming changes and help identify bugs before an official release. Get it using this shell command, which requires [Git](https://https://git-scm.com/):

`git clone https://github.com/pokhrelb9/bigsansar.git`

You can also download a [gzipped tarball](https://https://pypi.org/project/Bigsansar/#files) of the development version. This archive is updated every time we commit code.


# After you install bigsansar
1) Type `bigsansar init` command for **automatically** setup server for internal configurations.

** this command valid into vertualenv for developer 

# for full setup in to server 

this is work only on ubuntu os 

2) type ` python manage.py setup_server` commend for fully setup into server .

[How to Setup a Full Server with BigSansar, Django, and Ubuntu
](https://youtu.be/iEmI0HO_U0E)

# some usefull link 
[sitemap.xml](http://localhost/sitemap.xml)
[script.js](http://localhost/script.js)
[styles.css](http://localhost/styles.css)

# how to edit sitemap , js and css from pages

create a page **slug** name with sitemap,script , styles


# How to change admin URL in server side with domain 
go to **VirtualHost.py** file and change **localhost** with your subdomain 
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

## Count visitor in your blogs
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


## How to access codesnippet in to bigsansar pages

**add this script in to html head **

{% load static %}
<script type="text/javascript" src="{% static 'ckeditor/ckeditor-init.js' %}"></script>
<script type="text/javascript" src="{% static  'ckeditor/ckeditor/ckeditor.js' %}"></script>
<link rel="stylesheet" href="{% static 'ckeditor/ckeditor/plugins/codesnippet/lib/highlight/styles/default.css' %}"/>
<script src="{% static 'ckeditor/ckeditor/plugins/codesnippet/lib/highlight/highlight.pack.js' %}"></script>
<script>hljs.initHighlightingOnLoad();</script>