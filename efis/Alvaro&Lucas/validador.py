from wx import *
class MyValidator(Validator):
    def __init__(self):
        Validator.__init__(self)
        self.Bind(EVT_CHAR, self.OnChar)

    def Clone(self):
        return MyValidator()

    def OnChar(self, event):
        digitos = "0123456789."
        key = event.GetKeyCode()
        if key == WXK_TAB or key == WXK_BACK or chr(key) in digitos:
            event.Skip()
        return