# Registered Virtual File Drivers

| Driver | ID  | Search Name | Description | URL | Contact |
| ---    | --- | ---         | ---         | --- | ---     |
| CUDA GPU  | 512 | `gds`  | The HDF5 GPUDirect Storage VFD is a Virtual File Driver (VFD) for HDF5 that can be used to interface with Nvidia's GPUDirect Storage (GDS) API. The driver is built as a plugin library that is external to HDF5.| https://github.com/hpc-io/vfd-gds	| Suren Byna (sbyna at lbl dot gov) |
| GDAL vsil |	513	| `vsil` | The HDF5 GDAL vsil Storage VFD is a Virtual File Driver (VFD) for the GDAL HDF5 driver that can be used to access any file supported by the GDAL Virtual File System Interface (https://gdal.org/user/virtual_file_systems.html). | https://github.com/OSGeo/gdal/blob/master/frmts/hdf5/hdf5vfl.h | Even Rouault (even dot rouault at spatialys dot com) |
| Unidata/UCAR NetCDF-C ByteRange |	514 |	`byte-range` | The Unidata `H5FDhttp.[ch]` VFD driver is used to support accessing remote files using the HTTP byte range mechanism. It is part of the Unidata Netcdf-C library. | https://github.com/Unidata/netcdf-c/blob/main/libhdf5/H5FDhttp.c	| Dennis Heimbigner (dmh at ucar.edu) |
