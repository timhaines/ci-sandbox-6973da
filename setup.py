import os
from setuptools import setup
setup(name="sandbox-pkg", version=os.environ.get("BUILD_VERSION","0.0.0"), packages=["sandbox_pkg"], package_data={"sandbox_pkg":["marker.txt"]}, include_package_data=True)
