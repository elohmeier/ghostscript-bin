cmake_minimum_required(VERSION 3.24)
project(ghostscript-bin NONE)

include(ExternalProject)
include(ProcessorCount)
ProcessorCount(NPROC)
if(NPROC EQUAL 0)
    set(NPROC 1)
endif()

set(GS_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/extern/ghostscript")
set(GS_INSTALL_DIR "${CMAKE_CURRENT_BINARY_DIR}/gs-install")

find_program(STRIP strip)

ExternalProject_Add(ghostscript
    SOURCE_DIR "${GS_SOURCE_DIR}"
    BUILD_IN_SOURCE ON
    CONFIGURE_COMMAND "${GS_SOURCE_DIR}/autogen.sh"
        --prefix=${GS_INSTALL_DIR}
        --disable-cups
        --without-x
        --disable-gtk
        --disable-fontconfig
        --disable-dbus
        --disable-contrib
        --without-tesseract
        --without-ijs
        --with-drivers=PS,PNG,JPEG,TIFF,PBM
    BUILD_COMMAND make -j${NPROC}
    INSTALL_COMMAND make install
)

if(STRIP)
    ExternalProject_Add_Step(ghostscript strip
        COMMAND ${STRIP} "${GS_INSTALL_DIR}/bin/gs"
        DEPENDEES install
    )
endif()

install(
    PROGRAMS "${GS_INSTALL_DIR}/bin/gs"
    DESTINATION "${SKBUILD_PLATLIB_DIR}/ghostscript_bin/bin"
)
