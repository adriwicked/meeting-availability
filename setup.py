import setuptools

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name="meeting_availability",
    version="0.0.3",
    description="A module that allows you to know available time blocks for two people to meet.",
    long_description=readme,
    author="Adrián Moreno",
    author_email="adrianmn90@gmail.com",
    license=license,
    url="https://github.com/adriwicked/meeting-availability",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['meeting_availability'],
)
