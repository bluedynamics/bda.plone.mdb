from setuptools import setup, find_packages
import sys, os

version = "1.0"
shortdesc ="cone.app.mdb connector for Plone"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read() 
longdesc += open(os.path.join(os.path.dirname(__file__), 'docs', 'CHANGELOG.txt')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'docs', 'LICENSE.txt')).read()

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
      ],
      extras_require={
          'test': [
              'interlude',              
          ],
          'file': [
              'archetypes.schemaextender',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """      
)
