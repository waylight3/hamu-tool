from setuptools import setup, find_packages

setup(
    name='hamu-tool',
    version='0.0.20',
    description='Many useful tools for computer scientists!',
    license='MIT',
    author='DoHyeon Lee',
    author_email='waylight3@snu.ac.kr',
    url='https://github.com/waylight3/hamu-tool',
    keywords=['hamu', 'tool', 'computer', 'science', 'useful', 'toolkit', 'library', 'python', 'package', 'module', 'utility', 'function', 'class', 'method'],
    install_requires=['pymupdf'],
    python_requires='>=3.11',
    packages=find_packages(),
    zip_safe=False
)
