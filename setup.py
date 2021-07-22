from setuptools import setup, find_packages

setup(
    name='strigo',
    version='0.0.0',
    author='ops@strigo.io',
    author_email='ops@strigo.io',
    packages=find_packages(include=['strigo', 'strigo.endpoints']),
    license='LICENSE',
    description='A REST Client for Strigo',
    entry_points={'console_scripts': ['siesta = strigo.siesta:request']},
    extras_require={
        'cli': ['click==7.0.0'],
    },
    install_requires=[
        'requests==2.21.0',
        'python-box==3.4.0',
        'requests_toolbelt',
    ]
)
