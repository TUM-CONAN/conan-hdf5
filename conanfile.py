import os
import shutil
from conans import ConanFile, tools, CMake


class Hdf5Conan(ConanFile):
    name = "hdf5"
    version = "1.10.4"
    description = "HDF5 C and C++ libraries"
    url = "https://gitlab.com/ArsenStudio/ArsenEngine/dependencies/conan-{0}".format(name)
    homepage = "https://www.hdfgroup.org/"

    license = "https://support.hdfgroup.org/ftp/HDF5/releases/COPYING"

    exports = ["LICENSE.md"]

    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False]
    }
    default_options = "shared=False"
    short_paths = True

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    requires = "zlib/1.2.11@conan/stable"

    def source(self):
        git = tools.Git()
        git.clone("https://bitbucket.hdfgroup.org/scm/hdffv/hdf5.git",
                  "hdf5-{0}".format(self.version.replace(".", "_")))

    def configure(self):
        self.options["zlib"].shared = self.options.shared

    def build(self):
        self.cmake = CMake(self)

        self.cmake.configure(build_folder=self.build_subfolder, defs={
            "BUILD_SHARED_LIBS": self.options["shared"],
            "HDF5_BUILD_EXAMPLES": "OFF",
            "HDF5_BUILD_TOOLS": "ON",
            "HDF5_BUILD_HL_LIB": "OFF",
            "HDF5_BUILD_CPP_LIB": "OFF",
            "HDF5_ENABLE_Z_LIB_SUPPORT": "ON",
        })
        self.cmake.build()

    def package(self):
        self.cmake.install()
        self.copy("COPYING", src=self.source_subfolder, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

        if not self.options.shared and not self.settings.os == "Windows":
            self.cpp_info.libs.append("dl")
