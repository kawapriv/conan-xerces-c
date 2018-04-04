import os
from shutil import copyfile

from conans import ConanFile, tools, CMake
from conans.util import files

class XercesCConan(ConanFile):
    name = "xerces-c"
    version = "3.2.1"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = ("shared=False", "fPIC=True")
    url = "http://github.com/kwallner/conan-xerces-c"
    license = 'Apache License'
    description = "XML Parser"
    source_subfolder = "sources"
    no_copy_source = True

    def source(self):
        tools.get("http://ftp-stud.hs-esslingen.de/pub/Mirrors/ftp.apache.org/dist//xerces/c/3/sources/%s-%s.tar.gz"  % (self.name, self.version))
        os.rename("%s-%s" % (self.name, self.version), self.source_subfolder)
        
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="%s/%s" % (self.source_folder, self.source_subfolder))
        cmake.build()
        cmake.install()
               
    def package_info(self):
        self.env_info.XercesC_DIR = self.package_folder