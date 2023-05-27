
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


## Some usefull commands:

`python3 manage.py createuser` - get unlimited users.

## bug fixed 
fixed templated tags
now use extends tags
{% extends '<domain_name>/<page_slug>.html' %}


## New update
* added sitmap system 
* added font awesome packages
* addedd javascripts system for per domains
* added custom css system per domains sites 
* added youtube and codesnippet plugin in to blog post site 

## load blog list in templates

`{% load blogs %}
{% get_blog as bloglist %}
          {% for list in bloglist %}
          <div class="card my-4">
                <h5 class="card-header">{{list.title}} </h5>
            <div class="card-body">
                <p class="card-text"> {{list.body|slice:":100"}} </p>
                <a href="/blog/{{list.slug}}"
                   class="btn btn-danger">Read More</a>
            </div>
          </div>
          {% endfor %}`


## get single blog objects

`{% load blogs %}
{% get_blog_object as get_blog %}
{{ get_blog.title }}
{{ get_blog.body | safe }}
`

# get path slug 
{{ slug }}

#### More variable for **blog** list
* blog.id
* blog.domain
* blog.title
* blog.slug
* blog.body
* blog.visitor
* blog.publish_date



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
