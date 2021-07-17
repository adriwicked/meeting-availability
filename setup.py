import setuptools

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name="meeting-availability",
    version="0.0.1",
    author="Adrián Moreno",
    author_email="adrianmn90@gmail.com",
    description="A module that allows you to know available time blocks for two people to meet.",
    license=license,
    long_description=readme,
    url="https://github.com/adriwicked/meeting-availability",
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
)
