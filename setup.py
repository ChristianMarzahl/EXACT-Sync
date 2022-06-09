import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EXCAT-Sync", 
    version="0.0.34",
    author="Christian Marzahl",
    author_email="christian.marzahl@gamil.com",
    description="A package to download images and annotations from the EXACT Server https://github.com/ChristianMarzahl/Exact",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChristianMarzahl/EXACT-Sync",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests', 
        'tqdm', 
        'requests-toolbelt',
        'pillow',
        "locust==1.1.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


#python -m build
#python -m twine upload dist/*