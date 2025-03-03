from setuptools import setup, find_packages

setup(
    name='django-xapi-client',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
        'tincan>=0.0.5',
        'requests',
        'pyexcel'
    ],
    license='MIT',
    description='A Django client for xAPI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/simaoj/django-xapi-client',
    author='Giovanni Toffoli',
    author_email='gtoffoli@example.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)