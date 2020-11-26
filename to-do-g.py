# Lista de tareas con GridBagSizer
from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, title='Tareas para hacer')
        p = Panel(f)
        s = GridBagSizer(5, 5)
        derecha = ALIGN_RIGHT
        listaTareas = [('Trabajo','Hablar con Pepe'), ('Estudio','EFI de Lengua'),('Trabajo','Pagar la luz')]
        id = 1000
        fi = -1
        for t in listaTareas:
            id += 1
            co = 0
            fi += 1
            etiqueta = StaticText(p, -1, t[0])
            tarea = StaticText(p, -1, t[1])
            cb = CheckBox(p, id)
            s.Add(etiqueta, (fi, co), DefaultSpan, TOP, 5)
            co += 1
            s.Add(tarea, (fi, co), DefaultSpan, TOP|LEFT, 5)
            co += 1
            s.Add(cb, (fi, co))
            cb.Bind(EVT_CHECKBOX, self.evtCheckBox)
        p.SetSizerAndFit(s)
        f.Show()
        return True

    def evtCheckBox(self, event):
        id = event.GetId()
        print(id)

app = MyApp()
app.MainLoop()
