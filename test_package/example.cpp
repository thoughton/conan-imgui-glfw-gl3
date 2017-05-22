#include <iostream>

#include <imgui.h>

#include "imgui_impl_glfw_gl3.h"
#include <GL/gl3w.h>
#include <GLFW/glfw3.h>

int main()
{
	if (false)
	{
		glfwInit();

		gl3wInit();

		ImGui_ImplGlfwGL3_Init(nullptr, false);
	}

	ImGuiIO& io = ImGui::GetIO();

	std::cout << "ImGui::GetIO().IniFilename = " << io.IniFilename << std::endl;
}

