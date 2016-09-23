cmake_minimum_required(VERSION 2.8)

project(app_project)
file(GLOB all_src "my_src/*.cpp") #includes all the files in the folder src/
add_executable(myapp ${all_src}) #which files to build
install(TARGETS myapp DESTINATION bin) #where to place the binary
include_directories(my_inc_folder)  #adding the include folder
