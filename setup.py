from distutils.core import setup
setup(
  name = 'missingno',
  packages = ['missingno'], # this must be the same as the name above
  install_requires=['numpy', 'matplotlib'],
  version = '0.1.0',
  description = 'Missing data visualization module for Python.',
  author = 'Aleksey Bilogur',
  author_email = 'aleksey.bilogur@gmail.com',
  url = 'https://github.com/ResidentMario/missingno',
  download_url = 'https://github.com/ResidentMario/missingno/tarball/0.1.0',
  keywords = ['data', 'data visualization', 'data analysis', 'missing data', 'data science', 'pandas', 'python',
              'jupyter'],
  classifiers = [],
)