from setuptools import setup, find_packages

setup(
    name='foo_param',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'foo_param=foo_param.cli:main',
        ],
    },
    install_requires=[
        'tkinter',
    ],
    author='Mitra Azizian',
    author_email='mitra.azizian@example.com',
    description='A package to calculate the volume of a sphere using Foo et al. parameterization.',
    long_description=open('docs/README.md').read(),
    #long_description_content_type='docs/markdown',
    url='https://github.com/mazizian140/foo_param',
)
