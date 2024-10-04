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
		self._exitbutton = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Transparent
		self._label1.Font = System.Drawing.Font("Engravers MT", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(195, 302)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(445, 53)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(235, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Lyric 1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(445, 82)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(235, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Lyric 2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(445, 111)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(235, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "Lyric 3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(445, 140)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(235, 23)
		self._button4.TabIndex = 4
		self._button4.Text = "Lyric 4"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# exitbutton
		# 
		self._exitbutton.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._exitbutton.Location = System.Drawing.Point(12, 516)
		self._exitbutton.Name = "exitbutton"
		self._exitbutton.Size = System.Drawing.Size(57, 20)
		self._exitbutton.TabIndex = 5
		self._exitbutton.Text = "Exit"
		self._exitbutton.UseVisualStyleBackColor = True
		self._exitbutton.Click += self.Button5Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(248, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(189, 20)
		self._textBox1.TabIndex = 6
		self._textBox1.Text = "2024 - Playboi Carti"
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# button5
		# 
		self._button5.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(445, 169)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(235, 23)
		self._button5.TabIndex = 7
		self._button5.Text = "Lyric 5"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button6Click
		# 
		# button6
		# 
		self._button6.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(445, 199)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(235, 23)
		self._button6.TabIndex = 8
		self._button6.Text = "Lyric 6"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button7Click
		# 
		# button7
		# 
		self._button7.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(445, 229)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(235, 23)
		self._button7.TabIndex = 9
		self._button7.Text = "Lyric 7"
		self._button7.UseVisualStyleBackColor = True
		self._button7.Click += self.Button8Click
		# 
		# button8
		# 
		self._button8.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(445, 259)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(235, 23)
		self._button8.TabIndex = 10
		self._button8.Text = "Lyric 8"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.Font = System.Drawing.Font("Engravers MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(445, 287)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(235, 23)
		self._button9.TabIndex = 11
		self._button9.Text = "Lyric 9"
		self._button9.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.White
		self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
		self.ClientSize = System.Drawing.Size(692, 548)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._exitbutton)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Carti"
		self.ResumeLayout(False)
		self.PerformLayout()


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

	def exitbuttonClick(self, sender, e):
		Application.Exit()
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def Button5Click(self, sender, e):
		self._label1.Text = "Out of pocket with yo bih Chanel"
		pass

	def Button7Click(self, sender, e):
		pass

	def Button6Click(self, sender, e):
		pass

	def Button8Click(self, sender, e):
		pass