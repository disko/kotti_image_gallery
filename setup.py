from setuptools import setup, find_packages
import os

version = '0.3.2'

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ""
try:
    TODO = open(os.path.join(here, 'TODO.txt')).read()
except IOError:
    TODO = ""
try:
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    CHANGES = ""

tests_require = ["pytest",
                 "WebTest",
                 "wsgi_intercept",
                 "zope.testbrowser", ]

setup(name='kotti_image_gallery',
      version=version,
      description="Add an image gallery to your Kotti site",
      long_description=README + '\n\n' + TODO + '\n\n' + CHANGES,
      classifiers=["Programming Language :: Python",
                   "Framework :: Pylons",
                   "Topic :: Internet :: WWW/HTTP",
                   "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
                   "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
                   "License :: Repoze Public License", ],
      keywords='image gallery bootstrap kotti cms pylons pyramid',
      author='Andreas Kaiser',
      author_email='disko@binary-punks.com',
      url='https://github.com/disko/kotti_image_gallery',
      license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["Kotti>=0.6.0b1",
                        "PIL",
                        "plone.scale"] + tests_require,
      tests_require=tests_require,
      extras_require={
          'testing': tests_require,
          },
)
