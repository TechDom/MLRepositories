from setuptools import setup

setup(name='persephone',
      version='0.4.2',
      description='A tool for developing automatic phoneme transcription models',
      long_description=open('README.rst', encoding="utf8").read(),
      url='https://github.com/oadams/persephone',
      author='Oliver Adams',
      author_email='oliver.adams@gmail.com',
      license='Apache2.0',
      packages=['persephone', 'persephone.datasets', 'persephone.preprocess'],
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='speech-recognition machine-learning acoustic-models artificial-intelligence neural-networks',
      install_requires=[
           'nltk==3.4.5',
           'numpy>=1.14.5,<2',
           'python-speech-features==0.6',
           'scipy>=1.1.0,<2',
           'tensorflow>=1.13.1,<2',
           'scikit-learn==0.21.2',
           'pympi-ling==1.69',
           'pydub==0.20.0',
           'pint==0.9',
      ],
      include_package_data = True,
)