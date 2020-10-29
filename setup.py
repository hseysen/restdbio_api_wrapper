from setuptools import setup


def readme():
    with open("README.md", "r") as f:
        return f.read()

setup(
    name="restdbio_api_wrapper",
    version="0.0.1",
    long_description=readme(),
    long_description_content_type="text/markdown",
    description=("An API Wrapper written for restdb.io which helps host online databases."),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],  
    license="GPLv3",
    keywords="api wrapper restdbio online database",
    url="http://github.com/hseysen/restdbio_api_wrapper",
    author="Hasan Isgandarli",
    author_email="hesenisgenderli999@gmail.com",
    packages=["restdbio_api_wrapper"],
    install_requires=["requests"]
)