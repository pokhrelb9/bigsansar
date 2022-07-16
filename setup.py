import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bigsansar",
    version="0.1.2",
    author="Bikash Pokhrel",
    author_email="bigsansaroffice@gmail.com",
    description="Build one in minutes with bigsansar - a visual site building tool!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bigsansar.com",
    project_urls={
        "Bug Tracker": "https://github.com/pokhrelb9/bigsansar/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=setuptools.find_packages(),
    
     entry_points={
        'console_scripts': [
                    'bigsansar = bigsansar.core:main',
                ],
    },

    python_requires=">=3.6",
    install_requires=['django'],
    keywords=['python', 'django host', 'bigsansar', 'django', 'django sites framework', 'django flatpages']
)
