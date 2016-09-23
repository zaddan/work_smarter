cmake_minimum_required(VERSION 2.8)

add_definitions(-std=c++11) #to add the -std=c++11 flag 
project(app_project)
file(GLOB all_src1 "src/*.cpp")
#install(TARGETS tool_exe DESTINATION bin) #where to place the binary
add_executable(tool_exe ${all_src1}) 
include_directories("inc") 

