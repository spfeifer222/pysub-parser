from setuptools import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='pysub-parser',
  version='2.0.1',
  url='https://github.com/spfeifer222/pysub-parser',
  license='MIT',

  description='Utility to extract the contents of a subtitle file',
  long_description=long_description,
  long_description_content_type='text/markdown',

  author='Sebastian Pfeifer',
  author_email='pfeifer_s@web.de',

  packages=['pysubparser', 'pysubparser.classes', 'pysubparser.parsers', 'pysubparser.writers', 'pysubparser.cleaners'],
  install_requires=['unidecode'],
  test_requires=['coverage', 'parameterized'],

  keywords=['subtitle', 'subtitles', 'parser', 'srt', 'sub', 'ssa', 'txt'],
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)
