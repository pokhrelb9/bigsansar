
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

# For manually setup

### After you get it

go to `www` path and open `settings.py` file then add `bigsansar.apps.BigsansarConfig`  in to 
`INSTALLED_APPS = []` .

### For Virtualhost middleware
go to `www` path and open `settings.py` file then add `bigsansar.core.host.VirtualHostMiddleware`  in to top of 
`MIDDLEWARE = []` .

## Some usefull commands:

`python3 manage.py createuser` - get unlimited users.