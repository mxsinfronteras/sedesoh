from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='oaxaca.policy',
      version=version,
      description="Instala el Plone para SEDESOH",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Raul Ross Pineda',
      author_email='mxsinfronteras@gmail.com',
      url='http://sedesoh.info/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['oaxaca'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'oaxaca.newcontent',
      ],
      extras_require={
          'test': ['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
