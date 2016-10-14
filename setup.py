from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

version = open('packaging/VERSION').read().strip()
requirements = open('packaging/requirements.txt').read().split("\n")
test_requirements = open('packaging/requirements-test.txt').read().split("\n")

setup(
    name='bgpq3d',
    version=version,
    author='Workonline Communications',
    author_email='communications@workonkonline.co.za',
    description='A python daemon for prefix filter list management operations based on bgpq3',
    long_description=readme(),
    license='LICENSE',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    ],
    packages=find_packages(
        include=[
            'bgpq3d',
            'bgpq3d.*'
        ],
        exclude=[]
    ),
    entry_points={
    },
    include_package_data=True,

    url='https://github.com/wolcomm/bgpq3d',
    download_url='https://github.com/wolcomm/bgpq3d/%s' % version,

    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='nose.collector'
)
