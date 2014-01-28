import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'beautifulsoup4',
    'gunicorn',
    'Mako==0.9.1',
    'MySQL-python==1.2.5',
    'PyHAML==1.0.1',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid-webassets==0.7.1',
    'pyscss==1.2.0.post3',
    'python-dateutil==2.2',
    'requests==2.2.1',
    'SQLAlchemy==0.9.1',
    'transaction',
    'zope.sqlalchemy',
    'zope.interface==4.0.5',
    'waitress',
    'WebHelpers==1.3',
    'wtforms==1.0.5',
    ]

setup(name='dexter',
      version='0.0',
      description='dexter',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='dexter',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = dexter:main
      [console_scripts]
      initialize_dexter_db = dexter.scripts.initializedb:main
      """,
      )
