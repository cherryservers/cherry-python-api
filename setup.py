from setuptools import setup

setup(name='cherry',
      version='0.1',
      description='Cherry Servers API client',
      url='https://bitbucket.org/cherryservers/cherry-python-api',
      author='Aarturas Razinskij',
      author_email='arturas.razinskij@cherryservers.com',
      license='LGPL v3',
      packages=['cherry'],
      install_requires='requests',
      zip_safe=False)