from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='odl-mediawiki-migration',

    description='A script that extracts mediawiki content from a Mediawiki site'
                'and converts them to reStructuredText',
    author='Prateek Chanda',
    author_email='prateekkol21@gmail.com',
    version='1.0.1',

    url='https://github.com/prateekiiest/opendaylight-mediawiki-migration',

    license="EPL 2.0",
    keywords=['text', 'rst', 'mediawiki'],
    scripts=['extractor.py']
)
