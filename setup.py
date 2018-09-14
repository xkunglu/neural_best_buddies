""" setup file for nbb module Neural Best Buddies

    Kfir Aberman, Jing Liao, Mingyi Shi, Dani Lischinski, Baoquan Chen, Daniel Cohen-Or.
    "Neural Best-Buddies: Sparse Cross-Domain Correspondence"
    ACM Transactions on Graphics, Vol. 37, No. 4, Article 69. Publication date: August 2018
    https://dl.acm.org/citation.cfm?doid=3197517.3201332

"""
import sys
from setuptools import setup, find_packages

print (sys.version_info[:2])

def readme():
    with open('README.md', 'r') as fi:
        print(fi.read())

def setup_package():
    ''' setup '''

    metadata = dict(
        name='nbb',
        version='0.0.1',
        description='semantic descriptors',
        url='https://github.com/xkunglu/neural_best_buddies',
        license='need to inquire with auhors',
        install_requires=[],#'numpy', 'opencv', 'torchvision', 'sklearn'],
        packages=find_packages(),
        long_description=readme(),
        zip_safe=False)

    setup(**metadata)

if __name__ == '__main__':
    setup_package()