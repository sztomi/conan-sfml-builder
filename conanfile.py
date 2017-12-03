#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os


class SfmlBuilderConan(ConanFile):
    name = "sfml-builder"
    version = "1.0.0"
    url = "https://github.com/bincrafters/conan-sfml-builder"
    description = "Builder package for SFML."
    license = "MIT"
    exports_sources = ["sfml_builder.py"]

    def build(self):
        pass

    def package(self):
        self.copy("*.py")

    def package_info(self):
        self.env_info.PYTHONPATH.append(self.package_folder)