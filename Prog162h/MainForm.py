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
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(372, 43)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Number of Guests:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(13, 80)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(372, 43)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter Number of Chairs:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(161, 160)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(224, 43)
		self._label3.TabIndex = 2
		self._label3.Text = "Permutations:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(117, 221)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(268, 43)
		self._label4.TabIndex = 3
		self._label4.Text = "Guests Standing:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(391, 10)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(334, 46)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(391, 77)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(334, 46)
		self._textBox2.TabIndex = 5
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Black
		self._label5.Location = System.Drawing.Point(391, 160)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(334, 43)
		self._label5.TabIndex = 6
		self._label5.Text = "label5"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Black
		self._label6.Location = System.Drawing.Point(391, 220)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(334, 43)
		self._label6.TabIndex = 7
		self._label6.Text = "label6"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 280)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(261, 45)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(280, 280)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(221, 45)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(507, 279)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(218, 45)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(737, 337)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog162h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text   = ""
		self._label6.Text   = ""
		pass

	def Button1Click(self, sender, e):
		guests = self._textBox1.Text
		chairs = self._textBox2.Text
		var1  = float(guests) - 1
		var2  = float(guests) - 2
		var3  = float(guests) - 3
		var4  = float(guests) - 4
		var5  = float(guests) - 5
		var6  = float(guests) - 6
		var7  = float(guests) - 7
		var8  = float(guests) - 8
		var9  = 
		var10 = 
		var11 = 
		var12 = 
		var13 = 
		var14 = 
		var15 = 
		var16 = 
		var17 = 
		var18 = 
		var19 = 
		var20 = 
		
		pass