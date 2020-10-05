# Importing the Libraries
import win32com.client
import sys
import subprocess
import time


# This function will Login to SAP from the SAP Logon window

def saplogin():

    try:

        path = r"C:\Program Files (x86)\SAP\FrontEnd\SapGui\saplogon.exe"
        subprocess.Popen(path)
        time.sleep(10)

        SapGuiAuto = win32com.client.GetObject('SAPGUI')
        if not type(SapGuiAuto) == win32com.client.CDispatch:
            return

        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
            return
        connection = application.OpenConnection("073 : SAP R/3 CAMEL_iImaging - Production MBP", True)

        if not type(connection) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
            return

        session = connection.Children(0)
        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return

        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = "310295192"
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "iwff$#2352FHIE88"
        session.findById("wnd[0]").sendVKey(0)

    except:
        print(sys.exc_info()[0])

    finally:
        session = None
        connection = None
        application = None
        SapGuiAuto = None


saplogin()
