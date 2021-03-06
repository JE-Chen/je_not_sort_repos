import setuptools

with open("README.md", "r") as README:
    long_description = README.read()

setuptools.setup(
    name="je_log_system",
    version="0.0.0.0.5",
    author="JE-Chen",
    author_email="zenmailman@gmail.com",
    description="simple log system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JE-Chen/Python_Log_System_JE",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Traditional)",
    ]
)

# python setup.py sdist bdist_wheel
# python -m twine upload dist/*
