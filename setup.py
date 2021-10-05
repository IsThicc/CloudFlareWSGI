from setuptools import setup, find_packages
from cloudflare_wsgi import __version__, __license__

setup(
    name='CloudFlare WSGI',
    version=__version__,
    license=__license__,
    description="A simple module to find a client's IP address when behind CloudFlare.",
    long_description=open("README.md", "r").read(),
    long_description_content_type='text/markdown',
    url='https://isthicc.dev/',
    author='IsThicc Software',
    packages=find_packages(),
    # install_requires=[]
)
