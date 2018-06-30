# Conan package of HDF5
[![Download](https://api.bintray.com/packages/arsen-studio/arsen-deps/hdf5%3Aarsen-studio/images/download.svg)](https://bintray.com/arsen-studio/arsen-deps/hdf5%3Aarsen-studio/_latestVersion)

|Linux|Windows|OS X|
|-----|-------|----|
|GITLABCI_BADGE_URL|APPVEYOR_BADGE_URL|TRAVIS_BADGE_URL|

[Conan.io](https://conan.io) package for [hdf5](https://www.hdfgroup.org/) library. This package includes main library and utilities.

The packages generated with this **conanfile** can be found in [bintray.com](https://bintray.com/arsen-studio/arsen-deps/hdf5%3Aarsen-studio/).

## Setup
To configure Conan client to work with Arsen packages, you will need to add repository to the list of remotes. To add repository, use the following command:
```
conan remote add arsen-deps https://api.bintray.com/conan/arsen-studio/arsen-deps
```

### Basic

```
$ conan install hdf5/latest@arsen-studio/stable
```

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

```
[requires]
hdf5/latest@arsen-studio/stable

[options]
hdf5:shared=true # false

[generators]
txt
cmake
```

Complete the installation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

## Develop the package

### Build packages

    $ pip install conan_package_tools bincrafters_package_tools
    $ python build.py

### Upload packages to server

    $ conan upload hdf5/latest@arsen-studio/stable --all

## Issues

If you wish to report an issue, please do so here:

https://gitlab.com/ArsenStudio/ArsenEngine/dependencies/conan-hdf5/issues

For any pull or merge request, please do so here:

https://gitlab.com/ArsenStudio/ArsenEngine/dependencies/conan-hdf5/merge_requests

## License

[MIT LICENSE](LICENSE)