from setuptools import setup, find_packages

setup(name='jodel_api',
      version='1.0',
      description='Unoffical Python Interface to the Jodel API Edit',
      url='https://github.com/nborrmann/jodel_api',
      author='Nils Borrmann',
      author_email='n.borrmann@googlemail.com',
      license='MIT',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers'
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='jodel',
      install_requires=['requests'],
      package_dir={'': 'src'},
      py_modules=['jodel_api'],
      setup_requires=['pytest-runner', ],
      tests_require=['pytest', ],
      zip_safe=False)