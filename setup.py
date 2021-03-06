from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='twelisis',
      version='0.1.5',
	  description='Extracting Tweets from twitter and analysing them',
	  long_description=readme(),
      url='https://github.com/yagamiash/twelisis.git',
	  download_url='https://github.com/yagamiash/twelisis/blob/master/dist/twelisis-0.1.tar.gz',
	  classifiers=['Programming Language :: Python :: 2.7','Topic :: Text Processing :: Linguistic'],
      author='Ashik Poovanna',
      author_email='ashobot@gmail.com',
      packages=['twelisis'],
	  install_requires=['tweepy','pandas','vaderSentiment','twython'],
      test_suite='nose.collector',
      tests_require=['nose'],
	  include_package_data=True, 
	  )
