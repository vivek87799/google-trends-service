from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.14'
DESCRIPTION = 'Google Trends API Service'
LONG_DESCRIPTION = 'A simple service that uses pytrends to fetch the data from google trends using pytrends api and push it onto a Kafka topic'

# Setting up
setup(
    name="trendsingest",
    version=VERSION,
    author="Nullfinders (Vivek Loganathan)",
    author_email="<vivek87799@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pytrends', 'kafka-python'],
    keywords=['python', 'googel trends'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Linux :: Ubuntu 22.04",
        "Operating System :: Microsoft :: Windows",
    ]
)

