from setuptools import setup

setup(name='autodeskvault',
      version='0.1',
      description='Autodesk Vault web-services Python wrapper',
      keywords='autodesk vault web-services wrapper',
      url='https://github.com/a-severin/autodeskvault',
      author='Anatoliy Severin',
      author_email='severin.a.u@gmail.com',
      license='MIT',
      packages=['autodeskvault'],
      install_requires=[
            'zeep'
      ],
      zip_safe=False)
