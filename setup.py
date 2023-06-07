from setuptools import setup, find_packages

setup(
    name='octo_llm',
    version='1.0.0',
    author='',
    author_email='',
    description='Python utils for langchain',
    packages=['octo_llm'],
    install_requires=[
        'langchain',
        'llama_index',
        'pydantic',
        'python-dotenv',
        'Requests',
        'sentence-transformers'
    ],
)
