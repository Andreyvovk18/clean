from setuptools import setup

setup(name='clean',
      version='0.0.1',
      description='Very useful code',
      url='https://github.com/Andreyvovk18/sortuvalka',
      author='Sagun Andrey',
      author_email='Andreyvovk18@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      zip_safe = False,
      entry_points ={'console_scripts': ['clean-folder = clean_folder.clean:main']})