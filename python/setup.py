#!/usr/bin/env python3
"""
FurSight SDK - Python Package Setup
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fursight-sdk",
    version="1.0.0",
    author="FurSight.ai",
    author_email="admin@fursight.ai",
    description="Official Python SDK for the FurSight Pet Adoption API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OpenOvation/FurSight-SDK",
    project_urls={
        "Bug Tracker": "https://github.com/OpenOvation/FurSight-SDK/issues",
        # "Documentation": "https://sdk.fursight.ai",
        "API Documentation": "https://api.fursight.ai/docs",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        "pydantic>=2.0.0",
        "typing-extensions>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.900",
        ],
        "async": [
            "aiohttp>=3.8.0",
            "asyncio>=3.4.3",
        ],
    },
    entry_points={
        "console_scripts": [
            "fursight=fursight.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
