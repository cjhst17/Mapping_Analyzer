from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mapping-analyzer",
    version="1.0.0",
    author="United States Steel",
    description="X12 EDI Mapping Analyzer - Analyze and generate X12 map code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dev.azure.com/your-org/Mapping_Analyzer",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Proprietary",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.11",
    install_requires=[
        "pyyaml>=6.0",
        "jsonschema>=4.0",
        "lxml>=4.9",
        "requests>=2.28",
        "python-dateutil>=2.8",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4",
            "pytest-cov>=4.1",
            "pylint>=2.17",
            "black>=23.7",
            "mypy>=1.4",
        ],
    },
    entry_points={
        "console_scripts": [
            "mapping-analyzer=src.cli:main",
        ],
    },
)
