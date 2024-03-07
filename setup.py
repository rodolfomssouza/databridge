from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="databridge",
    version="0.2.6",
    description="Bridge shared datasets across diverse projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "geopandas",
        "polars",
        "prettytable",
    ],
    author="Rodolfo Souza",
    author_email="souzarod@proton.me",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": ["pytest", "twine"],
    },
    python_requires=">=3.10",
)
