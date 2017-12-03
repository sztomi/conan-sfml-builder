#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import tools, CMake
import os


def source(conanfile, extracted_dir, target_dir="sources"):
    source_url = "https://github.com/SFML/SFML"
    tools.get("{0}/archive/{1}.tar.gz".format(source_url, conanfile.version))
    os.rename(extracted_dir, target_dir)


def build_module(conanfile, module_name, source_dir="sources"):
    """ Builds a SFML module """
    cmake = CMake(conanfile)
    cmake.configure(source_dir=source_dir)
    cmake.build(target="sfml-" + module_name)


def package_module(conanfile, module_name, source_dir="sources"):
    with tools.chdir(source_dir):
        conanfile.copy(pattern="LICENSE")
        conanfile.copy(
            pattern="*",
            dst="include/" + module_name,
            src="sources/include/" + module_name)
        conanfile.copy(pattern="*.dll", dst="bin", src="bin", keep_path=False)
        conanfile.copy(pattern="*.lib", dst="lib", src="lib", keep_path=False)
        conanfile.copy(pattern="*.a", dst="lib", src="lib", keep_path=False)
        conanfile.copy(pattern="*.so*", dst="lib", src="lib", keep_path=False)
        conanfile.copy(
            pattern="*.dylib", dst="lib", src="lib", keep_path=False)
