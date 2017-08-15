from setuptools import setup, find_packages

setup (
  name                 = "todobackend",
  version              = "0.1.0",
  description          = "Todobackend Django REST service",
  # This will include any subdirectories that include __init__.py
  packages             = find_packages(),
  # This will include the packages in the final build distribution
  include_package_data = True,
  # An array to any scripts to be called on target platform.
  # Make manage.py callable anywhere within the virtual environment.
  scripts              = ["manage.py"],
  # These come from the requirements.txt
  install_requires     = ["Django>=1.11,<2.0",
                          "django-cors-headers>=2.0,<3.0",
                          "djangorestframework>=3.6",
                          "MySQL-python>=1.2.5",
                          "pytz>=2017"],
  extras_require       = {
                            "test": [
                              "colorama>=0.3,<0.4",
                              "coverage>=4.0,<5.0",
                              "django-nose>=1.4.4",
                              "nose>=1.3.7",
                              "pinocchio>=0.4.2"
                            ]
                         }
)
