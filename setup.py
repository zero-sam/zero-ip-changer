from setuptools import setup, find_packages

setup(
    name='ZeroIpChanger',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ZeroIpChanger = ZeroIpChanger.cli:menu',
        ],
    },
    install_requires=[
        'stem==1.8.0',
        'requests==2.31.0',
    ],
)
