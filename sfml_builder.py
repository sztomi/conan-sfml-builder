#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import tools, CMake
import os


def source(conanfile, target_dir="sources"):
    source_url = "https://github.com/SFML/SFML"
    tools.get("{0}/archive/{1}.tar.gz".format(source_url, conanfile.version))
    extracted_dir = conanfile.name + "-" + conanfile.version
    os.rename(extracted_dir, target_dir)


def build_module(conanfile, module_name, source_dir="sources"):
    """ Builds a SFML module """
    cmake = CMake(conanfile)
    cmake.configure(source_dir=source_dir)
    cmake.build(target=module_name)


def package_module(conanfile, module_name, source_dir="sources"):
    with tools.chdir(source_dir):
        self.copy(pattern="LICENSE")
        self.copy(
            pattern="*",
            dst="include/" + module_name,
            src="sources/include/" + module_name)
        self.copy(pattern="*.dll", dst="bin", src="bin", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", src="lib", keep_path=False)