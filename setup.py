from setuptools import setup

setup(
    name='cursopython',

    packages=['cursopython'],

    install_requires=[
        'flask',
        'gunicorn',
    ],

    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
