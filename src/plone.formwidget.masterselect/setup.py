from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='plone.formwidget.masterselect',
      version=version,
      description="An z3cfrom widget that controls the vocabulary or "
            "display of otheer fields on an edit page",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Jason Mehring',
      author_email='nrgaway@yahoo.com',
      url='http://svn.plone.org/svn/plone/plone.formwidget.masterselect',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.formwidget'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'z3c.form',
        'setuptools',
        'plone.z3cform',
        'simplejson',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
        'test': ['niteoweb.windmill',],
        'selenium': ['plone.app.testing', 'selenium',],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
