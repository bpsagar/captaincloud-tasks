from setuptools import find_packages, setup

setup(
    name='captaincloud-tasks',
    version='1.0.0-alpha',
    description='',
    url='https://github.com/bpsagar/captaincloud-tasks',
    author='Sagar Chakravarthy',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'captaincloud',
        'six'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    zip_safe=False)
