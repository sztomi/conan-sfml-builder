#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os


class SfmlBuilderConan(ConanFile):
    name = "sfml-builder"
    version = "1.0.0"
    url = "https://github.com/bincrafters/conan-sfml-meta"
    description = "Builder package for SFML."
    license = "https://github.com/SFML/SFML/blob/master/license.md"
    exports_sources = ["LICENSE", "sfml_builder.py"]
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    def build(self):
        pass

    def package(self):
        self.copy("*.py")

    def package_info(self):
        self.env_info.PYTHONPATH.append(self.package_folder)