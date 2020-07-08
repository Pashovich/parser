from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()


setup_args = dict(
    name='dependency-parser',
    version='0.0.1',
    description='Dependency parser',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='USERSTORY',
    author_email='p.sidorov@dev.userstory.ru',
    keywords=['DepParser','parser','dependepcy-parser'],
    url='https://gitlab.userstory.ru/userstory-ml/dependency-parser',
    download_url='https://gitlab.userstory.ru/userstory-ml/dependency-parser'
)

install_requires = [
    'spacy==2.1.9'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires, include_package_data = True)