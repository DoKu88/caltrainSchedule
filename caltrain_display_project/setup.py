from setuptools import setup, find_packages

setup(
    name="caltrain_display_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'lxml',
    ],
) 