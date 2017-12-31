from setuptools import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(name='lenny',
      version='0.1.3',
      description='Generate random lenny faces.',
      long_description=readme,
      url='https://github.com/davidsluo/lenny',
      author='davidsluo',
      author_email='email@davidsluo.me',
      license='MIT',
      packages=['lenny'],
      zip_safe=True,
      keywords=['lenny', 'face']
      )
