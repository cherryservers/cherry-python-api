from setuptools import setup

setup(name='cherry-python',
      version='0.1',
      description='Cherry Servers API client',
      url='https://bitbucket.org/cherryservers/cherry-python-api',
      author='Aarturas Razinskij',
      author_email='arturas.razinskij@cherryservers.com',
      license='LGPL v3',
      packages=['cherry'],
      install_requires='requests',
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'
    ]
)