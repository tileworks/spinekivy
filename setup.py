from distutils.core import setup

import spinekivy


packages = [
    'spinekivy'
]

package_dir = {
    'spinekivy': 'spinekivy'
}


setup(
    name='spinekivy',
    version=spinekivy.__version__,
    author='Tileworks Games',
    author_email='tileworksgames@gmail.com',
    description='Spine renderer for kivy.',
    long_description=spinekivy.__doc__,
    license='MIT',
    packages=packages,
    package_dir=package_dir
)
