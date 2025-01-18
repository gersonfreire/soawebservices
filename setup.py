from setuptools import setup, find_packages

setup(
    name="soa-webservices-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "click>=8.1.7",
        "pydantic>=2.5.2",
        "rich>=13.7.0",
    ],
    entry_points={
        'console_scripts': [
            'soa-cli=cli:cli',
        ],
    },
)