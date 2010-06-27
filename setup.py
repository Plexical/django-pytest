from distutils.core import setup

setup(
        name="django-pytest",
        version="0.1.2",
        author="Dusty Phillips",
        author_email="dusty@archlinux.ca",
        packages=['django_pytest', 'django_pytest.management.commands'],
        url="http://github.com/buchuki/django-pytest",
        license="LICENSE.txt",
        description="django test runner to use py.test tests",
        long_description=open('README.txt').read(),
)
