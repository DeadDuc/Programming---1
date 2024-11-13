import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 19
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(927, 384)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 415)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(305, 81)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(324, 415)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(305, 81)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(635, 415)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(305, 81)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(949, 508)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Prog122i"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button1Click(self, sender, e):
		heading = "Number\t\tNegative Number\tCube Root\tNegative Cube Root\t\tCubed\t\tNegative Cubed"
		self._listBox1.Items.Add(heading)
		for num in range(1, 27-1):
			nnum = num * -1
			pcube = num**3
			pcbrt = num**(1.0/3.0)
			ncbrt = abs(pcbrt) * -1
			ncube = ((nnum**3) * -1) * -1
			line = str(round(nnum, 2)) + "\t\t" + str(round(num, 2)) + "\t\t" + str(round(ncbrt, 2)) + "\t\t" + str(round(pcbrt, 2)) + "\t\t\t" + str(round(ncube, 2)) + "\t\t" + str(round(pcube, 2))
			self._listBox1.Items.Add(line)
			pass