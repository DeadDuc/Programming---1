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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.CornflowerBlue
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(8, 94)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(226, 46)
		self._label1.TabIndex = 0
		self._label1.Text = "Amount Due:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.CornflowerBlue
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(8, 161)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(226, 46)
		self._label2.TabIndex = 1
		self._label2.Text = "Amount Given:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(240, 94)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(222, 46)
		self._textBox1.TabIndex = 2
		self._textBox1.Text = "textBox1"
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(240, 161)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(222, 46)
		self._textBox2.TabIndex = 3
		self._textBox2.Text = "textBox2"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.CornflowerBlue
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(8, 226)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(226, 46)
		self._label3.TabIndex = 4
		self._label3.Text = "Change Due:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSteelBlue
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(240, 226)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(222, 46)
		self._label4.TabIndex = 5
		self._label4.Text = "label4"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DodgerBlue
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(8, 9)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(454, 68)
		self._label5.TabIndex = 6
		self._label5.Text = "Magic Change-O-Calculator"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.CornflowerBlue
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(8, 357)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(226, 46)
		self._label6.TabIndex = 7
		self._label6.Text = "Quarters Due:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.CornflowerBlue
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(8, 415)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(226, 46)
		self._label7.TabIndex = 8
		self._label7.Text = "Dimes Due:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.CornflowerBlue
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(8, 471)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(226, 46)
		self._label8.TabIndex = 9
		self._label8.Text = "Nickels Due:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label8.Click += self.Label8Click
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.CornflowerBlue
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(8, 526)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(226, 46)
		self._label9.TabIndex = 10
		self._label9.Text = "Pennies Due:"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.LightSteelBlue
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(240, 357)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(222, 46)
		self._label10.TabIndex = 11
		self._label10.Text = "label10"
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.LightSteelBlue
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(240, 415)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(222, 46)
		self._label11.TabIndex = 12
		self._label11.Text = "label11"
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.LightSteelBlue
		self._label12.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(240, 471)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(222, 46)
		self._label12.TabIndex = 13
		self._label12.Text = "label12"
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.LightSteelBlue
		self._label13.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(240, 526)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(222, 46)
		self._label13.TabIndex = 14
		self._label13.Text = "label13"
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(8, 576)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(454, 48)
		self._button1.TabIndex = 15
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.CornflowerBlue
		self._label14.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(8, 300)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(226, 46)
		self._label14.TabIndex = 16
		self._label14.Text = "Dollars Due:"
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.LightSteelBlue
		self._label15.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(240, 300)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(222, 46)
		self._label15.TabIndex = 17
		self._label15.Text = "label15"
		self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.RoyalBlue
		self.ClientSize = System.Drawing.Size(474, 636)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog58t"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Label8Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		amountdue = float (self._textBox1.Text)
		amountgiven = float (self._textBox2.Text)
		quartersdue = self._label10.Text
		changedue = amountgiven - amountdue
		specialdollarvariable = int(changedue)
		specialchangevariable = changedue - specialdollarvariable
		dimevariable = (changedue - (25 * quartersdue))
		if dimevariable < .10 and dimevariable > 0:
			self._label11.Text = ""
		if dimevariable < .20 and dimevariable > .10:
			self._label11.Text = "1"
		if dimevariable < .30 and dimevariable > .20:
			self._label11.Text = "2"
		changedue = self._label4.Text
		specialdollarvariable = self._label15.Text
		if changedue < .25:
			self._label10.Text = ""
		if changedue < .50 and changedue > .25:
			self._label10.Text = "1"
		if changedue < .75 and changedue > .50:
			self._label10.Text = "2"
		if changedue < 1 and changedue > .75:
			self._label10.Text = "3"
			
		pass