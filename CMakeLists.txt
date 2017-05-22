project(imguiglfwgl3)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(SRC_FILES
	imgui_impl_glfw_gl3/imgui_impl_glfw_gl3.cpp
	)

include_directories(
	imgui_impl_glfw_gl3
	)

add_library(imguiglfwgl3 STATIC ${SRC_FILES})

