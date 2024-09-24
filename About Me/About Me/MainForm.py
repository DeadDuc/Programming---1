import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(260, 235)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(333, 65)
		self._button1.TabIndex = 0
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(12, 235)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(242, 65)
		self._button2.TabIndex = 1
		self._button2.Text = "Show"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(599, 235)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(242, 65)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(829, 223)
		self._label1.TabIndex = 3
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(853, 312)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "About Me"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		self._label1.Text = "Just a kid from janesville who likes playing video games." 
		pass

	def Button1Click(self, sender, e):
		self._label1.Text = "" 
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass