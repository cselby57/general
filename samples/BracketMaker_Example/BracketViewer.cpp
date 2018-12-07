#include "BracketViewer.h"
// entry point for bracket maker
// initialize the windows form 
using namespace System;
using namespace System::Windows::Forms;

[STAThreadAttribute]
int main(cli::array <String^>^ args) {
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);
	BracketMaker::BracketViewer form;
	Application::Run(%form);
	return 0;
}