from setuptools import setup
import os
import adminlte_full


version = adminlte_full.__version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='django-adminlte-full',
    version=version,
    packages=['adminlte_full'],
    include_package_data=True,
    license='Apache License 2.0',
    description='This Django application is port the AdminLTE Template for easy integration into Django Framework',
    long_description=README,
    url='https://github.com/kyzima-spb/django-adminlte-full',
    author='Kirill Vercetti',
    author_email='office@kyzima-spb.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)