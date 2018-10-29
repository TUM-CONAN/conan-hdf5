import os
from conans import ConanFile, tools, CMake


class Hdf5Conan(ConanFile):
    name = "hdf5"
    version = "1.10.3"
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
        minor_version = ".".join(self.version.split(".")[:2])
        tools.get("https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-{0}/hdf5-{1}/src/hdf5-{1}.tar.gz"
                  .format(minor_version, self.version))
        os.rename("hdf5-{0}".format(self.version), self.source_subfolder)

    def configure(self):
        self.options["zlib"].shared = self.options.shared

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self.build_subfolder, defs={
            "HDF5_BUILD_EXAMPLES": False,
            "HDF5_BUILD_TOOLS": True,
            "HDF5_BUILD_HL_LIB": False,
            "HDF5_BUILD_CPP_LIB": True,
            "HDF5_ENABLE_Z_LIB_SUPPORT": True,
        })
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("COPYING", src=self.source_subfolder, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

        if not self.options.shared and not self.settings.os == "Windows":
            self.cpp_info.libs.append("dl")
