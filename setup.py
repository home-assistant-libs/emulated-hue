"""Set up file for emulatedhue package."""
from pathlib import Path

from setuptools import find_packages, setup

PROJECT_DIR = Path(__file__).parent.resolve()
README_FILE = PROJECT_DIR / "README.md"
LONG_DESCRIPTION = README_FILE.read_text(encoding="utf-8")
VERSION = (PROJECT_DIR / "emulatedhue" / "VERSION").read_text().strip()
GITHUB_URL = "https://github.com/home-assistant-libs/emulated-hue"
DOWNLOAD_URL = f"{GITHUB_URL}/archive/master.zip"


setup(
    name="emulatedhue",
    version=VERSION,
    description="Provide a package for emulatedhue",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="The Home Assistant Authors",
    author_email="hello@home-assistant.io",
    url=GITHUB_URL,
    download_url=DOWNLOAD_URL,
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    python_requires=">=3.7",
    install_requires=[],
    include_package_data=True,
    license="Apache-2.0",
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "'Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
