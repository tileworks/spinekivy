from setuptools import setup


setup(
    name='spinekivy',
    version='0.1.2-dev0',
    author='Tileworks Games and other contributors',
    author_email='tileworksgames@gmail.com',
    description='Spine skeleton renderer for Kivy framework.',
    license='MIT',
    packages=['spinekivy'],
    package_dir={
        'spinekivy': 'spinekivy'
    },
    install_requires=[
        'kivy>=1.8.0',
        'spine-cython>=0.5.0'
    ],
    keywords=['spine', 'kivy'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia :: Graphics'
    ]
)
