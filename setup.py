from distutils.core import setup

setup(
    # Application name:
    name="redis-email",
    # Version number (initial):
    version="0.1.0",
    # Application author details:
    author="name surname",
    author_email="maria.prudyvus@gmail.com",
    # Include additional files into the package
    include_package_data=True,
    # Details
    url="http://pypi.python.org/pypi/MyApplication_v010/",
    #
    # license="LICENSE.txt",
    description="Python redis emailer",
    long_description=open("README.md").read(),
    py_modules=['common', 'config'],
    i=True,
    # Dependent packages (distributions)
    install_requires=[
        "rq", "python-dotenv"
    ],
    python_requires=">=3.7"
)
