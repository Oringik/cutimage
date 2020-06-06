from setuptools import setup

setup(
    name="cutimage",
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
        'torchvision',
        'torch',
        'numpy',
        'opencv-python',
        'matplotlib'
    ],
    entry_points='''
        [console_scripts]
        cutimage=main:cli
    ''',
)