#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        pass

    def test(self):
        with tools.pythonpath(self):
            import sfml_builder
            assert hasattr(sfml_builder, "source")
            assert hasattr(sfml_builder, "build_module")
            assert hasattr(sfml_builder, "package_module")
