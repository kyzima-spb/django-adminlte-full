import os

from setuptools import setup, find_packages


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


readme = read_file('README.rst')
changelog = read_file('CHANGELOG.rst')


setup(
    name='django-adminlte-full',
    use_scm_version={
        'relative_to': __file__,
    },
    url='https://github.com/kyzima-spb/django-adminlte-full',
    description='This Django application is port the AdminLTE Template for easy integration into Django Framework',
    long_description=readme + '\n\n' + changelog,
    long_description_content_type='text/x-rst',
    author='Kirill Vercetti',
    author_email='office@kyzima-spb.com',
    license='Apache License 2.0',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'django>=3.0',
        'django-bootstrap4>=1.0'
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
