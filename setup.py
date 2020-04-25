from setuptools import setup, find_packages
import os


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


setup(
    name='django-adminlte-full',
    use_scm_version=True,
    url='https://github.com/kyzima-spb/django-adminlte-full',
    description='This Django application is port the AdminLTE Template for easy integration into Django Framework',
    long_description=README,
    author='Kirill Vercetti',
    author_email='office@kyzima-spb.com',
    license='Apache License 2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'setuptools_scm>=3.5',
        'django>=3.0',
        'django-bootstrap3>=7.0'
    ],
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
