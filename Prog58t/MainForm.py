﻿import System.Drawing
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
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
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
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(240, 161)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(222, 46)
		self._textBox2.TabIndex = 3
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
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(236, 576)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(232, 48)
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
		self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(122, 576)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(112, 48)
		self._button2.TabIndex = 18
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(8, 576)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(112, 48)
		self._button3.TabIndex = 19
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.RoyalBlue
		self.ClientSize = System.Drawing.Size(474, 636)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
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
		changedue = amountgiven - amountdue
		self._label4.Text = str(changedue)
		# Amount of dollars needed to give back (if any)
		dollarvalue = int(changedue)
		self._label15.Text = str(dollarvalue)
		# How to get precise amount of change needed (And calculate and print precise coins)
		decimalchange = changedue - dollarvalue
		quartervalue = float(decimalchange) // .25
		quarterliteralvalue = float(quartervalue) * .25
		# Remaining Change After Quarters
		rcaq = float(decimalchange) - float(quarterliteralvalue)
		self._label10.Text = str(quartervalue)
		dimevalue = float(rcaq) // .10
		self._label11.Text = str(dimevalue)
		dimeliteralvalue = float(dimevalue) * .10
		rcad = float(rcaq) - dimeliteralvalue
		nickelvalue = float(rcad) // .05
		self._label12.Text = str(nickelvalue)
		nickelliteralvalue = float(nickelvalue) * .05
		rcan = float(rcad) - nickelliteralvalue
		pennyvalue = float(rcan) // .01
		self._label13.Text = str(pennyvalue)
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._label15.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		pass