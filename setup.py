import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jakym",
    version="0.2",
    author="Mayank Jha",
    author_email="jhamayank159@gmail.com",
    description="Just Another Konsole YouTube-Music",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/themayankjha/JAKYM",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'youtube_dl',
          'pyfiglet',
          'requests',
          'pydub',
          'termcolor',
          'beautifulsoup4',
          'lxml',
      ],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['jakym = jakym.__main__:main']
    },
)
