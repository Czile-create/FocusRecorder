import setuptools
from FocusRecorder import __version__

with open("README.MD", "r", encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().split('\n')

setuptools.setup(
    name="FocusRecorder",
    version=__version__,
    author="Czile",
    author_email="Czile@foxmail.com",
    description="记录电脑使用记录",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Czile-create/FocusRecorder",
    packages=[
        'FocusRecorder',
    ],
    package_dir={'FocusRecorder':
                 'FocusRecorder'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires = requirements,
    license='Apache License',
    entry_points={
        'console_scripts': [
            'FocusRecorder=FocusRecorder.FocusRecorder:main',
        ],
    },
)