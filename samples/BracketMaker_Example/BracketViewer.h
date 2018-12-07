#pragma once
#include "bracketMaker.h"
#include <msclr\marshal_cppstd.h>

/*	Cameron Selby Spring 2018
	Toolbox generated windows form code for very basic march madness bracket generator
	
	* text alignment needs work*/

namespace BracketMaker {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	/// <summary>
	/// Summary for BracketViewer
	/// </summary>
	public ref class BracketViewer : public System::Windows::Forms::Form
	{
	public:
		BracketViewer(void)
		{
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			// ehh
			
			//
		}

	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~BracketViewer()
		{
			if (components)
			{
				delete components;
			}
		}

	private: System::Windows::Forms::Label^  SWsecondRound;
	private: System::Windows::Forms::Label^  SWsweet16;
	private: System::Windows::Forms::Label^  SWelite8;
	private: System::Windows::Forms::Label^  SouthF4;
	private: System::Windows::Forms::Label^  SWfinalist;
	private: System::Windows::Forms::Label^  Champ;
	private: System::Windows::Forms::Label^  EMWsecondRound;
	private: System::Windows::Forms::Label^  EMWsweet16;
	private: System::Windows::Forms::Label^  EMWelite8;
	private: System::Windows::Forms::Label^  EastF4;
	private: System::Windows::Forms::Label^  EMWfinalist;
	private: System::Windows::Forms::Label^  MidwestF4;
	private: System::Windows::Forms::Label^  WestF4;
	private: System::Windows::Forms::Button^  bracketBut;
	private: System::Windows::Forms::Label^  label1;



	protected:

	private:
		/// <summary>
		/// Required designer variable.
		/// </summary>
		System::ComponentModel::Container ^components;

#pragma region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		void InitializeComponent(void)
		{
			System::ComponentModel::ComponentResourceManager^  resources = (gcnew System::ComponentModel::ComponentResourceManager(BracketViewer::typeid));
			this->SWsecondRound = (gcnew System::Windows::Forms::Label());
			this->SWsweet16 = (gcnew System::Windows::Forms::Label());
			this->SWelite8 = (gcnew System::Windows::Forms::Label());
			this->SouthF4 = (gcnew System::Windows::Forms::Label());
			this->SWfinalist = (gcnew System::Windows::Forms::Label());
			this->Champ = (gcnew System::Windows::Forms::Label());
			this->EMWsecondRound = (gcnew System::Windows::Forms::Label());
			this->EMWsweet16 = (gcnew System::Windows::Forms::Label());
			this->EMWelite8 = (gcnew System::Windows::Forms::Label());
			this->EastF4 = (gcnew System::Windows::Forms::Label());
			this->EMWfinalist = (gcnew System::Windows::Forms::Label());
			this->MidwestF4 = (gcnew System::Windows::Forms::Label());
			this->WestF4 = (gcnew System::Windows::Forms::Label());
			this->bracketBut = (gcnew System::Windows::Forms::Button());
			this->label1 = (gcnew System::Windows::Forms::Label());
			this->SuspendLayout();
			// 
			// SWsecondRound
			// 
			this->SWsecondRound->AutoSize = true;
			this->SWsecondRound->BackColor = System::Drawing::Color::Transparent;
			this->SWsecondRound->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->SWsecondRound->ForeColor = System::Drawing::SystemColors::ControlText;
			this->SWsecondRound->Location = System::Drawing::Point(84, 9);
			this->SWsecondRound->Name = L"SWsecondRound";
			this->SWsecondRound->Size = System::Drawing::Size(0, 15);
			this->SWsecondRound->TabIndex = 1;
			// 
			// SWsweet16
			// 
			this->SWsweet16->AutoSize = true;
			this->SWsweet16->BackColor = System::Drawing::Color::FromArgb(static_cast<System::Int32>(static_cast<System::Byte>(0)), static_cast<System::Int32>(static_cast<System::Byte>(0)),
				static_cast<System::Int32>(static_cast<System::Byte>(0)), static_cast<System::Int32>(static_cast<System::Byte>(0)));
			this->SWsweet16->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->SWsweet16->Location = System::Drawing::Point(151, 30);
			this->SWsweet16->Name = L"SWsweet16";
			this->SWsweet16->Size = System::Drawing::Size(0, 15);
			this->SWsweet16->TabIndex = 2;
			// 
			// SWelite8
			// 
			this->SWelite8->AutoSize = true;
			this->SWelite8->BackColor = System::Drawing::Color::Transparent;
			this->SWelite8->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->SWelite8->Location = System::Drawing::Point(207, 65);
			this->SWelite8->Name = L"SWelite8";
			this->SWelite8->Size = System::Drawing::Size(0, 15);
			this->SWelite8->TabIndex = 3;
			// 
			// SouthF4
			// 
			this->SouthF4->AutoSize = true;
			this->SouthF4->BackColor = System::Drawing::Color::Transparent;
			this->SouthF4->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->SouthF4->Location = System::Drawing::Point(267, 125);
			this->SouthF4->Name = L"SouthF4";
			this->SouthF4->Size = System::Drawing::Size(0, 15);
			this->SouthF4->TabIndex = 4;
			// 
			// SWfinalist
			// 
			this->SWfinalist->AutoSize = true;
			this->SWfinalist->BackColor = System::Drawing::Color::Transparent;
			this->SWfinalist->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->SWfinalist->Location = System::Drawing::Point(248, 200);
			this->SWfinalist->Name = L"SWfinalist";
			this->SWfinalist->Size = System::Drawing::Size(0, 15);
			this->SWfinalist->TabIndex = 5;
			// 
			// Champ
			// 
			this->Champ->AutoSize = true;
			this->Champ->BackColor = System::Drawing::Color::Transparent;
			this->Champ->Location = System::Drawing::Point(351, 259);
			this->Champ->Name = L"Champ";
			this->Champ->Size = System::Drawing::Size(0, 13);
			this->Champ->TabIndex = 6;
			this->Champ->TextAlign = System::Drawing::ContentAlignment::MiddleCenter;
			// 
			// EMWsecondRound
			// 
			this->EMWsecondRound->AutoSize = true;
			this->EMWsecondRound->BackColor = System::Drawing::Color::Transparent;
			this->EMWsecondRound->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->EMWsecondRound->Location = System::Drawing::Point(642, 9);
			this->EMWsecondRound->Name = L"EMWsecondRound";
			this->EMWsecondRound->Size = System::Drawing::Size(0, 15);
			this->EMWsecondRound->TabIndex = 7;
			// 
			// EMWsweet16
			// 
			this->EMWsweet16->AutoSize = true;
			this->EMWsweet16->BackColor = System::Drawing::Color::Transparent;
			this->EMWsweet16->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->EMWsweet16->Location = System::Drawing::Point(572, 30);
			this->EMWsweet16->Name = L"EMWsweet16";
			this->EMWsweet16->Size = System::Drawing::Size(0, 15);
			this->EMWsweet16->TabIndex = 8;
			// 
			// EMWelite8
			// 
			this->EMWelite8->AutoSize = true;
			this->EMWelite8->BackColor = System::Drawing::Color::Transparent;
			this->EMWelite8->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->EMWelite8->Location = System::Drawing::Point(515, 63);
			this->EMWelite8->Name = L"EMWelite8";
			this->EMWelite8->Size = System::Drawing::Size(0, 15);
			this->EMWelite8->TabIndex = 9;
			// 
			// EastF4
			// 
			this->EastF4->AutoSize = true;
			this->EastF4->BackColor = System::Drawing::Color::Transparent;
			this->EastF4->Location = System::Drawing::Point(450, 125);
			this->EastF4->Name = L"EastF4";
			this->EastF4->Size = System::Drawing::Size(0, 13);
			this->EastF4->TabIndex = 10;
			// 
			// EMWfinalist
			// 
			this->EMWfinalist->AutoSize = true;
			this->EMWfinalist->BackColor = System::Drawing::Color::Transparent;
			this->EMWfinalist->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->EMWfinalist->Location = System::Drawing::Point(450, 292);
			this->EMWfinalist->Name = L"EMWfinalist";
			this->EMWfinalist->Size = System::Drawing::Size(0, 15);
			this->EMWfinalist->TabIndex = 11;
			// 
			// MidwestF4
			// 
			this->MidwestF4->AutoSize = true;
			this->MidwestF4->BackColor = System::Drawing::Color::Transparent;
			this->MidwestF4->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->MidwestF4->Location = System::Drawing::Point(450, 375);
			this->MidwestF4->Name = L"MidwestF4";
			this->MidwestF4->Size = System::Drawing::Size(0, 15);
			this->MidwestF4->TabIndex = 12;
			// 
			// WestF4
			// 
			this->WestF4->AutoSize = true;
			this->WestF4->BackColor = System::Drawing::Color::Transparent;
			this->WestF4->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 9, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				static_cast<System::Byte>(0)));
			this->WestF4->Location = System::Drawing::Point(270, 375);
			this->WestF4->Name = L"WestF4";
			this->WestF4->Size = System::Drawing::Size(0, 15);
			this->WestF4->TabIndex = 13;
			// 
			// bracketBut
			// 
			this->bracketBut->Location = System::Drawing::Point(331, 157);
			this->bracketBut->Name = L"bracketBut";
			this->bracketBut->Size = System::Drawing::Size(75, 23);
			this->bracketBut->TabIndex = 14;
			this->bracketBut->Text = L"Generate";
			this->bracketBut->UseVisualStyleBackColor = true;
			this->bracketBut->MouseClick += gcnew System::Windows::Forms::MouseEventHandler(this, &BracketViewer::bracketBut_MouseClick);
			// 
			// label1
			// 
			this->label1->AutoSize = true;
			this->label1->BackColor = System::Drawing::Color::Transparent;
			this->label1->Location = System::Drawing::Point(308, 112);
			this->label1->Name = L"label1";
			this->label1->Size = System::Drawing::Size(136, 26);
			this->label1->TabIndex = 15;
			this->label1->Text = L"Selby\'s Dumb, Ugly,\nbut 'Impartial' Bracket Maker";
			this->label1->TextAlign = System::Drawing::ContentAlignment::MiddleCenter;
			// 
			// BracketViewer
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(6, 13);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->BackColor = System::Drawing::SystemColors::ButtonShadow;
			this->BackgroundImage = (cli::safe_cast<System::Drawing::Image^>(resources->GetObject(L"$this.BackgroundImage")));
			this->ClientSize = System::Drawing::Size(741, 527);
			this->Controls->Add(this->label1);
			this->Controls->Add(this->bracketBut);
			this->Controls->Add(this->WestF4);
			this->Controls->Add(this->MidwestF4);
			this->Controls->Add(this->EMWfinalist);
			this->Controls->Add(this->EastF4);
			this->Controls->Add(this->EMWelite8);
			this->Controls->Add(this->EMWsweet16);
			this->Controls->Add(this->EMWsecondRound);
			this->Controls->Add(this->Champ);
			this->Controls->Add(this->SWfinalist);
			this->Controls->Add(this->SouthF4);
			this->Controls->Add(this->SWelite8);
			this->Controls->Add(this->SWsweet16);
			this->Controls->Add(this->SWsecondRound);
			this->Name = L"BracketViewer";
			this->Text = L"BracketViewer";
			this->Load += gcnew System::EventHandler(this, &BracketViewer::BracketViewer_Load);
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
	private: System::Void BracketViewer_Load(System::Object^  sender, System::EventArgs^  e) {
	}
	private: System::Void pictureBox1_Click(System::Object^  sender, System::EventArgs^  e) {
	}
	private: System::Void bracketBut_MouseClick(System::Object^  sender, System::Windows::Forms::MouseEventArgs^  e) {
		// if they clicked the button they want a bracket
		B theB;
		team theWinner = theB.getChampion(theB.theBracket); // initialize a brakcet and solve it
		// clear all the labels
		SWsecondRound->Text = "";
		SWsweet16->Text = "";
		SWelite8->Text = "";
		SouthF4->Text = "";
		WestF4->Text = "";
		SWfinalist->Text = "";
		Champ->Text = "";
		EastF4->Text = "";
		MidwestF4->Text = "";
		EMWfinalist->Text = "";
		EMWelite8->Text = "";
		EMWsweet16->Text = "";
		EMWsecondRound->Text = "";
		// fill all the labels
		// south & west 32
		for (int i = 0; i < 8; i++) {
			SWsecondRound->Text += theB.theBracket.south.firstRound[i].winningTeam.seed + "\n\n";
		}
		SWsecondRound->Text += "\n";
		for (int i = 0; i < 8; i++) {
			SWsecondRound->Text += theB.theBracket.west.firstRound[i].winningTeam.seed + "\n\n";
		}
		// south & west 16
		for (int i = 0; i < 4; i++) {
			SWsweet16->Text += theB.theBracket.south.secondRound[i].winningTeam.seed + "\n\n\n\n";
		}
		for (int i = 0; i < 4; i++) {
			SWsweet16->Text += theB.theBracket.west.secondRound[i].winningTeam.seed + "\n\n\n\n";
		}
		// south & west 8
		for (int i = 0; i < 2; i++) {
			SWelite8->Text += theB.theBracket.south.sweet16[i].winningTeam.seed + "\n\n\n\n\n\n\n\n";
		}
		for (int i = 0; i < 2; i++) {
			SWelite8->Text += theB.theBracket.west.sweet16[i].winningTeam.seed + "\n\n\n\n\n\n\n\n";
		}
		// south & west 4
		SouthF4->Text += theB.theBracket.south.elite8.winningTeam.seed;
		WestF4->Text += theB.theBracket.west.elite8.winningTeam.seed;
		// south & west finalist
		String^ SWfinalistRegion = gcnew String(theB.theBracket.final4WestSouth.winningTeam.regionFrom.c_str());
		SWfinalist->Text += SWfinalistRegion + " ";
		SWfinalist->Text += theB.theBracket.final4WestSouth.winningTeam.seed;
		// champion
		String^ ChampStr = gcnew String(theB.theBracket.championship.winningTeam.regionFrom.c_str());
		Champ->Text += ChampStr + " ";
		Champ->Text += theB.theBracket.championship.winningTeam.seed;
		// south & west finalist
		String^ EMWfinalistRegion = gcnew String(theB.theBracket.final4EastMidwest.winningTeam.regionFrom.c_str());
		EMWfinalist->Text += EMWfinalistRegion + " ";
		EMWfinalist->Text += theB.theBracket.final4EastMidwest.winningTeam.seed;
		// east & midwest 4
		EastF4->Text += theB.theBracket.east.elite8.winningTeam.seed;
		MidwestF4->Text += theB.theBracket.east.elite8.winningTeam.seed;
		// east & midwest 32
		for (int i = 0; i < 8; i++) {
			EMWsecondRound->Text += theB.theBracket.east.firstRound[i].winningTeam.seed + "\n\n";
		}
		EMWsecondRound->Text += "\n";
		for (int i = 0; i < 8; i++) {
			EMWsecondRound->Text += theB.theBracket.midwest.firstRound[i].winningTeam.seed + "\n\n";
		}
		// east & midwest 16
		for (int i = 0; i < 4; i++) {
			EMWsweet16->Text += theB.theBracket.east.secondRound[i].winningTeam.seed + "\n\n\n\n";
		}
		for (int i = 0; i < 4; i++) {
			EMWsweet16->Text += theB.theBracket.midwest.secondRound[i].winningTeam.seed + "\n\n\n\n";
		}
		// east & midwest 8
		for (int i = 0; i < 2; i++) {
			EMWelite8->Text += theB.theBracket.east.sweet16[i].winningTeam.seed + "\n\n\n\n\n\n\n\n";
		}
		SWelite8->Text += "\n";
		for (int i = 0; i < 2; i++) {
			EMWelite8->Text += theB.theBracket.midwest.sweet16[i].winningTeam.seed + "\n\n\n\n\n\n\n\n";
		}

		
	}
};
}
