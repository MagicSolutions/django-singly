from setuptools import setup, find_packages

setup(
    name='django-singly',
    version='0.2.5',
    description='Django package for integration with Singly API (uses open-singly)',
    author='Venelin Stoykov',
    author_email='venelin@magicsolutions.bg',
    url='https://github.com/MagicSolutions/django-singly',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
      'Django>=1.4',
      'django-json-field>=0.5.4',
      'open-singly>=0.2',
    ],
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Web Environment',
      'Intended Audience :: Developers',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
    ]
)
