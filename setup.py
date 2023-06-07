from setuptools import setup, find_packages

setup(
    name='octollms',
    version='1.0.0',
    author='',
    author_email='',
    description='Python utils for langchain',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'llama_index',
        'pydantic',
        'python-dotenv',
        'Requests',
        'sentence-transformers'
    ],
)
