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
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 209)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(205, 62)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(223, 209)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(196, 62)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(425, 209)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(196, 62)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 38
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(608, 194)
		self._listBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveBorder
		self.ClientSize = System.Drawing.Size(633, 281)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog152a"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button1Click(self, sender, e):
		heading = "Number\t\tSum"
		self._listBox1.Items.Add(heading)
		num = 0
#		3223
		finalsum = 15586428
		num      = int(3)
		num2     = int(3)
		for even in range(0, 3223+1):
			num += 3
			num2 = num + num2
			line = str(num) + "\t\t" + str(num2)
			self._listBox1.Items.Add(line)
			if num2 == finalsum:
				finalline = "The final sum of the multiples of 3, from 3 " "to 9669 is 15586428!"
				finalline2 = "to 9669 is 15586428!"
				self._listBox1.Items.Add(finalline)
				self._listBox1.Items.Add(finalline2)
				break				
