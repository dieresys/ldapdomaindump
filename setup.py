from setuptools import setup
setup(name='ldapdomaindump',
      version='0.8.0',
      description='Active Directory information dumper via LDAP',
      author='Dirk-jan Mollema',
      author_email='dirkjan@sanoweb.nl',
      url='https://github.com/dirkjanm/ldapdomaindump/',
      packages=['ldapdomaindump'],
      install_requires=['dnspython','ldap3'],
      package_data={'ldapdomaindump': ['style.css']},
      include_package_data=True,
      scripts=['bin/ldapdomaindump']
      )
