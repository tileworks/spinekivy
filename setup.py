from setuptools import setup

import spinekivy


setup(
    name='spinekivy',
    version=spinekivy.__version__,
    author='Tileworks Games and other contributors',
    author_email='tileworksgames@gmail.com',
    description='Spine skeleton renderer for Kivy framework.',
    long_description=spinekivy.__doc__,
    license='MIT',
    packages=['spinekivy'],
    package_dir={
        'spinekivy': 'spinekivy'
    },
    install_requires=[
        'kivy>=1.8.0',
        'spine-cython>=0.5.0'
    ],
    keywords='spine kivy',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia :: Graphics',
    ]
)
