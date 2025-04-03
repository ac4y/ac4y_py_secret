from setuptools import setup, find_packages

setup(
    name="ac4y_py_secret",
    version="0.1",
    packages=find_packages(),
    description="Egyszerű titkosítási csomag",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Réka",
    author_email="reka@example.com",
    url="https://github.com/ac4y/ac4y_py_secret",  # GitHub link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
