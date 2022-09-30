import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rotary',
    version='1.0.0',
    description='A Python driver to read a rotary encoder.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/submer-crypto/micropython-rotary',
    license='MIT',
    packages=['rotary'],
    package_dir={
        'rotary': '.'
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.8'
)
