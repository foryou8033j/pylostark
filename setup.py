import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylostark",
    version="0.0.1",
    author="Jeongsam",
    author_email="foryou8033j@gmail.com",
    description="Lostark OpenAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/foryou8033j/pylostark",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)