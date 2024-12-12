from setuptools import setup, find_packages

setup(
    name="betrand_ngoh_mutagha_version_10",  # Updated to reflect your project name
    version="0.2.10",  # Valid version string as per PEP 440
    author="BETRAND MUTAGHA",
    author_email="mutagha2@gmail.com",
    url="https://github.com/Betrand1999/cicd",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
