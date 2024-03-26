PhysX has a circular dependency between the PhysX and PvD library, which premake does not handler gracefully. 
In order to build the Linux libraries, you need to remove PvD support. This can be done in the following ways:

- Before generating the Makefiles, the CMakefile describing the CXX flags where PX_SUPPORT_PVD and PX_SUPPORT_OMNI_PVD are set.
  Edit all configurations to =0

- After the Makefiles have been generated, go into the appropriate dir (e.g. linux-debug) and grep for PX_SUPPORT_PVD. 
  Set both PX_SUPPORT_PVD and PX_SUPPORT_OMNI_PVD to =0
  