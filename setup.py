from setuptools import setup

long_description = '''
UltiPro SOAP Python is a Python client that wraps the UltiPro SOAP API.
'''

def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='ultipro',
    version='0.0.4',
    url='https://github.com/call/ultipro-soap-python',
    author_email=['bizappdev@puppet.com', 'jonathan.revah@equinox.com'],
    packages=['ultipro', 'ultipro.services'],
    license='Apache License 2.0',
    install_requires=read_requirements(),
    keywords=['UltiPro', 'SOAP API', 'Wrapper', 'Client'],
    description='Python Client for the UltiPro SOAP API',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'ultipro=ultipro.cli:cli',
        ],
    },
)
