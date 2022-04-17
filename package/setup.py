from setuptools import setup

environment = [
    'scikit-learn',
    'tqdm',
    'pandas',
    'numpy',
    'scipy',
    'nltk',
    'keras',
    'tensorflow',
    'torch',
    'transformers',
    'sentencepiece',
]

setup(name='BERT_Aron',
      author='Aron Kiss heavily borrowing from Rubing Shen, Chris McCormick, and Nick Ryan',
      license='MIT',
      author_email='aroki587@student.liu.se',
      version='0.1',
      description='wrapper for BERT classification models training and prediction',
      packages=['BERT_Aron'],
      zip_safe=False,
      install_requires=environment)
