import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(876, 23)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 40)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(876, 23)
		self._label2.TabIndex = 1
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(12, 67)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(876, 23)
		self._label3.TabIndex = 2
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(12, 94)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(876, 23)
		self._label4.TabIndex = 3
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(12, 121)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(876, 23)
		self._label5.TabIndex = 4
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(12, 148)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(876, 23)
		self._label6.TabIndex = 5
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(12, 175)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(876, 23)
		self._label7.TabIndex = 6
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(12, 202)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(876, 23)
		self._label8.TabIndex = 7
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 228)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(309, 73)
		self._button1.TabIndex = 8
		self._button1.Text = "Show Schedule"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(327, 228)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(248, 72)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(581, 228)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(307, 71)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(900, 310)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Good Schedule"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "AP World History 8:00-8:47"
		self._label2.Text = "Computer Programming :P 8:52-9:39"
		self._label3.Text = "Chemistry Honors 9:41-10:31"
		self._label4.Text = "Accelerated English 9-10 Honors 10:36-11:25"
		self._label5.Text = "Exploring Business and Marketing 11:30-12:52"
		self._label6.Text = "Geometry Honors 12:57-1:44"
		self._label7.Text = "Freshman Seminar 1:49-2:36"
		self._label8.Text = "Spanish language and Culture 2:41-3:28"
		pass

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Label3Click(self, sender, e):
		pass