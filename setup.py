from setuptools import setup, find_packages
import re

with open("actions_demo/__init__.py", encoding="utf-8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

requirements = [x.strip() for x in open("requirements.txt").readlines()]

setup(
    name="actions-demo",
    version=version,
    author="sshuair",
    author_email="sshuair@gmail.com",
    url="https://github.com/sshuair/github-actions-demo",
    description="github actions for test, build, package, docker...",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="MIT",
    install_requires=requirements,
)
