from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("python.flake8")

name = "hello_world_app"
version = "0.1.1"
default_task = "publish"

@init
def initialize(project):
    project.build_depends_on("wheel")
    project.depends_on("flask")
    project.set_property("distutils_classifiers", [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9"
    ])
    project.set_property("distutils_commands", ["sdist", "bdist_wheel"])
    project.set_property("distutils_upload_repository", "https://upload.pypi.org/legacy/")
