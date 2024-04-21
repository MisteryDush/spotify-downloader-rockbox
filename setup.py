from setuptools import setup, find_packages

setup(
    name="spotdl_rockbox",
    version="0.1",
    packages=find_packages(),
    description="Fix of spotdl for rockbox",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="MisteryDush",
    author_email="ikrom.arifdjanov@gmail.com",
    license="MIT",
    install_requires=[
        # dependencies listed here, e.g., "requests >= 2.23.0"
    ],
    url="http://url_to_your_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
