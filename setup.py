import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bigsansar",
    version="0.0.4",
    author="Bikash Pokhrel",
    author_email="admin@bigsansar.com",
    description="Build one in minutes with bigsansar - a visual site building tool!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://youtube.com/bigsansar",
    project_urls={
        "Bug Tracker": "https://github.com/pokhrelb9/pokhrelb9/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=['django'],
    keywords=['python', 'django host', 'bigsansar', 'django', 'django sites framework', 'django flatpages']
)