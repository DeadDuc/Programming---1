import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._sumlabel = System.Windows.Forms.Label()
		self._averagelabel = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.MenuBar
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(166, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(412, 46)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.MenuBar
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(166, 61)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(412, 46)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.SystemColors.MenuBar
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(166, 113)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(412, 46)
		self._textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.SystemColors.MenuBar
		self._textBox4.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(166, 165)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(412, 46)
		self._textBox4.TabIndex = 3
		# 
		# sumlabel
		# 
		self._sumlabel.BackColor = System.Drawing.SystemColors.MenuBar
		self._sumlabel.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._sumlabel.Location = System.Drawing.Point(166, 224)
		self._sumlabel.Name = "sumlabel"
		self._sumlabel.Size = System.Drawing.Size(412, 50)
		self._sumlabel.TabIndex = 4
		self._sumlabel.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# averagelabel
		# 
		self._averagelabel.BackColor = System.Drawing.SystemColors.MenuBar
		self._averagelabel.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._averagelabel.Location = System.Drawing.Point(166, 286)
		self._averagelabel.Name = "averagelabel"
		self._averagelabel.Size = System.Drawing.Size(412, 50)
		self._averagelabel.TabIndex = 5
		self._averagelabel.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 22)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(125, 29)
		self._label3.TabIndex = 6
		self._label3.Text = "First Number"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 78)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 21)
		self._label1.TabIndex = 7
		self._label1.Text = "Second Number"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 126)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(125, 29)
		self._label2.TabIndex = 8
		self._label2.Text = "Third Number"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 178)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(125, 29)
		self._label4.TabIndex = 9
		self._label4.Text = "Fourth Number"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 371)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(218, 62)
		self._button1.TabIndex = 10
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(434, 371)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(144, 62)
		self._button2.TabIndex = 11
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(237, 371)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(191, 62)
		self._button3.TabIndex = 12
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(13, 226)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(147, 48)
		self._label5.TabIndex = 13
		self._label5.Text = "Sum"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(13, 288)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(147, 48)
		self._label6.TabIndex = 14
		self._label6.Text = "Average"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.InactiveCaption
		self.ClientSize = System.Drawing.Size(590, 445)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._averagelabel)
		self.Controls.Add(self._sumlabel)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		Application.Exit()
		pass

	def Button1Click(self, sender, e):
		first = int(self._textBox1.Text)
		second = int(self._textBox2.Text)
		third = int(self._textBox3.Text)
		fourth = int(self._textBox4.Text)
		s = first + second + third + fourth
		self._sumlabel.Text = str(s)
		average = s / 4
		self._averagelabel.Text = str(average)
		pass

	def Button3Click(self, sender, e):
		self._sumlabel.Text = ""
		self._averagelabel.Text = ""
		pass