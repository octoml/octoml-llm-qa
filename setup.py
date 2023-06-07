from setuptools import setup, find_packages

setup(
    name='octo-llms',
    packages=['octo_llms'],
    version='1.0.0',
    author='',
    author_email='',
    description='Python utils for langchain',
    install_requires=[
        'langchain',
        'llama_index',
        'pydantic',
        'python-dotenv',
        'Requests',
        'sentence-transformers'
    ],
)
