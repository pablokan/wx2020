# Lista de tareas con BoxSizers anidados
from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        p = Panel(f)
        st = StaticText(p, -1, "Tareas para hacer")
        derecha = ALIGN_RIGHT
        listaTareas = ['Comprar la leche', 'Pagar la luz', 'Ir al dentista']
        self.cbList = cbList = []
        id = 1000
        for tarea in listaTareas:
            cb = CheckBox(p, id, tarea, style=derecha)
            cb.Bind(EVT_CHECKBOX, self.evtCheckBox)
            cbList.append(cb)
            id += 1

        s = BoxSizer(VERTICAL)
        s.Add(st, 0, ALL, 5)
        for c in cbList:
            s.Add(c, 0, ALL|ALIGN_RIGHT, 5)
        p.SetSizer(s)
        f.Show()
        return True

    def evtCheckBox(self, event):
        id = event.GetId()
        print(id)

app = MyApp()
app.MainLoop()
