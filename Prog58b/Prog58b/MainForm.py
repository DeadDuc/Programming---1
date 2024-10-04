import math
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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(394, 86)
		self._label1.TabIndex = 0
		self._label1.Text = "The quadratic formula:      [-B+/- √(B^2 - 4AC)]/2A"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(13, 103)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(123, 46)
		self._label2.TabIndex = 1
		self._label2.Text = "A Input"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 156)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(123, 46)
		self._label3.TabIndex = 2
		self._label3.Text = "B Input"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(13, 210)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(123, 46)
		self._label4.TabIndex = 3
		self._label4.Text = "C Input"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(142, 103)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(265, 46)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(142, 156)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(265, 46)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.White
		self._textBox3.Location = System.Drawing.Point(142, 210)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(265, 46)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(414, 13)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(408, 243)
		self._label5.TabIndex = 7
		self._label5.Text = "label5"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 262)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(395, 55)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(414, 262)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(202, 55)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(623, 262)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(199, 55)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(833, 328)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog58b"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()

		

	def MainFormLoad(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label5.Text = ""
		pass

	def Button1Click(self, sender, e):
		A = float (self._textBox1.Text)
		B = float (self._textBox2.Text)
		C = float (self._textBox3.Text)
		negativeroot = (-B - math.sqrt(b**2 - 4 * A * C))/2 * A
		positiveroot = (-B + math.sqrt(b**2 - 4 * A * C))/2 * A
		self._label5.Text = str(negativeroot)  str(positiveroot)
		pass