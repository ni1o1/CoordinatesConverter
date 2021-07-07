import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="CoordinatesConverter",
    version="0.1.0",
    author="Qing Yu",
    author_email="qingyu0815@foxmail.com",
    description="A tool to convert coordinates between WGS84 GCJ02 and BD09",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/ni1o1/CoordinatesConverter",
    project_urls={
        "Bug Tracker": "https://github.com/ni1o1/CoordinatesConverter/issues",
    },
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
