from setuptools import setup,find_packages

setup(name = "project",
      version = "0.0.1",
      author = "seenu",
      author_email = "srinubabu1911@gmail.com",
      packages = find_packages(),
      install_requires = ['pandas','numpy','flask','logging','matplotlib','numpy','seaborn','cufflinks','scipy']
      )