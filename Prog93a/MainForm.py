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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Plum
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label1.Location = System.Drawing.Point(12, 62)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(250, 43)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter kWh used:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Violet
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label2.Location = System.Drawing.Point(12, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(495, 43)
		self._label2.TabIndex = 1
		self._label2.Text = "The Electric Bill!"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(268, 61)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(238, 46)
		self._textBox1.TabIndex = 2
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Fuchsia
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label3.Location = System.Drawing.Point(12, 143)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(250, 43)
		self._label3.TabIndex = 3
		self._label3.Text = "Base Rate:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Fuchsia
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label4.Location = System.Drawing.Point(12, 195)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(250, 43)
		self._label4.TabIndex = 4
		self._label4.Text = "Surcharge:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Fuchsia
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label5.Location = System.Drawing.Point(12, 248)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(250, 43)
		self._label5.TabIndex = 5
		self._label5.Text = "City Tax:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Fuchsia
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label6.Location = System.Drawing.Point(12, 335)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(250, 43)
		self._label6.TabIndex = 6
		self._label6.Text = "Total Bill:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Fuchsia
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label7.Location = System.Drawing.Point(12, 395)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(250, 43)
		self._label7.TabIndex = 7
		self._label7.Text = "Late Bill:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkViolet
		self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label8.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label8.Location = System.Drawing.Point(268, 143)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(239, 43)
		self._label8.TabIndex = 8
		self._label8.Text = "Label8"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkViolet
		self._label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label9.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label9.Location = System.Drawing.Point(268, 195)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(239, 43)
		self._label9.TabIndex = 9
		self._label9.Text = "Label9"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.DarkViolet
		self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label10.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label10.Location = System.Drawing.Point(267, 248)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(239, 43)
		self._label10.TabIndex = 10
		self._label10.Text = "Label10"
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.MediumOrchid
		self._label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label11.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label11.Location = System.Drawing.Point(268, 335)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(239, 43)
		self._label11.TabIndex = 11
		self._label11.Text = "Label11"
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.MediumOrchid
		self._label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label12.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label12.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label12.Location = System.Drawing.Point(268, 395)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(239, 43)
		self._label12.TabIndex = 12
		self._label12.Text = "Label12"
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 441)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(250, 46)
		self._button1.TabIndex = 13
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(268, 441)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(122, 46)
		self._button2.TabIndex = 14
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(396, 441)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(110, 46)
		self._button3.TabIndex = 15
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Orchid
		self.ClientSize = System.Drawing.Size(519, 493)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
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
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		# Collecting kWh and turning number into  a float
		kwh = float(self._textBox1.Text)
		# Calculating base rate
		prebaserate = float(kwh) * 0.0475
		baserate = round(prebaserate, 2)
		# Printing base rate
		self._label8.Text = "$" + str(baserate)
		# Calculating surcharge
		presurcharge = float(baserate) * .1
		surcharge = round(presurcharge, 2)
		# Printing surcharge
		self._label9.Text = "$" + str(surcharge)
		# Calculating city tax
		pretax = float(baserate) * .03
		tax = round(pretax, 2)
		# Printing city tax
		self._label10.Text = "$" + str(tax)
		# Calculating total bill
		totalbill = float(baserate) + float(surcharge) + float(tax)
		# Printing total bill
		self._label11.Text = "$" + str(totalbill)
		# Calculating late fee
		prelatefee = float(totalbill) * .04
		latefee = round(prelatefee, 2)
		latebill = float(totalbill) + float(latefee)
		# Printing late fee
		self._label12.Text = "$" + str(latebill)
		pass

	def Button2Click(self, sender, e):
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._textBox1.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass