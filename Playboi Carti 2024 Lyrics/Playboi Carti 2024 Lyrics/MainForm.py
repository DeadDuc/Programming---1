import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("Playboi_Carti_2024_Lyrics.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(673, 148)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 474)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(173, 105)
		self._button1.TabIndex = 1
		self._button1.Text = "Lyric 1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(494, 474)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(191, 105)
		self._button2.TabIndex = 2
		self._button2.Text = "Lyric 2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
		self.ClientSize = System.Drawing.Size(697, 591)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Playboi Carti 2024 Lyrics"
		self.ResumeLayout(False)

		
	def Button1Click(self, sender, e):
		self._Label1.Text = "Yeah Yeah you came back nd u failed"
		pass

	def Button2Click(self, sender, e):
		self._Label1.Text = "Second place cant be in my face oh nah"
		pass