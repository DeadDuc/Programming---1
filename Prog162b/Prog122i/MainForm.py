﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("MingLiU_HKSCS-ExtB", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 21
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(1210, 361)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("MingLiU_HKSCS-ExtB", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 401)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(397, 83)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("MingLiU_HKSCS-ExtB", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(829, 401)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(394, 83)
		self._button2.TabIndex = 2
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("MingLiU_HKSCS-ExtB", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(416, 401)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(407, 83)
		self._button3.TabIndex = 3
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(1235, 496)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122i"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		Application.Exit()
		pass

	def Button3Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button1Click(self, sender, e):
		heading = "Negative Number\tNumber\t\tNeg Cube Root\tCube Root\t\tNegative Cubed\t\tCubed"
		self._listBox1.Items.Add(heading)
		for num in range(1, 27-1):
			nnum = num * -1
			pcube = num**3
			pcbrt = num**(1.0/3.0)
			ncbrt = abs(pcbrt) * -1
			ncube = ((nnum**3) * -1) * -1
			msg = str(nnum) + "\t\t" + str(num) + "\t\t" + str(ncbrt) + "\t\t\t" + str(pcbrt) + "\t\t" + str(ncube) + "\t\t" + str(pcube)
			self._listBox1.Items.Add(msg)
		pass