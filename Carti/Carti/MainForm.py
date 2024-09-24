import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("Carti.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Transparent
		self._label1.Font = System.Drawing.Font("Old English Text MT", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(195, 302)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(445, 53)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(235, 31)
		self._button1.TabIndex = 1
		self._button1.Text = "Lyric 1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(445, 90)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(235, 31)
		self._button2.TabIndex = 2
		self._button2.Text = "Lyric 2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(445, 127)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(235, 32)
		self._button3.TabIndex = 3
		self._button3.Text = "Lyric 3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(445, 166)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(235, 31)
		self._button4.TabIndex = 4
		self._button4.Text = "Lyric 4"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(12, 516)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(33, 20)
		self._button5.TabIndex = 5
		self._button5.Text = "Exit"
		self._button5.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.White
		self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
		self.ClientSize = System.Drawing.Size(692, 548)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Carti"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Yeah Yeah you came back and you failed"
		pass

	def Button2Click(self, sender, e):
		self._label1.Text = "Second place can't be in my face oh nah"
		pass

	def Button3Click(self, sender, e):
		self._label1.Text = "Deep pockets they think im rockin Chanel"
		pass

	def Button4Click(self, sender, e):
		self._label1.Text = "Fat wallet lil bih you know I got here"
		pass