cmake_minimum_required(VERSION 3.12...3.22)
project(vertex_one_description)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME} SKIP_COMPILE)

include(GNUInstallDirs)
install(DIRECTORY launch DESTINATION ${CMAKE_INSTALL_DATADIR}/${PROJECT_NAME})
install(DIRECTORY config DESTINATION ${CMAKE_INSTALL_DATADIR}/${PROJECT_NAME} OPTIONAL)
install(DIRECTORY rviz DESTINATION ${CMAKE_INSTALL_DATADIR}/${PROJECT_NAME})
install(DIRECTORY urdf DESTINATION ${CMAKE_INSTALL_DATADIR}/${PROJECT_NAME})
install(DIRECTORY urdf/meshes
        DESTINATION share/${PROJECT_NAME}/gz_resources/${PROJECT_NAME}/urdf)


ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/hooks/gz_resources.dsv.in")
ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/hooks/gz_resources.sh.in")

#Package
ament_package()
