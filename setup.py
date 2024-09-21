from setuptools import setup, find_packages

setup(
    name='htpapers',
    version='0.1.0',
    description='',
    author='James Peaker',
    author_email='jpeaker97@gmail.com',
    packages=find_packages(where="src"), 
    package_dir={"": "src"}, 
    python_requires='>=3.8'
)