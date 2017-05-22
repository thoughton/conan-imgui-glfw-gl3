from conans import ConanFile, CMake, tools
#import os


class Imguiglfwgl3Conan(ConanFile):
    name = "ImGui_glfw_gl3"
    version = "latest"
    license = "MIT"
    url = "https://github.com/thoughton/conan-imgui-glfw-gl3"
    description = "ImGui GLFW binding with OpenGL3 + shaders."

    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "LICENSE"

    requires = "ImGui/latest@thoughton/testing", "glfw/latest@thoughton/testing", "gl3w/latest@thoughton/testing"

    def source(self):
        tools.download("https://github.com/ocornut/imgui/raw/master/examples/opengl3_example/imgui_impl_glfw_gl3.cpp", "imgui_impl_glfw_gl3/imgui_impl_glfw_gl3.cpp")
        tools.download("https://github.com/ocornut/imgui/raw/master/examples/opengl3_example/imgui_impl_glfw_gl3.h", "imgui_impl_glfw_gl3/imgui_impl_glfw_gl3.h")

    def build(self):
        cmake = CMake(self)
        self.run('cmake . %s' % (cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="imgui_impl_glfw_gl3", keep_path=True)
        self.copy("*imguiglfwgl3.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["imguiglfwgl3"]

