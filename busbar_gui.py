# -*- coding: utf-8 -*-
import wx
import mid_file
import time

result = []

class MyFrame1 ( wx.Frame ):
    def __init__(self):
        wx.Frame.__init__ (self,None, -1, u"BusBar仿真平台", size = wx.Size( 800,500 ))
        self.res = result

        gSizer1 = wx.GridSizer( 2, 2, 0, 0 )
        gSizer2 = wx.GridSizer( 4, 2, 0, 0 )
        #page1
        self.m_notebook1 = wx.Notebook(self, -1)
        self.m_panel1 = wx.Panel(self.m_notebook1, -1)

        self.m_l_label = wx.StaticText(self.m_panel1,-1, u"铜排长度(mm)")
        self.m_l_text = wx.TextCtrl(self.m_panel1,-1)

        self.m_w_label = wx.StaticText(self.m_panel1,-1, u"铜排宽度(mm)",)
        self.m_w_text = wx.TextCtrl(self.m_panel1,-1)

        self.m_d_label = wx.StaticText(self.m_panel1,-1, u"铜排厚度(mm)")
        self.m_d_text = wx.TextCtrl(self.m_panel1,-1)

        self.m_c_label = wx.StaticText(self.m_panel1,-1, u"接触区域长度(mm)")
        self.m_c_text = wx.TextCtrl(self.m_panel1,-1)

        gSizer2.Add(self.m_l_label, 0, wx.ALL, 5 )
        gSizer2.Add(self.m_l_text, 0, wx.ALL, 5 )
        gSizer2.Add(self.m_w_label, 0, wx.ALL, 5 )
        gSizer2.Add(self.m_w_text, 0, wx.ALL, 5 )
        gSizer2.Add(self.m_d_label, 0, wx.ALL, 5 )
        gSizer2.Add(self.m_d_text, 0, wx.ALL, 5 )
        gSizer2.Add(self.m_c_label, 0, wx.ALL, 5 )
        gSizer2.Add(self.m_c_text, 0, wx.ALL, 5 )

        self.m_panel1.SetSizer( gSizer2 )
        self.m_panel1.Layout()
        gSizer2.Fit(self.m_panel1 )
        self.m_notebook1.AddPage(self.m_panel1, u"几何参数")

        #page2
        self.m_panel2 = wx.Panel(self.m_notebook1,-1 )
        gSizer3 = wx.GridSizer( 5, 3, 0, 0 )

        self.m_class_label = wx.StaticText(self.m_panel2,-1, u"类别")
        self.m_cooper_label = wx.StaticText(self.m_panel2,-1, u"铜")
        self.m_steel_label = wx.StaticText(self.m_panel2,-1, u"钢")

        self.m_y_label = wx.StaticText(self.m_panel2,-1, u"杨氏模量",)
        self.m_y_text1 = wx.TextCtrl(self.m_panel2,-1)
        self.m_y_text2 = wx.TextCtrl(self.m_panel2,-1)

        self.m_p_label = wx.StaticText(self.m_panel2,-1, u"泊松比")
        self.m_p_text1 = wx.TextCtrl(self.m_panel2,-1)
        self.m_p_text2 = wx.TextCtrl(self.m_panel2,-1)

        self.m_con_label = wx.StaticText(self.m_panel2,-1, u"电导率")
        self.m_con_text1 = wx.TextCtrl(self.m_panel2,-1)
        self.m_con_text2 = wx.TextCtrl(self.m_panel2,-1)

        self.m_tcon_label = wx.StaticText(self.m_panel2,-1, u"热导率")
        self.m_tcon_text1 = wx.TextCtrl(self.m_panel2,-1)
        self.m_tcon_text2 = wx.TextCtrl(self.m_panel2,-1)

        gSizer3.Add(self.m_class_label, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_cooper_label, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_steel_label, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_y_label, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_y_text1, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_y_text2, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_p_label, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_p_text1, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_p_text2, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_con_label, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_con_text1, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_con_text2, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_tcon_label, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_tcon_text1, 0, wx.ALL, 5 )
        gSizer3.Add(self.m_tcon_text2, 0, wx.ALL, 5 )

        self.m_panel2.SetSizer( gSizer3 )
        self.m_panel2.Layout()
        gSizer3.Fit(self.m_panel2 )
        self.m_notebook1.AddPage(self.m_panel2, u"材料参数" )

        #page3
        self.m_panel3 = wx.Panel(self.m_notebook1,-1 )
        gSizer4 = wx.GridSizer( 4, 2, 0, 0 )


        self.m_t_label = wx.StaticText( self.m_panel3,-1, u"环境温度(℃)" )
        self.m_t_text = wx.TextCtrl(self.m_panel3,-1)

        self.m_r_label = wx.StaticText( self.m_panel3,-1, u"接触电阻(Ω)")
        self.m_r_text = wx.TextCtrl( self.m_panel3,-1)

        self.m_i_label = wx.StaticText( self.m_panel3,-1, u"电流(A)")
        self.m_i_text = wx.TextCtrl( self.m_panel3,-1)

        self.m_film_label = wx.StaticText( self.m_panel3,-1, u"对流换热系数")
        self.m_film_text = wx.TextCtrl( self.m_panel3,-1)

        gSizer4.Add(self.m_t_label, 0, wx.ALL, 5 )
        gSizer4.Add(self.m_t_text, 0, wx.ALL, 5 )
        gSizer4.Add(self.m_r_label, 0, wx.ALL, 5 )
        gSizer4.Add(self.m_r_text, 0, wx.ALL, 5 )
        gSizer4.Add(self.m_i_label, 0, wx.ALL, 5 )
        gSizer4.Add( self.m_i_text, 0, wx.ALL, 5 )
        gSizer4.Add( self.m_film_label, 0, wx.ALL, 5 )
        gSizer4.Add( self.m_film_text, 0, wx.ALL, 5 )


        self.m_panel3.SetSizer( gSizer4 )
        self.m_panel3.Layout()
        gSizer4.Fit( self.m_panel3 )
        self.m_notebook1.AddPage( self.m_panel3, u"热电分析条件")

        #page4
        self.m_panel4 = wx.Panel(self.m_notebook1,-1,)
        gSizer5 = wx.GridSizer( 2, 2, 0, 0 )


        self.m_force_label = wx.StaticText(self.m_panel4,-1, u"预紧力(N)")
        self.m_force_text = wx.TextCtrl(self.m_panel4,-1)

        self.m_ff_label = wx.StaticText(self.m_panel4,-1, u"摩擦系数")
        self.m_ff_text = wx.TextCtrl(self.m_panel4,-1)

        gSizer5.Add( self.m_force_label, 0, wx.ALL, 5 )
        gSizer5.Add(self.m_force_text, 0, wx.ALL, 5 )
        gSizer5.Add( self.m_ff_label, 0, wx.ALL, 5 )
        gSizer5.Add( self.m_ff_text, 0, wx.ALL, 5 )


        self.m_panel4.SetSizer( gSizer5 )
        self.m_panel4.Layout()
        gSizer5.Fit(self.m_panel4 )
        self.m_notebook1.AddPage(self.m_panel4, u"接触分析条件" )
        gSizer1.Add(self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self,-1,)
        bSizer = wx.BoxSizer( wx.VERTICAL )

        m_bitmap1 = wx.StaticBitmap(self.m_panel5, -1)
        bSizer.Add(m_bitmap1, 0, wx.ALL, 5 )

        self.m_panel5.SetSizer( bSizer )
        self.m_panel5.Layout()
        bSizer.Fit(self.m_panel5 )
        gSizer1.Add(self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )



        self.m_panel6 = wx.Panel( self,-1,)
        gSizer7 = wx.GridSizer( 4, 2, 0, 0 )


        self.m_nut_label = wx.StaticText( self.m_panel6, -1, u"螺栓个数")
        self.m_nut_text = wx.TextCtrl( self.m_panel6, -1)

        self.m_bolt_label = wx.StaticText( self.m_panel6,-1, u"螺栓型号")
        self.m_comboBox2Choices = [ u"M5", u"M6", u"M8" ]
        self.m_comboBox2 = wx.ComboBox( self.m_panel6, -1, u"M4", wx.DefaultPosition, wx.DefaultSize, self.m_comboBox2Choices, 0 )

        self.m_hole_label = wx.StaticText( self.m_panel6,-1, u"开孔位置")
        self.m_hole_text = wx.TextCtrl( self.m_panel6, -1)

        self.m_button_t = wx.Button( self.m_panel6, -1, u"热电仿真分析")
        self.m_button_c = wx.Button( self.m_panel6, -1, u"接触仿真分析" )

        gSizer7.Add( self.m_nut_label, 0, wx.ALL, 5 )
        gSizer7.Add( self.m_nut_text, 0, wx.ALL, 5 )
        gSizer7.Add( self.m_bolt_label, 0, wx.ALL, 5 )
        gSizer7.Add(self.m_comboBox2, 0, wx.ALL, 5 )
        gSizer7.Add(self.m_hole_label, 0, wx.ALL, 5 )
        gSizer7.Add( self.m_hole_text, 0, wx.ALL, 5 )
        gSizer7.Add( self.m_button_t, 0, wx.ALL, 5 )
        gSizer7.Add(self.m_button_c, 0, wx.ALL, 5 )

        self.m_panel6.SetSizer( gSizer7 )
        self.m_panel6.Layout()
        gSizer7.Fit( self.m_panel6 )
        gSizer1.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )



        self.m_panel7 = wx.Panel( self, -1)
        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        #m_bitmap2 = wx.StaticBitmap( m_panel7, -1, wx.Bitmap( u"捕获1.PNG", wx.BITMAP_TYPE_ANY ))
        self.m_bitmap2 = wx.StaticBitmap( self.m_panel7, -1)
        bSizer7.Add( self.m_bitmap2, 0, wx.ALL, 5 )

        self.m_panel7.SetSizer( bSizer7 )
        self.m_panel7.Layout()
        bSizer7.Fit( self.m_panel7 )
        gSizer1.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( gSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )

        self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
        self.Bind(wx.EVT_BUTTON,self.t_e_analysis,self.m_button_t)
    def t_e_analysis( self, event ):
        self.res.append(self.m_l_text.GetValue())
        self.res.append(self.m_w_text.GetValue())
        self.res.append(self.m_d_text.GetValue())
        self.res.append(self.m_c_text.GetValue())
        self.res.append(self.m_y_text1.GetValue())
        self.res.append(self.m_y_text2.GetValue())
        self.res.append(self.m_p_text1.GetValue())
        self.res.append(self.m_p_text2.GetValue())
        self.res.append(self.m_con_text1.GetValue())
        self.res.append(self.m_con_text2.GetValue())
        self.res.append(self.m_tcon_text1.GetValue())
        self.res.append(self.m_tcon_text2.GetValue())
        self.res.append(self.m_t_text.GetValue())
        self.res.append(self.m_r_text.GetValue())
        self.res.append(self.m_i_text.GetValue())
        self.res.append(self.m_film_text.GetValue())
        self.res.append(self.m_nut_text.GetValue())
        self.res.append(self.m_comboBox2.GetValue())
        #center = eval()
        self.res.append(self.m_hole_text.GetValue())
        #args = ['180','60','4','60','108000000000.0','193000000000.0','0.34','0.31','0.399','0.0485',
        # '59700.0','1390.0','25','1','100','5','1','M4',(0,0)]
        time.sleep(2)
        #cmd = 'abaqus cae script=d:\py_test\Busbar.py'
        #os.system(cmd)
        with open ('D:\py_test\data.txt', 'w') as f:
            for i in self.res:
                f.write(i+'\n')
        mid_file.main()
        event.Skip()
    def OnCloseWindow(self,event):
        self.Destroy()
def set_args():
    return result

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame1()
    frame.Show(True)
    app.MainLoop()
