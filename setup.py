from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-pacemaker",
    version="0.1.0",
    description="A starter template for modern development techniques with Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/destacks/django-pacemaker",
    author="Alexis Michaltsis",
    author_email="am@destacks.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="django starter template",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.6",
)
