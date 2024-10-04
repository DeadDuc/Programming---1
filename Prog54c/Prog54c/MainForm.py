import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._radiusinput = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._label1.Font = System.Drawing.Font("Microsoft YaHei UI", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 10)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(249, 47)
		self._label1.TabIndex = 0
		self._label1.Text = "Radius"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# radiusinput
		# 
		self._radiusinput.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radiusinput.Location = System.Drawing.Point(267, 10)
		self._radiusinput.Name = "radiusinput"
		self._radiusinput.Size = System.Drawing.Size(525, 44)
		self._radiusinput.TabIndex = 1
		self._radiusinput.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._label2.Font = System.Drawing.Font("Microsoft YaHei UI", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 77)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(249, 47)
		self._label2.TabIndex = 2
		self._label2.Text = "Area"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._label3.Font = System.Drawing.Font("Microsoft YaHei UI", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 144)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(249, 47)
		self._label3.TabIndex = 3
		self._label3.Text = "Circumference"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.InactiveBorder
		self._label4.Font = System.Drawing.Font("Microsoft YaHei UI", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(267, 77)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(524, 47)
		self._label4.TabIndex = 4
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.InactiveBorder
		self._label5.Font = System.Drawing.Font("Microsoft YaHei UI", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(267, 144)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(524, 47)
		self._label5.TabIndex = 5
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 195)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(249, 68)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(268, 195)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(249, 68)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(522, 195)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(269, 68)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.HotTrack
		self.ClientSize = System.Drawing.Size(803, 270)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._radiusinput)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._label5.Text = ""
		self._radiusinput.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button1Click(self, sender, e):
		radius = float(self._radiusinput.Text)
		circumference = 2 * radius
		pi = 3.14159
		r2 = radius * radius
		area = pi * r2
		self._label4.Text = str(area)
		self._label5.Text = str(circumference)
		pass