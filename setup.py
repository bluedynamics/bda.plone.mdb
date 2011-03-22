from setuptools import setup, find_packages
import sys, os

version = "1.0"
shortdesc ="cone.app.mdb connector for Plone"
currentdir = os.path.dirname(__file__)
longdesc = open(os.path.join(currentdir, 'README.rst')).read() 
longdesc += open(os.path.join(currentdir, 'CHANGELOG.rst')).read()
longdesc += open(os.path.join(currentdir, 'LICENSE.rst')).read()
tests_require = ['interlude',]

setup(name='bda.plone.mdb',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Framework :: Zope2',
            'Framework :: Plone',
            'Topic :: Software Development :: Libraries :: Python Modules'        
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='media database integration plone cone pyramid',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url='https://github.com/bluedynamics/bda.plone.mdb',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bda', 'bda.plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'restkit',
      ],
      tests_require=tests_require,
      test_suite="bda.plone.mdb.tests.test_suite",
      extras_require = {
          'test': tests_require,
          'contenttype': [
              'archetypes.schemaextender',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """      
)

