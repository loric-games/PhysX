import os
from conan import ConanFile
from conan.tools.files import copy

class sampleRecipe(ConanFile):
    settings = "os", "build_type"
    name = "physx"
    version = "5.3.1"

    def layout(self):
        self.folders.build = os.path.join( ".." )
        self.folders.source = self.folders.build
        self.cpp.includedirs = ["include"]
        
        osSubDir = "win.x86_64.vc142.mt"
        if self.settings.os == "Linux":
            osSubDir = "linux.clang"
            
        buildTypeSubDir = "debug"
        if self.settings.build_type == "Release":
            buildTypeSubDir = "checked"
        
        self.cpp.build.libdirs = [ os.path.join( "bin", osSubDir, buildTypeSubDir ) ]

    def package(self):
        local_include_folder = os.path.join( self.source_folder, "include" )
        local_lib_dir = os.path.join( self.build_folder, self.cpp.build.libdirs[ 0 ] )
        copy( self, "*.h", local_include_folder, os.path.join( self.package_folder, "include" ), keep_path = True )
        copy( self, "*.lib", local_lib_dir, os.path.join( self.package_folder, "lib" ), keep_path = False )
        copy( self, "*.pdb", local_lib_dir, os.path.join( self.package_folder, "lib" ), keep_path = False )
        copy( self, "*.a", local_lib_dir, os.path.join( self.package_folder, "lib" ), keep_path = False )

    def package_info(self):
        self.cpp_info.libs = [
            "PhysX_static_64", 
            "PhysXCommon_static_64",
            "PhysXExtensions_static_64",
            "PhysXPvdSDK_static_64",
            #"PhysX_static_64", <-- There is a circular dependency which must be hand edited into projects using the PhysX library on Linux
            "PhysXFoundation_static_64",
            "PhysXCooking_static_64"
        ]
        #if self.settings.os == "Linux":
        #    [ "lib" + s for s in libList ]
