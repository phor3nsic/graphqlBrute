from setuptools import setup, find_packages

setup(
    name='graphqlBrute',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "requests"
    ],  # requirements.txt
    entry_points={
        'console_scripts': [
            'graphqlBrute=graphqlBrute.main:main',
        ],
    },
    author='Walleson Rodrigues',
    author_email='phorensic@pm.me',
    description='Description of graphqlBrute.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/phor3nsic/graphqlBrute',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
