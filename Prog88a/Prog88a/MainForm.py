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
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label17 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label1.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(10, 74)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(172, 39)
		self._label1.TabIndex = 0
		self._label1.Text = "Number 1:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label2.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(10, 124)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(172, 39)
		self._label2.TabIndex = 1
		self._label2.Text = "Number 2:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label3.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(10, 196)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(172, 39)
		self._label3.TabIndex = 2
		self._label3.Text = "Sum:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label4.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(10, 235)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(172, 39)
		self._label4.TabIndex = 3
		self._label4.Text = "Difference:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label5.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(10, 274)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(172, 39)
		self._label5.TabIndex = 4
		self._label5.Text = "Product:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightGreen
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label6.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(188, 196)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(316, 39)
		self._label6.TabIndex = 5
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label7.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(10, 430)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(172, 39)
		self._label7.TabIndex = 6
		self._label7.Text = "Minumum:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label8.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label8.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(10, 391)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(172, 39)
		self._label8.TabIndex = 7
		self._label8.Text = "Maximum:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label8.Click += self.Label8Click
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label9.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label9.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(10, 352)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(172, 39)
		self._label9.TabIndex = 8
		self._label9.Text = "Distance:"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label10.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label10.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(10, 313)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(172, 39)
		self._label10.TabIndex = 9
		self._label10.Text = "Average:"
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.LightGreen
		self._label11.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label11.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(188, 235)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(316, 39)
		self._label11.TabIndex = 10
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.LightGreen
		self._label12.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label12.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label12.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(188, 274)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(316, 39)
		self._label12.TabIndex = 11
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.LightGreen
		self._label13.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label13.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label13.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(188, 313)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(316, 39)
		self._label13.TabIndex = 12
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.LightGreen
		self._label14.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label14.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label14.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(188, 352)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(316, 39)
		self._label14.TabIndex = 13
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.LightGreen
		self._label15.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label15.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label15.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(188, 391)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(316, 39)
		self._label15.TabIndex = 14
		self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.LightGreen
		self._label16.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label16.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label16.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(188, 430)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(316, 39)
		self._label16.TabIndex = 15
		self._label16.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(188, 73)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(315, 40)
		self._textBox1.TabIndex = 16
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(188, 120)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(315, 40)
		self._textBox2.TabIndex = 17
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LawnGreen
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(10, 473)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(225, 80)
		self._button1.TabIndex = 18
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LawnGreen
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(241, 473)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(137, 80)
		self._button2.TabIndex = 19
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LawnGreen
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(384, 473)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(119, 80)
		self._button3.TabIndex = 20
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label17
		# 
		self._label17.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label17.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label17.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label17.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label17.Location = System.Drawing.Point(12, 9)
		self._label17.Name = "label17"
		self._label17.Size = System.Drawing.Size(491, 61)
		self._label17.TabIndex = 21
		self._label17.Text = "Magic Calculator"
		self._label17.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.ForestGreen
		self.ClientSize = System.Drawing.Size(517, 565)
		self.Controls.Add(self._label17)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
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
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label8Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		self._label6.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""
		self._label15.Text = ""
		self._label16.Text = ""
		self._textBox2.Text = ""
		self._textBox1.Text = ""
		pass

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		Dif = num1 - num2
		product = num1 * num2
		average = (num1 + num2)/2
		absolutevalue = abs(Dif)
		max = 0
		min = 0
		if num1 >= num2:
			Max = num1
		else: # means otherwise essentially
			Max = num2
		if Max == num1: # "==" means same so if max is the same as num1
			Min = num2
		else:
			Min = num1
		self._label6.Text = str(Sum)
		self._label11.Text = str(Dif)
		self._label12.Text = str(product)
		self._label13.Text = str(average)
		self._label14.Text = str(absolutevalue)
		self._label15.Text = str(Min)
		self._label16.Text = str(Max)

		
		