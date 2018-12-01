import os
import sys
from setuptools import setup

if sys.version_info < (3, 3):    # Confirmed good through 3.7.0
    print("Sorry, django-markupfield-helpers currently requires Python 3.3+.")
    sys.exit(1)

# From: https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    "Django>=1.11",    # Confirmed good through 2.1.3
    "django-markupfield>=1.3.5",    # Confirmed good through 1.5.0
    "docutils>=0.12",    # Confirmed good through 0.14
    "markdown2>=2.3.0",    # Confirmed good through 2.3.6
]

setup(
    name='django-markupfield-helpers',
    version='0.0.0',
    packages=['markupfield_helpers'],
    include_package_data=True,
    license='BSD License',
    keywords='markup markdown',
    description='Django helpers to make it easier to work with django-markupfield',
    long_description=(read('README.rst') + '\n\n' +
                      read('CHANGELOG.rst')),
    url='https://github.com/mfcovington/django-markupfield-helpers',
    author='Michael F. Covington',
    author_email='mfcovington@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Documentation',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
)