from setuptools import setup

setup(
    name='storyblok_richtext',
    version='0.2.0',
    description='Storyblok Python library for Richtext component',
    author='Emanuel Souza',
    author_email='eg@storyblok.com',
    url='https://github.com/storyblok/storyblok-python-richtext-renderer',
    download_url = 'https://github.com/storyblok/storyblok-python-richtext-renderer/archive/0.2.0.tar.gz',
    license='MIT',
    install_requires=[],
    packages=[
        'storyblok_richtext'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)