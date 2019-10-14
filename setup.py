import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

# RELEASE STEPS
# $ python setup.py upload

__title__ = "snapshot-pyppeteer"
__description__ = "Render pyecharts as image via pyppeteer"
__url__ = "https://github.com/pyecharts/snapshot-pyppeteer"
__author_email__ = "379978424@qq.com"
__license__ = "MIT"
__requires__ = ["pyppeteer"]
__keywords__ = ["snapshot-pyppeteer", "snapshot", "pyppeteer"]
here = os.path.abspath(os.path.dirname(__file__))

__version__ = "0.0.1"


class UploadCommand(Command):
    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        print("✨✨ {0}".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
            rmtree(os.path.join(here, "build"))
            rmtree(os.path.join(here, "{0}.egg-info".format(__title__)))
        except OSError:
            pass

        self.status("Building Source and Wheel distribution…")
        os.system("{0} setup.py bdist_wheel".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system('git tag -a v{0} -m "release version v{0}"'.format(__version__))
        os.system("git push origin v{0}".format(__version__))

        sys.exit()


setup(
    name=__title__,
    version=__version__,
    description=__description__,
    url=__url__,
    author="sunhailin-Leo",
    author_email=__author_email__,
    license=__license__,
    packages=find_packages(exclude=("test",)),
    keywords=__keywords__,
    install_requires=__requires__,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
    ],
    cmdclass={"upload": UploadCommand},
)
