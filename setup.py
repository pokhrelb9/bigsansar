import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bigsansar",
    version="2.4.3",
    author="Bikash Pokhrel",
    author_email="bigsansaroffice@gmail.com",
    description="Build one in minutes with bigsansar - a visual site building tool!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bigsansar.com",
    project_urls={
        "Bug Tracker": "https://github.com/pokhrelb9/bigsansar/issues",
        "Documentations": "https://docs.bigsansar.com/"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux", 
        "Operating System :: OS Independent",
    ],

    packages=setuptools.find_packages(exclude=("www",
                                               "static",
                                               "ssl",
                                               "apache2"
                                               )),
    #packages=['bigsansar'],
    package_data={'': ['etc/*',
                       'templates/*',
                       'templates/*/*',
                                'static/*',
                                'static/ckeditor/ckeditor/plugins/youtube/*',
                                'static/ckeditor/ckeditor/plugins/youtube/*/*']},
                  
    include_package_data= True,

    entry_points={
        'console_scripts': [
                    'bigsansar = bigsansar.core:main',
                ],
    },

    python_requires=">=3.6",
    install_requires=['django', 'django-phonenumber-field[phonenumberslite]', 'django-ckeditor', 'requests', 'pillow', 'fontawesomefree'],
    keywords=['python', 'django host', 'bigsansar', 'django', 'django sites framework', 'django flatpages']
)
