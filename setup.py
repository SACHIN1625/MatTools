import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MatTools", 
    version="1.0.2",
    author="Sachin_S",
    author_email="sachinshanmugam07@gmail.com",
    description="A package to simplify Matrix Operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SACHIN1625/MatTools/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
