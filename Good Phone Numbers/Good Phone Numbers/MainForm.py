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
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(847, 22)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 31)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(847, 24)
		self._label2.TabIndex = 1
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(12, 55)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(847, 25)
		self._label3.TabIndex = 2
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(12, 80)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(847, 23)
		self._label4.TabIndex = 3
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(12, 107)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(847, 21)
		self._label5.TabIndex = 4
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 149)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(290, 160)
		self._button1.TabIndex = 5
		self._button1.Text = "Show Phone Numbers"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(308, 149)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(243, 160)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(557, 149)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(302, 160)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(871, 321)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Good Phone Numbers"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Italian House - (608)-754-2226"
		self._label2.Text = "Milwaukee Grill - (608)-754-1919"
		self._label3.Text = "Layne's - (608)-563-0397"
		self._label4.Text = "El Neno Tacos & Tortas - (608)-563-1513)"
		self._label5.Text = "San Miguel De Allende - (608)-352-7072"
		pass

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass