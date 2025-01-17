import re
import sys


PACKAGE_REGEX = r'^[_a-z][_a-z0-9]+$'

repo_name = '{{ cookiecutter.repo_name }}'
package_name = '{{ cookiecutter.package_name }}'
distribution_name = '{{ cookiecutter.distribution_name }}'

# enforce naming conventions

if "_" in repo_name:
    print('ERROR: The repo name "%s" contains underscores. Hyphens are more user-friendly. Remove the underscores or use - instead.' % package_name)
    sys.exit(1)
elif not repo_name.islower():
    print('ERROR: The repo name "%s" contains upper case characters. Use lower case.' % repo_name)
    sys.exit(1)

if not re.match(PACKAGE_REGEX, package_name):
    print('ERROR: "%s" is not a valid Python PEP8 package name. It must be all lower case, not begin with a number, and have no hyphens.' % package_name)
    sys.exit(1)

if "_" in package_name:
    print('WARNING: The package name "%s" contains underscores. PEP8 discourages the use of underscores in package names.' % package_name)

if len(package_name) > 12:
    print('WARNING: The package name "%s" is longer than 12 chars. PEP8 encourages short package names.' % package_name)


if "_" in distribution_name:
    print('ERROR: The distribution name "%s" contains underscores. Hyphens are more user-friendly. Remove the underscores or use - instead.' % distribution_name)
    sys.exit(1)
elif not distribution_name.islower():
    print('ERROR: The distribution name "%s" contains upper case characters. Use lower case.' % distribution_name)
    sys.exit(1)
