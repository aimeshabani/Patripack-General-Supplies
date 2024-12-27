
import os.path
import threading
from kivy.uix.button import Button , ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.textinput import TextInput
import json ,time
from kivy.uix.carousel import Carousel
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import ftplib,sys
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, SwapTransition, FallOutTransition
from kivy.graphics import Rectangle,Color
from random import randint
from kivy.uix.image import AsyncImage
from kivy.uix.scatter import Scatter
from kivy.utils import platform
from kivy.uix.filechooser import FileChooserListView, FileChooserIconView
from kivy.uix.behaviors import DragBehavior
import requests



SD0="/storage/emulated/0/Documents/"
if platform=="android":
    if not os.path.isfile("/storage/emulated/0/Documents/name.t"):   # simu ya innocent iliubali kama name.t iko lakini haiku write name ku ile dir.. so , nitapima u write njo nikubali
        from android.permissions import request_permissions, Permission

        request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

        from android.storage import primary_external_storage_path


        primary_ext_storage = primary_external_storage_path()
        directory = "Documents/"
        parent_dir = primary_ext_storage
        SD0 = os.path.join(parent_dir, directory)
        if not os.path.isdir(SD0):
            os.mkdir(SD0)

        try:
            pth = SD0 + "test.t"
            open(pth, "w").write("test")
        except:
            SD0 = "./"
            open(SD0 + 'test.t', "w").write("test.t")

    else:
        try:
            pth=SD0+"test.t"
            open(pth, "w").write("test")
        except:
            try:
                from android.permissions import request_permissions, Permission

                request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

                from android.storage import primary_external_storage_path
                primary_ext_storage = primary_external_storage_path()
                directory = "Documents/"
                parent_dir = primary_ext_storage
                SD0 = os.path.join(parent_dir, directory)
                if not os.path.exists(SD0):
                    os.makedirs(SD0)
                pth = SD0 + "test.t"
                open(pth, "w").write("test")
            except:
                SD0="./"
                open(SD0+'test.t', "w").write("test.t")
    # from jnius import autoclass
    # Env=autoclass('android.os.Environment')
    # # SD0=Env.getExternalStorageDirectory().getAbsolutePath()+"/emulated/0"
    # SD0="/storage/emulated/0"
else:
    Window.size=(900,500)
    if platform=="linux":
        hd = os.path.expanduser("~/")
        if not os.path.exists(hd + "Documents"):
            os.makedirs(hd + "Documents")
        SD0 = hd + "Documents/"
        # Window.size = (360, 680)
    else:
        hd=os.path.expanduser("~\\")
        if not os.path.exists(hd+"Documents"):
           os.makedirs(hd+"Documents")
        SD0=os.path.expanduser(hd+"Documents\\")
        # Window.size = (360, 680)
import logging

logging.basicConfig(filename=SD0+"kivy_logs.log", level=logging.DEBUG)
logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


b_screen=None
sig=2
sums=[]

# ips=[
#     "195.35.23.244","127.0.0.1","192.168.43.1","192.168.8.100", "192.168.8.101", "192.168.8.102",
#     "192.168.8.103","192.168.8.104","192.168.8.105","192.168.8.106","192.168.8.107"
#      ]
# for ii in range(100):
#     ips.append("192.168.43."+str(ii))

# ips=["195.35.23.244"]
ips=["195.35.23.244"]
status="offline"
DEBTS=[]


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Window.softinput_mode="below_target"
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
try:
    IP=open(SD0+"ip.ip","r").read()
except:
    # IP="195.35.23.244"
    IP="195.35.23.244"

port=2121
srv="aime shabani"
pwd="12435687"
# FTP="FTP/FTP/"
FTP="root/FTP/FTP/"
spin_blocker=1


def shab(l, n,ind1=None,ind2=None):
    try:
        c = l[n]
        if ind1 !=None and ind2 != None:
            return l[n][ind1][ind2]
        if ind1!=None and ind2 is None:
            return l[n][ind1]
    except:
        return ""

def inn(l, n,i):
    try:
        c = l[n]
        return l[n][i]
    except:
        return ""

def outt(l, n,i):
    try:
        c = l[n]
        return l[n][i]
    except:
        return ""

def loutt(lst, n,i,i2):

    try:
        c = lst[n]
        if i==0:
            return lst[n][i]
        else:
            return lst[n][i][i2]
    except:
        return ""

def lin(l, n,i):
    try:
        c = l[n]
        return l[n][i]
    except:
        return ""

def fnam(d):
    if platform=="android":
        p = "/"  # PTH()
    else:
        p="\\"
    x = ""
    for i in range(len(d)):
        if d[-1] == p:
            break
        else:
            x = d[-1] + x
            d = d[:-1]

    return x

def milli(st):
    I=float(st) if st not in [""," ","None",None] else 0.0
    try:
        return str( "{:,}".format(I) )  # but this is not universal
    except:
        try:
            return str("{:,}".format(I))  # but this is not universal
        except:
            return  "0"
    # s=str(st)
    # if len(s) <= 1:
    #     return "0"
    # r = ""
    # f = ""
    # if "." in s:
    #     f = s[s.index("."):]
    #     s = s[:s.index(".")]
    #
    # for i in range(len(s)):
    #     if len(s) <= 3:
    #         r = s + r
    #         return r + f
    #     else:
    #         # r += "," + s[-3:]            #    1,567,234
    #         r = "," + s[-3:] + r           #    1,234,567
    #         s = s[:-3]
    # if r[0]== ",":
    #     r=r[1:]
    # return r + f

class ImageButton(ButtonBehavior, AsyncImage):
    def on_press(self):

        tx=self.text
        TT=self.text.split("/")[-1]
        pg = GridLayout(cols=1, size_hint=(1.,1.))

        gsk = GridLayout(cols=1, size_hint=(1., .7))
        sk = Scatter(do_rotation=True, do_translation=True, do_scale=True,
                     scale=min(self.parent.width / self.width, self.parent.height / self.height))    #center=self.parent.center,
        im = AsyncImage(source=tx,size=(700,700))
        sk.add_widget(im)

        gsk.add_widget(sk)
        pg.add_widget(gsk)

        content_cancel = Button(text='Cancel', size_hint_y=None, height=60,background_color=(0,1,0,.2))

        pg.add_widget(content_cancel)

        popup2 = Popup(title=TT[:-4].replace("-"," "), size_hint=(1.,1.), content=pg,disabled=False)
        content_cancel.bind(on_release=popup2.dismiss)
        popup2.open()


class MyCarousel(Carousel):
    def on_index(self, instance,value):
        global sig
        sig+=1
        print("Current index : ",value)
        if sig >= 4 :
            pgs=Rep()
            Clock.schedule_once( pgs.change)

class DraggableButton(DragBehavior, Button):
    pass

gr,SB,bgr=None,None,None

class sm(ScreenManager):
    def __init__(self, **kwargs):
        super(sm, self).__init__(**kwargs)

class Rep(Screen):
    def __init__(self,**kwargs):
        super(Rep, self).__init__(**kwargs)
        open(SD0 + "t1", "w").write("test")
        Clock.schedule_once(self.choose)
        Clock.schedule_once(lambda x: threading.Thread(target=self.find_ip).start(), 1)



    def choose(self,x):
        Clock.unschedule(self.b_g1_anim)
        Clock.unschedule(self.g1_anim)
        lt=os.listdir("bg/")
        with self.canvas:
            Color(1,1,1,1)
            Rectangle(source="bg/"+lt[randint(0,len(lt)-1)],size=Window.size,pos=(0,0))
        spc=Window.size[1]  +100   #randint(1,2)

        self.g1=GridLayout(cols=2,spacing=spc, pos_hint={"center_x": .45, "center_y": .5},
                      size_hint=(None, None), size=(Window.size[0], Window.size[0]/1.8))

        self.g1.add_widget(Button(background_normal="r.png",background_down="k.png", on_release=self.call_rot))
        self.g1.add_widget(Button(background_normal="w.png",background_down="k.png",on_press=self._pre_ini))

        self.add_widget(self.g1)

        self.animat(self.g1,spc)

        Clock.schedule_interval(lambda x:threading.Thread(target=self.Bring_debt).start(),3)

    def Bring_debt(self):
        global DEBTS
        open(SD0 + "debt.txt", "w").write(str(DEBTS))
        TD = json.dumps({"main": "DEBTS","json": {"name":open(SD0+"name.t","r").read()} } )
        url = 'http://' + IP + ':8080/PGS/' + TD
        response = requests.get(url, timeout=4)

        if response.status_code == 200:
            status = 'online'
            DEBTS = response.json()["DEBTS"]
            json.dump( response.json(), open(SD0 + "debts.al", "w"))

        else:
            DEBTS = json.load(open(SD0 + "debts.al", "r"))["DEBTS"]

        open(SD0+"debt.txt","w").write(str(DEBTS))



    def animat(self,wid,spc):
        global WIDGET,SPC
        WIDGET,SPC=wid,spc
        Clock.schedule_interval(self.g1_anim,0.001)

    def g1_anim(self,x):
        global WIDGET,SPC
        WIDGET.spacing=SPC
        SPC-=25
        if SPC<=8 :
            Clock.unschedule(self.g1_anim)

    def b_animat(self,wid,spc):
        global DGET,SPAC
        DGET,SPAC=wid,spc
        Clock.schedule_interval(self.b_g1_anim,0.001)

    def b_g1_anim(self,x):
        global DGET,SPAC
        DGET.spacing=SPAC
        SPAC-=100
        if SPAC>=1000 :
            Clock.unschedule(self.b_g1_anim)

    def _pre_ini(self,w):
        global PPPP
        inp = TextInput(hint_text="Password", password=True,multiline=False)
        inp.bind(text=self._validated)
        inp.bind(on_text_validatin=self._validated)
        PPPP = Popup(title='This is to prevent data falsification', size_hint=(None, None),
                   size=(Window.size[0] - 300, Window.size[1] // 5),pos=(0, 10), content=inp, disabled=False)

        PPPP.open()
    def _validated(self,wd,tx=None):
        global PPPP
        if wd.text=="    a    ":
            PPPP.dismiss()
            Clock.schedule_once(self.pre_ini)

    def pre_ini(self,wgt):
        global gr, SB

        try:
            self.remove_widget(self.g1)
        except:
            pass
        try:
            x4 = open("w5.jpg", "rb").read()
            x5 = open(SD0 + "w5.jpg", "wb")
            x5.write(x4)
            x5.close()
        except:
            pass
        gr = GridLayout(cols=1,spacing=8, padding=15)        #Window.size[1] + 100
        # Calculate the center coordinates of the widget
        center_x = Window.size[0] / 2
        center_y = Window.size[1] / 2

        # Define the size and position of the Rectangle
        rect_width = Window.size[0]  # You can set the width and height as needed
        rect_height = Window.size[1]

        # Calculate the position of the Rectangle to center it
        rect_x = center_x - rect_width / 2
        rect_y = center_y - rect_height / 2

        lt = os.listdir("bg/")
        with gr.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(source="bg/"+lt[randint(0,len(lt)-1)], size=(Window.size[0], Window.size[1]), pos=(rect_x, rect_y))
        pth = SD0 + "name.t"
        if not os.path.isfile(pth):
            Clock.schedule_once(self.ver, 2)
        else:
            Clock.schedule_once(self.open)
        self.add_widget(gr)
        Window.bind(on_key_down=self.back)

    def back(self,modifier,keycode,a,b,c):

        if keycode==27 :
            pn.export_to_png("App.png")
            try:
                self.remove_widget(gr)
                Clock.schedule_once(self.choose)
            except:
                pass

            self.animat(self.g1, Window.size[1] + 100)
            return True


    def LOSGR(self):
        losgr = GridLayout(cols=2, row_default_height=80, size_hint=(None, None), size=(Window.size[0], 80 * 20 + 400),
                           row_force_default=True)
        BB1 = []

        if os.path.isfile(SD0 + time.strftime("%d-%B-%Y") + ".json"):
            D1 = json.load(open(SD0 + time.strftime("%d-%B-%Y") + ".json", "r"))
            BB1 = list(D1['LOSSES'].items())
            # BB1 = BB1[2:]

        cl1 = [(.3, 1, .6, .8), (1, .5, 1, .8)]
        s = 0
        CCnt = 2
        losgr.add_widget(Label(text=",", color=(1, 0, 1, 1)))
        losgr.add_widget(Label(text="."))
        losgr.add_widget(Label(text="'"))
        losgr.add_widget(Label(text="LOSSES ( PERTES )"))

        for x in range(20):
            x = cl1[s]
            losgr.add_widget(
                TextInput(hint_text="Why ?", text="" if lin(BB1, CCnt, 0) == "" else lin(BB1, CCnt, 0), multiline=True,
                          background_color=x))
            losgr.add_widget(
                TextInput(hint_text="Amount", text="" if lin(BB1, CCnt, 1) == "" else lin(BB1, CCnt, 1),
                          multiline=True,
                          background_color=x))
            if s == 0:
                s += 1
            else:
                s -= 1
            CCnt += 1
        return losgr

    def OUTGR(self):
        outgr = GridLayout(cols=2, row_default_height=80, size_hint=(None, None), size=(Window.size[0], 80 * 20 + 400),
                           row_force_default=True)
        BB_ = []

        if os.path.isfile(SD0 + time.strftime("%d-%B-%Y") + ".json"):
            D = json.load(open(SD0 + time.strftime("%d-%B-%Y") + ".json", "r"))
            BB_ = list(D['OUT'].items())
            # BB_ = BB_[2:]


        cl_ = [(1, 1, 0, .8), (1, .8, 1, .8)]
        s_ = 0
        CCnt_ = 2
        outgr.add_widget(Label(text=",", color=(1, 0, 1, 1)))
        outgr.add_widget(Label(text="."))
        outgr.add_widget(Label(text="'"))
        outgr.add_widget(Label(text="OUT ( SORTI )"))

        outgr.add_widget(TextInput(text="UMEME", readonly=True, background_color=(.8, .7, .4, .6)))
        outgr.add_widget(TextInput(hint_text="units", text=" " if outt(BB_, 0, 1) == "" else outt(BB_, 0, 1),
                                   background_color=(.4, .4, .8, .6)))
        outgr.add_widget(TextInput(text="Wifi", readonly=True, background_color=(.8, .7, .4, .6)))
        outgr.add_widget(TextInput(hint_text="MB", text=" " if outt(BB_, 1, 1) == "" else outt(BB_, 1, 1),
                                   background_color=(.4, .7, .8, .6)))

        for num in range(20):
            x_ = cl_[s_]
            outgr.add_widget(
                TextInput(hint_text="Reason", text="" if outt(BB_, CCnt_, 0) == "" else outt(BB_, CCnt_, 0),
                          multiline=True, background_color=x_))
            outgr.add_widget(
                TextInput(hint_text="Amount", text="" if (BB_, CCnt_, 1) == "" else outt(BB_, CCnt_, 1),
                          multiline=True,
                          background_color=x_))
            if s_ == 0:
                s_ += 1
            else:
                s_ -= 1
            CCnt_ += 1
        return outgr

    def INGR(self):
        ingr = GridLayout(cols=2, row_default_height=80, size_hint=(None, None), size=(Window.size[0], 80 * 20 + 400),
                          row_force_default=True)
        CC = []

        if os.path.isfile(SD0 + time.strftime("%d-%B-%Y") + ".json"):
            D = json.load(open(SD0 + time.strftime("%d-%B-%Y") + ".json", "r"))
            CC = list(D['IN'].items())
            # CC = CC[2:]

        cl2 = [(1, 0, .93, .8), (1, .75, 1, .8)]
        s2 = 0
        CNT = 2
        ingr.add_widget(Label(text=",", color=(1, 0, 1, 1)))
        ingr.add_widget(Label(text="."))
        ingr.add_widget(Label(text="'"))
        ingr.add_widget(Label(text="IN ( ENTREE )"))

        ingr.add_widget(TextInput(text="UMEME", readonly=True, background_color=(.8, .4, .2, .6)))
        ingr.add_widget(TextInput(hint_text="units", text=" " if inn(CC, 0, 1) == "" else inn(CC, 0, 1),
                                  background_color=(.2, .4, .8, .6)))
        ingr.add_widget(TextInput(text="Wifi", readonly=True, background_color=(.8, .4, .2, .6)))
        ingr.add_widget(TextInput(hint_text="MB", text=" " if inn(CC, 1, 1) == "" else inn(CC, 1, 1),
                                  background_color=(.2, .4, .8, .6)))
        for xx in range(20):
            xx = cl2[s2]
            ingr.add_widget(
                TextInput(hint_text="Reason", text=inn(CC, CNT, 0) if inn(CC, CNT, 0) != "" else "", multiline=True,
                          foreground_color=(0, 0, 0, 1), background_color=xx))
            ingr.add_widget(
                TextInput(hint_text="Amount", text=inn(CC, CNT, 1) if inn(CC, CNT, 1) != "" else "", multiline=True,
                          foreground_color=(0, 0, 0, 1), background_color=xx))
            if s2 == 0:
                s2 += 1
            else:
                s2 -= 1
            CNT += 1
        return ingr

    def LOUTGR(self):
        loutgr = GridLayout(cols=5,padding=15, row_default_height=80, size_hint=(None, None), size=(Window.size[0], 80 * 20 + 400),
                            row_force_default=True)
        BB2 = []

        if os.path.isfile(SD0 + time.strftime("%d-%B-%Y") + ".json"):
            D1 = json.load(open(SD0 + time.strftime("%d-%B-%Y") + ".json", "r"))
            BB2 = list(D1['LOAN_OUT'].items())
            # BB2 = BB2[2:]
        cl11 = [(1, .5, .3, .8), (1, .8, .2, .8)]
        s1 = 0
        CCnt1 = 0
        loutgr.add_widget(Label(text=",", color=(1, 0, 1, 1)))
        loutgr.add_widget(Label(text="."))
        loutgr.add_widget(Label(text="'"))
        loutgr.add_widget(Label(text="'"))
        loutgr.add_widget(Label(text="LOAN OUT ( EMPRUNT )"))

        vl = []
        for x in range(18, 76):
            vl.append(str(x))

        for x in range(20):
            x = cl11[s1]

            loutgr.add_widget(
                TextInput(hint_text="Name", text="" if loutt(BB2, CCnt1, 0,0) == "" else loutt(BB2, CCnt1, 0,0),
                          multiline=True, background_color=x, size_hint=(None, 1),size=(loutgr.size[0]/3,80)))

            loutgr.add_widget(
                TextInput(hint_text="Amount", text="" if loutt(BB2, CCnt1, 1,0) == "" else loutt(BB2, CCnt1, 1,0),
                          multiline=True, background_color=x, size_hint=(None,1),size=(loutgr.size[0]/4,80)))

            loutgr.add_widget(Spinner(text='Sex' if loutt(BB2, CCnt1, 1,1) == '' else loutt(BB2, CCnt1, 1,1),values=("M","F"),
                                      size_hint=(None,1),size=(loutgr.size[0]/7,80)))



            loutgr.add_widget(Spinner(text='Age' if loutt(BB2, CCnt1, 1,2) == '' else loutt(BB2, CCnt1, 1,2),
                                      values=tuple(vl), size_hint=(None,1),size=(loutgr.size[0]/7,80)))

            loutgr.add_widget(Spinner(text='Relation' if loutt(BB2, CCnt1, 1,3) == '' else loutt(BB2, CCnt1, 1,3),
                                      values=("Maried", "Single","Divorced","Widowed","S.P"),size_hint=(None,1),size=(loutgr.size[0]/5,80)))



            if s1 == 0:
                s1 += 1
            else:
                s1 -= 1
            CCnt1 += 1
        return loutgr

    def RQGR(self):
        rqgr = GridLayout(cols=3, spacing=2, row_default_height=100, size_hint=(.7, None), size=(Window.size[0], 100 * 20 + 200),
                          row_force_default=True)
        DD = []

        if os.path.isfile(SD0 + time.strftime("%d-%B-%Y") + ".json"):
            D = json.load(open(SD0 + time.strftime("%d-%B-%Y") + ".json", "r"))
            DD = list(D['REQ'].items())

        cl3 = [(1, 0, .93, .8), (1, .8, 1, .8)]
        s3 = 0
        rqgr.add_widget(Label(text="_"))
        rqgr.add_widget(Label(text="REQUESTS ( DEMANDE )", color=(1, 0, 1, 1), font_size=30))
        rqgr.add_widget(Label(text=""))
        rqgr.add_widget(Label(text="__"))
        rqgr.add_widget(Label(text=".."))
        rqgr.add_widget(Label(text="..."))

        xxx = Window.size[0]
        req = []
        cnt = 0

        for Xs in range(20):

            xx = cl3[s3]
            bt = Button(text="" if shab(DD, cnt, 1, 1) != "" else "...", background_normal=shab(DD, cnt, 1, 1),
                        color=(1, .8, 1, 1),
                        background_color=(1, 1, 1, 1) if shab(DD, cnt, 1, 1) != "" else (.4, 0, .5, 1),
                        on_press=self.load_medi, size_hint=(None, None), size=(120, 100))

            rqgr.add_widget(bt)
            req.append(bt)
            field1 = TextInput(hint_text="Need" + str(Xs + 1),
                               text=shab(DD, cnt, ind1=0) if shab(DD, cnt, ind1=0) != "" else "", multiline=True,
                               size_hint=(None, None),
                               size=((xxx-120) /2, 100),
                               foreground_color=(0, 0, 0, 1), background_color=xx)
            rqgr.add_widget(field1)
            req.append(field1)

            field2 = TextInput(hint_text="Amount" + str(Xs + 1),
                               text=shab(DD, cnt, ind1=1, ind2=0) if shab(DD, cnt, ind1=1, ind2=0) != "" else "",
                               size_hint=(None, None),
                               size=((xxx-120) /2, 100),
                               foreground_color=(0, 0, 0, 1), background_color=xx)
            rqgr.add_widget(field2)
            req.append(bt)
            cnt += 1
            if s3 == 0:
                s3 += 1
            else:
                s3 -= 1
        return rqgr

    def PAY(self):
        lingr = GridLayout(cols=2, row_default_height=80, size_hint=(None, None), size=(Window.size[0], Window.size[1]*2),
                           row_force_default=True)


        lingr.add_widget(Label(text=","))
        lingr.add_widget(Label(text="."))

        lingr.add_widget(Label(text="."))
        lingr.add_widget(Label(text="LOAN PAID ( PAIYEMENT )"))

        lingr.add_widget(Label(text="."))
        lingr.add_widget(Label(text="."))

        self.search=TextInput(hint_text="Search", multiline=True, background_color=(.3, 1, .6, .8))
        self.search.bind(text=self.Find)
        lingr.add_widget(self.search)
        lingr.add_widget(Label(text="."))


        self.select=Spinner(text="select name")
        lingr.add_widget(self.select)
        self.paid=TextInput(hint_text="Amount",multiline=True,background_color=(1, .5, 1, .8))
        self.paid.bind(text=self.intg)
        lingr.add_widget(self.paid)

        self.select_2 = Spinner(text="select name")
        lingr.add_widget(self.select_2)
        self._paid = TextInput(hint_text="Amount", multiline=True, background_color=(1, .5, 1, .8))
        self._paid.bind(text=self.intg)
        lingr.add_widget(self._paid)

        self._select_ = Spinner(text="select name")
        lingr.add_widget(self._select_)
        self._2paid = TextInput(hint_text="Amount", multiline=True, background_color=(1, .5, 1, .8))
        self._2paid.bind(text=self.intg)
        lingr.add_widget(self._2paid)

        self.select3 = Spinner(text="select name")
        lingr.add_widget(self.select3)
        self._paid2 = TextInput(hint_text="Amount", multiline=True, background_color=(1, .5, 1, .8))
        self._paid2.bind(text=self.intg)
        lingr.add_widget(self._paid2)



        return lingr

    def LINGR(self):
        lingr = GridLayout(cols=2, row_default_height=80, size_hint=(None, None), size=(Window.size[0], 80 * 20 + 400),
                           row_force_default=True)
        BB1 = []

        if os.path.isfile(SD0 + time.strftime("%d-%B-%Y") + ".json"):
            D1 = json.load(open(SD0 + time.strftime("%d-%B-%Y") + ".json", "r"))
            BB1 = list(D1['LOAN_IN'].items())
            # BB1 = BB1[2:]
        cl1 = [(.3, 1,.6, .8), (1, .5, 1, .8)]
        s = 0
        CCnt = 2
        lingr.add_widget(Label(text=",", color=(1, 0, 1, 1)))
        lingr.add_widget(Label(text="."))
        lingr.add_widget(Label(text="'"))
        lingr.add_widget(Label(text="LOAN PAID ( PAIYEMENT )"))

        for x in range(20):
            x = cl1[s]
            lingr.add_widget(
                TextInput(hint_text="Name", text="" if lin(BB1, CCnt, 0) == "" else lin(BB1, CCnt, 0), multiline=True,
                          background_color=x))
            lingr.add_widget(
                TextInput(hint_text="Amount", text="" if lin(BB1, CCnt, 1) == "" else lin(BB1, CCnt, 1),
                          multiline=True,
                          background_color=x))
            if s == 0:
                s += 1
            else:
                s -= 1
            CCnt += 1
        return lingr

    def Find(self,sp,tx):
        if len(DEBTS) == 0 :
            sp.background_color=(.6,0,0,1)
            return
        else:
            chs=[]
            for x in DEBTS:
                if tx.strip() in x or x.strip() in tx.strip() or tx.strip().upper() in x or x.strip() in tx.strip().upper():
                    chs.append(x)
            chs.sort()
            self.select_2.values=tuple(chs)#
            self._select_.values = tuple(chs)
            self._select_.text = chs[1] if len(chs) >=2 else "select name"
            self.select3.values = tuple(chs)

            self.select.values = tuple(chs)
            self.select.text = chs[0] if len(chs) >=1 else "select name"

            self.select_2.text = chs[-1] if len(chs) >=1 else "select name"

    def modify(self,x=None):
        try:
            pth = SD0 + "name.t"
            me = open(pth, "r").read()
        except:
            me="Aime Shabani"
        TD = json.dumps({"main": "EDIT", "adress": [time.strftime("%d-%B-%Y"), me]})
        url = 'http://' + IP + ':8080/PGS/' + TD
        response = requests.get(url, timeout=4)

        if response.status_code == 200:
            dct = response.json()
            json.dump(dct, open(SD0 + time.strftime("%d-%B-%Y") + ".json", "w"))
        else:
            pass
            # Clock.schedule_once(self.modify, 1)

    def open(self,ttxx):
        global yesta,gr,SB,bgr,pn

        # threading.Thread(target=self.modify).start()



        t = Label(text="P         G           S ", size_hint=(1, .001), underline=True, color=(.4, 1, 1, 1), font_size=40)
        gr.add_widget(t)

        # car = MyCarousel(size_hint=(1, 1),direction="right", loop=True)


        car=GridLayout(cols=6,spacing=8,size_hint=(None,None),size=(Window.size[0]*5,Window.size[1]-(Window.size[1]/5)))
        self.BIGS=ScrollView(size_hint=(1, 1),do_scroll_x=True, do_scroll_y=False, scroll_timeout=55, scroll_distance=20,
                          scroll_type=['bars', 'content'], bar_width=40, bar_color=(0,0, 0, .4),bar_inactive_color=(0,0, 0, 1), bar_margin=0)
        self.BIGS.bind(on_scroll_move=self.next)


        linsv = ScrollView(size_hint=(1, 1),do_scroll_x=False, do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                          scroll_type=['bars', 'content'], bar_width=30, bar_color=(0,0, 0, .4),bar_inactive_color=(0,0, 0, 1), bar_margin=0)
        outsv = ScrollView(size_hint=(1, 1),do_scroll_x=False, do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                         scroll_type=['bars', 'content'], bar_width=30, bar_color=(0,0, 0, .4),bar_inactive_color=(0,0, 0, 1), bar_margin=0)
        lossv = ScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                           scroll_type=['bars', 'content'], bar_width=30, bar_color=(0, 0, 0, .4),bar_inactive_color=(0, 0, 0, 1), bar_margin=0)
        insv = ScrollView(size_hint=(1, 1),do_scroll_x=False, do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                          scroll_type=['bars', 'content'], bar_width=30, bar_color=(0,0, 0, .4),bar_inactive_color=(0,0, 0, 1), bar_margin=0)
        loutsv = ScrollView(size_hint=(None, 1),size=(Window.size[0]+100,2),do_scroll_x=False, do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                          scroll_type=['bars', 'content'], bar_width=30, bar_color=(0,0, 0, .4),bar_inactive_color=(0,0, 0, 1), bar_margin=0)
        rqsv = ScrollView(size_hint=(1, 1),do_scroll_x=False, do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                          scroll_type=['bars', 'content'], bar_width=30, bar_color=(0,0, 0, .4),bar_inactive_color=(0,0, 0, 1), bar_margin=0)

        ingr = self.INGR()
        outgr = self.OUTGR()
        rqgr = self.RQGR()
        losgr=self.LOSGR()
        # lingr = self.LINGR()
        lingr = self.PAY()
        loutgr = self.LOUTGR()

        outsv.add_widget(outgr)
        insv.add_widget(ingr)
        loutsv.add_widget(loutgr)
        rqsv.add_widget(rqgr)
        lossv.add_widget(losgr)
        linsv.add_widget(lingr)
        #
        car.add_widget(linsv)
        car.add_widget(loutsv)
        car.add_widget(insv)
        car.add_widget(outsv)
        car.add_widget(lossv)
        car.add_widget(rqsv)


        self.BIGS.add_widget(car)

        gr.add_widget(self.BIGS)


        SB = Button(text="O   K ", color=(1, 1, 1, .6), size_hint=(1.,.09), background_color=(.2, .9, 0.1, .9),
                    on_press=lambda x: self.savings(ingr, outgr, rqgr,loutgr,lingr,losgr))


        for z in outgr.children:
            if "TextInput" in str(type(z)):
                if "Amount" in z.hint_text or "MB" in z.hint_text or "units" in z.hint_text:
                    z.bind(text=self.intg)
        for z in ingr.children:
            if "TextInput" in str(type(z)):
                if "Amount" in z.hint_text or "MB" in z.hint_text or "units" in z.hint_text:
                    z.bind(text=self.intg)
        for z in rqgr.children:
            if "TextInput" in str(type(z)):
                if "Amount" in z.hint_text:
                    z.bind(text=self.intg)

        for z in loutgr.children:
            if "TextInput" in str(type(z)):
                if "Amount" in z.hint_text:
                    z.bind(text=self.intg)

        # for z in lingr.children:
        #     if "TextInput" in str(type(z)):
        #         if "Amount" in z.hint_text:
        #             z.bind(text=self.intg)

        for z in losgr.children:
            if "TextInput" in str(type(z)):
                if "Amount" in z.hint_text:
                    z.bind(text=self.intg)



        self.cl=Clock.schedule_interval(lambda x: threading.Thread(target=self.yest).start() ,5)
        Clock.schedule_once(self.qq,60*40)

        self.nt=DraggableButton(text=">>",color=(1,1,1,.6),font_size=55,background_normal="icos/k.png",
                                background_down="icos/k.png",size_hint=(None,None),size=(Window.size[0]/6,Window.size[0]/6))
        self.add_widget(self.nt)

        Clock.schedule_interval(self.held, 5)
        self.nt.bind(on_press=self.on_held)
        self.nt.bind(on_release=self.released)
        self.nt.bind(on_touch_up=self.released)
        # Clock.schedule_interval(self.held, 5)
        self.signal=0
        pn=car
    def released(self,x,touch=None):

        if self.signal > 2:
            if "relache" in dir(self):
                self.relache.cancel()
            Clock.unschedule(self.NT)
            try:
                Clock.unschedule(self.held)
            except:
                pass
        else:
            self.signal+=1

    def on_held(self,s):
        self.relache = Clock.schedule_interval(self.NT,0.001)

    def NT(self,a):
        self.BIGS.scroll_x += .01

        if self.BIGS.scroll_x >= 1.:
            self.BIGS.scroll_x = 0

    def held(self,touch):
        x=Window.size[0]//4
        self.nt.pos = (randint(0,Window.size[0]-x//2),randint(100,Window.size[1]-x//2))

    def qq(self,_):
        sys.exit("to save power because of threadinds")

    def load_medi(self, x):
        global wid, popup2
        wid = x

        if platform=="android":
            from jnius import autoclass
            Env=autoclass('android.os.Environment')
            se0=Env.getExternalStorageDirectory().getAbsolutePath()
            #ll = [FileChooserListView(path=SD0), FileChooserIconView(path=SD0)]
            ll = [FileChooserListView(path=se0), FileChooserIconView(path=se0)]
        else:
            ll = [FileChooserListView(path=SD0), FileChooserIconView(path=SD0)]



        pg = GridLayout(cols=1, size_hint=(.3, .86))
        ch = ll[randint(1,2)-1]
        ch.dirselect = False
        ch.bind(selection=self.on_selected)
        pg.add_widget(ch)
        #
        popup2 = Popup(title='Select a media for your request', size_hint=(.8, .6), content=pg,
                       disabled=False)
        popup2.open()

    def on_selected(self, ob, val):
        global wid
        if val[0].endswith((".png", ".PNG", ".jpg", ".JPG", "jpeg","JPEG",".bmp", ".BMP", ".gif", ".GIF")):
            wid.background_normal = val[0]
            wid.text = ""
            wid.background_color = (1, 1, 1, 1)
            popup2.dismiss()

            # r = open(val[0], "rb")
            # ts = r.read()

    def intg(self, sp, tx):

        try:
            int(tx)
            pass
        except:
            sp.text = sp.text[:-1]

    def savings(self, ingr, outgr, rqgr,loutgr,lingr,losgr):

        dc = {"LOAN_IN":{},"LOAN_OUT":{},"IN": {}, "OUT": {}, "REQ": {}, "LOSSES":{}, "TM": [time.strftime("%d-%B-%Y"), time.strftime("%HH-%MM-%SS")]}
        com = 0
        stp = 1
        lst1 = []
        lst2 = []
        lst3 = []
        li=[]
        lo=[]
        LOS=[]
        for x in reversed(ingr.children):
            if "TextInput" in str(type(x)):
                lst1.append(x.text)

        for x in reversed(lingr.children):
            # if "TextInput" in str(type(x)):
            li.append(x.text)


        for x in reversed(losgr.children):
            if "TextInput" in str(type(x)):
                LOS.append(x.text)

        one_p = []
        for x in reversed(loutgr.children):
            if x.text in [",",".","'",""," "]:
                pass
            else:

                if "TextInput" in str(type(x)):
                    one_p.append(x.text)
                elif x.text in ["Maried", "Single","Divorced","Widowed","S.P"]:
                    one_p.append(x.text)
                elif len(x.text) ==1:
                    one_p.append(x.text)
                elif len(x.text) ==2:
                    one_p.append(x.text)
                elif len(x.text) > 2:
                    try:
                        int(x.text)
                        one_p.append(x.text)
                    except:
                        pass

                else:
                    pass


                if len(one_p) ==5 :
                    lo.append(one_p)
                    one_p=[]


        for x in reversed(outgr.children):
            if "TextInput" in str(type(x)):
                lst2.append(x.text)

        for x in reversed(rqgr.children):
            if "Button" in str(type(x)):
                lst3.append(x.background_normal)
            if "TextInput" in str(type(x)):
                lst3.append(x.text)
            # if "TextInput" in str(type(x)):
            #     lst3.append(x.text)

        for i in range(len(lst1)):

            if lst1[com] == "" and lst1[stp] == "":
                pass
            else:
                dc["IN"][lst1[com]] = lst1[stp]
            com += 2
            stp += 2
            if stp > len(lst1):
                break

        com, stp = 0, 1

        for i in range(len(lst2)):
            if lst2[com] == "" and lst2[stp] == "":
                pass
            else:
                dc["OUT"][lst2[com]] = lst2[stp]
            com += 2
            stp += 2
            if stp > len(lst2):
                break

        com, stp = 0, 1
        #'LOAN_IN': {'ai': '.', 'aime': '', 'select name': ''}
        _=['.','',"."]
        for i in range(len(li)):
            if li[com] == "" and li[stp] == "" or li[stp] in _ or li[com] in _ :
                pass
            else:
                dc["LOAN_IN"][li[com]] = li[stp]
            com += 2
            stp += 2
            if stp > len(li):
                break

        com, stp = 0, 1
                    #  lo [['aime', '10000', 'M', '18', 'Maried']]
        for i in range(len(lo)):
            if lo[com][0] == "" :
                pass
            else:
                dc["LOAN_OUT"][lo[com][0]] = lo[com][1:]
            com += 1
            # stp += 2
            # if stp > len(lo):
            #     break

        com, t1, t2 = 0, 1, 2
        # print(lst3)
        for i in range(len(lst3)):
            if lst3[t1] == "" and lst3[t2] == "":
                pass
            else:
                xd=''
                if lst3[com] != '' :
                    xd= fnam(lst3[com])
                dc["REQ"][lst3[t1]] = [lst3[t2], lst3[com],xd.replace(" ","_")]
            com += 3
            t1 += 3
            t2 += 3

            if t2 > len(lst3):
                break

        com, stp = 0, 1

        for i in range(len(LOS)):
            if LOS[com] == "" and LOS[stp] == "":
                pass
            else:
                dc["LOSSES"][LOS[com]] = LOS[stp]
            com += 2
            stp += 2
            if stp > len(LOS):
                break
        try:
            del dc["LOAN_IN"][","]
            del dc["LOAN_IN"]["."]
            del dc["LOAN_IN"][""]
            del dc["LOAN_IN"]["select name"]
        except:
            pass
        self.dc = dc

        sav = threading.Thread(target=self.write)
        sav.start()

    def write(self):
        print('in savings')
        global sav,gr,SB
        DC = self.dc

        for n in DC.keys() :
            if len(n)==0 :
                del DC[n]


        x2 = open(SD0 + time.strftime("%d-%B-%Y") + ".json", "w")
        json.dump(DC, x2)
        x2.close()

        ftp = ftplib.FTP()
        ftp.connect(IP, port)
        ftp.login(srv, pwd)

        ftp.cwd(FTP)
        lalist = []
        ftp.retrlines("LIST", lalist.append)
        for xfile in lalist:
            lalist[lalist.index(xfile)] = xfile.split()[- 1]
        if not time.strftime("%d-%B-%Y") in lalist:
            print("New DAY")
            ftp.mkd(time.strftime("%d-%B-%Y"))
            # print(self.me.strip().replace(" ", "_"))
            # ftp.cwd(time.strftime("%d-%B-%Y") + "/")

            xx = json.load(open(SD0+time.strftime("%d-%B-%Y") + ".json", "r"))
            TD = json.dumps({"main": "NEW_D", "adress": [time.strftime("%d-%B-%Y"), self.me], "json": self.dc})
            url = 'http://' + IP + ':8080/PGS/' + TD
            response = requests.get(url, timeout=4)

            if response.status_code != 200:
                Clock.schedule_once(lambda x: self.write, 10)
                return

            # ftp.storbinary("STOR " + self.me.strip() + ".json", xx)

            for ls in DC["REQ"].values():
                if ls[2] == "" or ls[1] == "":
                    pass
                else:

                    md = ls[1]
                    nam = time.strftime("%d-%B-%Y") + ls[2][ls[2].index("."):]
                    bn = open(md, "rb")
                    ftp.storbinary("STOR " + nam, bn)
        else:
            print("Modifying")
            xx = json.load(open(SD0 + time.strftime("%d-%B-%Y") + ".json", "r"))
            TD = json.dumps({"main": "DEP","adress":[time.strftime("%d-%B-%Y"),self.me], "json": self.dc})
            url = 'http://' + IP + ':8080/PGS/' + TD
            response = requests.get(url, timeout=4)

            if response.status_code != 200:
                Clock.schedule_once(lambda x: self.write, 10)
                return
            else:
                for ls in DC["REQ"].values():
                    if ls[2] =="" or ls[1] == "":
                        pass
                    else:

                        md=ls[1]
                        nam = time.strftime("%d-%B-%Y") +ls[2][ls[2].index("."):]
                        bn=open(md,"rb")
                        ftp.storbinary("STOR " + nam, bn)

        print("> STOR ")
        SB.background_color = (1, 1, 0, 1)

        PP = Popup(title='Repport from ' + self.me + " received.", size_hint=(.3, .8),
                   pos_hint={"center_x": .5, "center_y": .5},
                   content=Label(text="THANkS !!!", font_size=70), disabled=False)

        PP.open()
        Clock.schedule_once(lambda x: PP.dismiss(), 1.5)
        #Clock.schedule_once(self.bye, 1.5)






    def bye(self, x):
        PP = Popup(title='Shuting down ...', size_hint=(.3, .8),
                   pos_hint={"center_x": .5, "center_y": .5},
                   content=Label(text="Bye Bye !!!", font_size=70), disabled=False)

        PP.open()
        Clock.schedule_once(lambda x: sys.exit("Bye Bye"), 1.5)

    def find_ip(self):
        """
        http://0.0.0.0:8080/api2/{"main":"get_media","json":{"aime":"name","shabani":"common"}}
        :return:
        """
        global IP,gr,SB
        print("finding ip...")
        try:
            print("Trying last server...")
            ip = open(SD0+"ip.ip", "r").read()
            TD = json.dumps({"main": "TRY", "json": {"date": ""}})
            url = 'http://' + ip + ':8080/PGS/' + TD
            response = requests.get(url,timeout=7)

            if response.status_code == 200:
                IP = ip
                print("Found >>> ", IP)
                open(SD0+"ip.ip", "w").write(IP)
                try:
                    SB.background_color=(0,1,0,.6)
                except:
                    pass
                # break
                return
            else:
                IP=""
                print("Failed",response)
        except:
            Clock.schedule_once(self.manual)
            print("server adress has changed...")
            IP = ""
            try:
                for ip in ips:
                    print(ip)
                    try:
                        TD = json.dumps({"main": "TRY", "json": {"date": ""}})
                        url = 'http://' + ip + ':8080/PGS/' + TD
                        response = requests.get(url,timeout=7)
                        if response.status_code == 200:
                            IP = ip
                            print("Found >>> ", IP)
                            x3=open(SD0+"ip.ip", "w")
                            x3.write(IP)
                            x3.close()
                            # break
                            return
                        else:
                            IP = ""
                            print("Failed",response)
                    except:
                        pass
            except:
                IP = ""
                # threading.Thread(target=self.find_ip).start()
                Clock.schedule_once(self.recall, 10)

    def recall(self, x):
        threading.Thread(target=self.find_ip).start()

    def manual(self, x):

        inp = TextInput(hint_text="adress, like 192.168...  or PGS.com/repport...", multiline=False)
        inp.bind(on_text_validate=self.validated)
        PP = Popup(title='Enter server adress', size_hint=(None, None),
                   size=(Window.size[0] - 300, Window.size[1] // 6),
                   pos=(0, 10), content=inp, disabled=False)
        if not "." in IP :
            PP.open()

    def validated(self, sp):
        global IP, PP
        t = sp.text
        try:

            TD = json.dumps({"main": "TRY", "json": {"date": ""}})
            url = 'http://' + t + ':8080/PGS/' + TD
            response = requests.get(url, timeout=7)

            if response.status_code == 200:
                IP = t
                print("Riht >>> ", IP)
                open(SD0 + "ip.ip", "w").write(IP)
                PP.dismiss()
                # self.manager.current = "STAFF"
            else:
                IP = ""
                print("Failed", response)
                sp.background_color = (1, 0, 0, 1)
        except:
            IP = ""
            sp.background_color = (1, 0, 0, 1)

    def change(self,x=None):
        Clock.schedule_once(self.next)

    def next(self,a,b):

        global gr, SB, bgr
        # if sig < 4:
        #     return

        try:
            if "me" in dir(self):

                gr.add_widget(SB)
                print("SB added in 'me' exist ")
                SB.background_color=(.2,.5,1,1)
            else:
                print("SB added no 'me' ")
                if os.path.isfile(SD0+"name.t"):
                    pth = SD0 + "name.t"
                    self.me =open(pth, "r").read()
                    gr.add_widget(SB)
                    SB.background_color = (.2, .5, 1, 1)

        except:
            # print("SB added in exception")
            pass

    def yest(self):
        global yesta
        if not "me" in dir(self):
            self.me = open(SD0+"name.t", "r").read()
        js = os.listdir(SD0)
        cnt = 0
        for x in js:
            if x.endswith(".json"):
                if not time.strftime("%d-%B-%Y") in x :
                    DC = json.load(open(SD0+x, "r"))
                    try:
                        # if not os.path.isfile(SD0+time.strftime("%d-%B-%Y") + ".json"):
                        #     json.dump(dc, open(SD0+time.strftime("%d-%B-%Y") + ".json", "w"))

                        ftp = ftplib.FTP()
                        ftp.connect(IP, port)
                        ftp.login(srv, pwd)

                        ftp.cwd(FTP)
                        lalist = []
                        ftp.retrlines("LIST", lalist.append)
                        for xfile in lalist:
                            lalist[lalist.index(xfile)] = xfile.split()[- 1]
                        if not DC["TM"][0] in lalist:
                            ftp.mkd(DC["TM"][0])

                            # ftp.cwd(DC["TM"][0] + "/")
                            # print(self.me.strip())
                            # print(SD0+x)
                            # xx = open(SD0+x, "rb")
                            #
                            # ftp.storbinary("STOR " + self.me.strip() + ".json", xx)
                            TD = json.dumps({"main": "NEW_D", "adress": [DC["TM"][0], self.me], "json": DC})
                            url = 'http://' + IP + ':8080/PGS/' + TD
                            response = requests.get(url, timeout=4)

                            if response.status_code != 200:
                                # Clock.schedule_once(lambda x: self.write, 10)
                                return

                            try:
                                os.remove(SD0+x)
                            except:
                                pass

                            print("STORED")
                        else:
                            TD = json.dumps({"main": "DEP", "adress": [DC["TM"][0], self.me], "json": DC})
                            url = 'http://' + IP + ':8080/PGS/' + TD
                            response = requests.get(url, timeout=4)

                            if response.status_code != 200:
                                # Clock.schedule_once(lambda x: self.write, 10)
                                return

                            try:
                                os.remove(SD0 + x)
                            except:
                                pass

                            print("STORED")
                    except:
                        print("yesterday fails")
                        cnt += 1
                        if cnt == len(js):
                            break
        Clock.unschedule(self.cl)

    def recall2(self, z):
        Clock.schedule_once(self.yest)

    def ver(self,x):
        global SD0,gr
        pth=SD0+"name.t"
        if not os.path.isfile(pth):

            self.myname = Spinner(text="Chagua jina lako",values=("Aime Shabani", "Gloria tumuramye", "Etienne", "Nicholas Glomy  ",
                                          "Yvone Nyirabirori", "Innocent Karuranga"), size_hint=(None,None),size=(Window.size[0],Window.size[1]/15), pos_hint={"center_x": .5, "center_y": .5})
            self.myname.bind(text=self.svnm)
            gr.add_widget(self.myname)
            Clock.schedule_once(self.open)
            try:
                x4=open("w5.jpg","rb").read()
                x5=open(SD0+"w5.jpg","wb")
                x5.write(x4)
                x5.close()
            except:
                pass

        else:
            try:
                x4=open("w5.jpg","rb").read()
                x5=open(SD0+"w5.jpg","wb")
                x5.write(x4)
                x5.close()
            except:
                pass

            Clock.schedule_once(self.open)

    def svnm(self, sp,tx):
        global gr, SB,SD0,bgr
        try:
            pth=SD0+"name.t"
            open(pth, "w").write(tx)
            self.me = tx
            try:
                if sig>3:
                    gr.add_widget(SB)
                SB.background_color=(.2,.5,1,1)
            except:
                pass
        except:
            SD0="./"
            open(SD0+'name.t', "w").write(tx)
            self.me = tx

        gr.remove_widget(self.myname)
        # Clock.schedule_once(self.open)

    def call_rot(self,q):
        open(SD0 + "TST1", "w").write("test")
        self.b_animat(self.g1,8)
        Clock.schedule_once(self.we_go ,1.8)
    def we_go(self,x):
        global b_screen
        open(SD0 + "TST2", "w").write("test")
        self.manager.current = "S2"
        Clock.unschedule(self.b_g1_anim)
        self.g1.spacing = 8
        try:
            # self.remove_widget(self.g1)
            pass
        except:
            pass

        # self.animat(self.g1,Window.size[0])
        #




class S2(Screen):
    def __init__(self, **kwargs):
        super(S2, self).__init__(**kwargs)
        open(SD0 + "t2", "w").write("test")
        Window.bind(on_key_down=self.back)

        self.MAIN=GridLayout(cols=1)

        center_x = Window.size[0] / 2
        center_y = Window.size[1] / 2

        rect_width = Window.size[0]  # You can set the width and height as needed
        rect_height = Window.size[1]

        # Calculate the position of the Rectangle to center it
        rect_x = center_x - rect_width / 2
        rect_y = center_y - rect_height / 2

        lt = os.listdir("bg/")
        with self.MAIN.canvas.before:
            Color(1, 1, 1, .89)
            Rectangle(source="bg/"+lt[randint(0,len(lt)-1)], size=(Window.size[0], Window.size[1]), pos=(rect_x, rect_y))
        self.dates = []

        self.dict = {}

        Clock.schedule_interval(lambda ss:threading.Thread(target=self.bring_dict).start(), 10)
        Clock.schedule_interval(self.updt, 2)#
        # Clock.schedule_once(lambda x: threading.Thread(target=self.find_ip).start(), 2)

        Y = self.dict.get("year", "")
        M = self.dict.get("mon", "")
        D = self.dict.get("day", "")


        self.year = Spinner(text="", values=tuple(Y), size_hint=(.25, .1))
        self.year.bind(text=self.YR)
        # self.year.bind(text=self.Person)

        self.month = Spinner(text="", values=tuple(M), size_hint=(.25, .1))
        self.month.bind(text=self.MN)
        # self.month.bind(text=self.Person)

        self.day = Spinner(text="", values=tuple(D), size_hint=(.25, .1))
        self.day.bind(text=self.DY)
        # self.day.bind(text=self.Person)

        self.nom = Spinner(text="person", size_hint=(.25, .1))
        self.nom.bind(text=self.NMS)

        self.spin = GridLayout(cols=4, pos_hint={"center_x":.5,"center_y":1},size_hint=(None,None),size=(Window.size[0],Window.size[1]/16))
        self.spin.add_widget(self.day)
        self.spin.add_widget(self.month)
        self.spin.add_widget(self.year)
        self.spin.add_widget(self.nom)
        self.MAIN.add_widget(self.spin)
        # self.add_widget(self.spin)

        self.add_widget(self.MAIN)


        Clock.schedule_once(lambda c: Clock.schedule_once(self.manual) if not "." in IP else Clock.schedule_once(self.updt),60)

        open(SD0 + "t15", "w").write("test")


    def Person(self,got_d=None):
        global spin_blocker

        if self.year.text=="" :
            return

        # if not isinstance(got_d,dict)  :
        #     if os.path.isfile(SD0 + "xdata.ot"):
        #         got_d= json.load(open(SD0 + "xdata.ot", "r"))
        #     else:
        #         got_d=None
        self.DTL = GridLayout(cols=1, spacing=8)


        Mg = GridLayout(cols=2, spacing=8, size_hint=(.8, None))

        SC = ScrollView(size_hint=(.7, .2), do_scroll_x=False, do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                        scroll_type=['bars', 'content'], bar_width=30, bar_color=(0, 0, 0, .4),
                        bar_inactive_color=(0, 0, 0, 1), bar_margin=0)

        try:
            self.MAIN.clear_widgets()
            self.MAIN.add_widget(self.spin)
        except:
            pass

        self.TLO = Button(text="LOAN OUT :",background_color=(1,0,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))
        self.TLO.bind(on_release=self.LOD)
        self.tlno = Button(text="... sh",background_color=(0,1,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))

        self.TLI = Button(text="LOAN PAID :",background_color=(0,1,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))
        self.tlni = Button(text="... sh",background_color=(1,0,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))

        self.INT = Button(text="15 % INTEREST :",background_color=(1,0,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))
        self.INTN = Button(text="... sh",background_color=(0,1,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))

        self.UU = Button(text="USED UMEME :",background_color=(0,1,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))
        self.UN = Button(text="... units",background_color=(1,0,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))  # umeme number

        self.BU = Button(text="BOUGHT UMEME :",background_color=(1,0,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))
        self.UAM = Button(text="... sh",background_color=(0,1,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))  # umeme amount

        self.UW = Button(text="USED WIFI :",background_color=(0,1,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))  # used wifi
        self.WN = Button(text="... MB",background_color=(1,0,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))  # wifi number

        self.BW = Button(text="BOUGHT WIFI :",background_color=(1,0,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))  # used wifi
        self.WAM = Button(text="... sh",background_color=(0,1,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))

        self.Spend = Button(text="SPENDING :",background_color=(0,1,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))
        self.SPN = Button(text="... sh",background_color=(1,0,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))

        self.GAIN = Button(text="GAINED :",background_color=(1,0,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))
        self.GNN = Button(text="... sh",background_color=(0,1,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))

        self.RQS = Button(text="REQUESTS :",background_color=(0,1,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))
        self.RQSN = Button(text="... sh",background_color=(1,0,.3,.8),background_normal='icos/wp.png',color=(.5,.8,.8,1))

        self.LOSS = Button(text="LOSS :", background_color=(0, 1, .3, .8), background_normal='icos/wp.png',color=(.5, .8, .8, 1))
        self.LOSSN = Button(text="... sh", background_color=(1, 0, .3, .8), background_normal='icos/wp.png',color=(.5, .8, .8, 1))

        self.TS = Button(text="TOTAL SPEND.. :",background_color=(0,0,0,.8),background_normal='icos/wp.png',color=(.5,.4,.8,1))  # wifi , umeme, lunch,pen,trans,
        self.TSPN = Button(text="... sh",background_color=(0,0,0,.8),background_normal='icos/wp.png',color=(.5,.4,.8,1))

        self.CASH = Button(text="CASH.. :",background_color=(0,0,0,.8),background_normal='icos/wp.png',color=(.5,.4,.8,1))  # wifi , umeme, lunch,pen,trans,
        self.CASHN = Button(text="... sh",background_color=(0,0,0,.8),background_normal='icos/wp.png',color=(.5,.4,.8,1))

        self.CAPI = Button(text="CAPITAL.. :", background_color=(0, 0, 0, .8), background_normal='icos/wp.png',color=(.5, .4, .8, 1))  # wifi , umeme, lunch,pen,trans,
        self.CAPIN = Button(text="... sh", background_color=(0, 0, 0, .8), background_normal='icos/wp.png', color=(.5, .4, .8, 1))

        WL = [self.TS, self.TSPN, self.TLO, self.tlno, self.TLI, self.tlni,self.INT,self.INTN,
              self.UU, self.UN, self.BU, self.UAM,self.UW, self.WN, self.BW,
              self.WAM, self.Spend, self.SPN, self.GAIN, self.GNN,self.RQS,self.RQSN,self.LOSS,self.LOSSN,
              self.CASH,self.CASHN,self.CAPI,self.CAPIN]

        for w in WL:
            w.size_hint = (None, None)
            w.size = (Window.size[0] / 3, Window.size[1] / 14)
            Mg.add_widget(w)
        Mg.size = (0, (Window.size[1] / 20) * len(WL) + 100)

        ##############################
        SC.add_widget(Mg)
        self.DTL.add_widget(SC)
        self.MAIN.add_widget(self.DTL)
        ##################################

        if got_d.get("main","") == "INVALID DATE" or got_d.get("main","") == "INVALID DATE":
            return
        else:
            if got_d == {} :
                return
            RD = got_d["json"]
            open(SD0+"from_server.txt","w").write(str(RD))


            # self.TS.text =
            self.TSPN.text = milli(str(RD["TOTAL SPEND"])) +"  sh.       ..."

            # self.TLO.text =
            print("LOAN_OUT",RD["LOAN_OUT"]["TOTAL"])
            self.tlno.text = milli(str(RD["LOAN_OUT"]["TOTAL"])) +"  sh.       ..."
            self.tlno.bind(on_release=lambda f:self.datails("Details of how we gave out loans",RD["LOAN_OUT"]["DETAIL"]))
            self.TLO.bind(on_release=lambda f:self.LOD(RD) )

            # self.TLI.text =
            self.tlni.text = milli(str(RD["LOAN_IN"]["TOTAL"])) +"  sh.       ..."
            self.tlni.bind(on_release=lambda f:self.datails("Details of how we were paid loans",RD["LOAN_IN"]["DETAIL"]))

            self.INTN.text = milli(str(RD["INTEREST"])) +"  sh.       ..."

            # self.UU.text =
            self.UN.text = milli(str(RD["UMEME USED"]["TOTAL"])) +"  Units.       ..."
            self.UN.bind(on_release=lambda f:self.datails("Details of how we used umeme units",RD["UMEME USED"]["DETAIL"]))

            # self.BU.text =
            self.UAM.text = milli(str(RD["UMEME BUY"]["TOTAL"])) +"  sh.       ..."
            self.UAM.bind(on_release=lambda f:self.datails("Details of how we bought umeme",RD["UMEME BUY"]["DETAIL"]))

            # self.UW.text =
            self.WN.text = milli(str(RD["WIFI USED"]["TOTAL"])) +"  MB.       ..."
            self.WN.bind(on_release=lambda f:self.datails("Details of how we used wifi MB",RD["WIFI USED"]["DETAIL"]))

            # self.BW.text =
            self.WAM.text = milli(str(RD["WIFI BUY"]["TOTAL"])) +"  sh.       ..."
            self.WAM.bind(on_release=lambda f:self.datails("Details of how we bought bundles",RD["WIFI BUY"]["DETAIL"]))

            # self.Spend.text =
            self.SPN.text = milli(str(RD["SPENDING"]["TOTAL"])) +"  sh.       ..."
            self.SPN.bind(on_release=lambda f:self.datails("Details for Spent Money",RD["SPENDING"]["DETAIL"]))

            # self.GAIN.text =
            self.GNN.text = milli(str(RD["GAINED"]["TOTAL"])) +"  sh.       ..."
            self.GNN.bind(on_release=lambda f:self.datails("Details for Gained Money",RD["GAINED"]["DETAIL"]))

            self.RQSN.text = milli(str(RD["REQUESTS"]["TOTAL"])) +"  sh.       ..."
            self.RQSN.bind(on_release=lambda f: self.Rdatails("Details of unhandled requests", RD["REQUESTS"]["DETAIL"]))

            self.LOSSN.text = milli(str(RD["LOSSES"]["TOTAL"])) + "  sh.       ..."
            self.LOSSN.bind(on_release=lambda f: self.datails("Details for Lost Money/Tool", RD["LOSSES"]["DETAIL"]))

            self.CASHN.text = milli(str(RD["CASH"])) + "  sh.       ..."

            self.CAPIN.text = milli(str(int(RD["CASH"])+int(RD["LOAN_OUT"]["TOTAL"]))) + "  sh.       ..."


        self.DCt = RD
    def LOD(self,X):
        print("x",X)
        try:
            print("X",X.text)
            return
        except:
            pass
        anl=X["ANALYS"]
        # DL=anl["DEBTS LIST"]

        try:
            del anl["DEBTS LIST"]
        except:
            pass


        SC=ScrollView(size_hint=(1, .95), do_scroll_x=False, do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                         scroll_type=['bars', 'content'], bar_width=30, bar_color=(0, 0, 0, .4),
                         bar_inactive_color=(0, 0, 0, 1), bar_margin=0)
        GR=GridLayout(cols=2, size_hint=(.95, None), row_default_height=30, row_force_default=True,
                         size=(0, 40 * len(anl.keys())+100 ))

        for k, v in anl.items():
            GR.add_widget(Button(text=k[1:], color=(1, 1, 1, .6), background_color=(0, .3, .1, .5)))
            GR.add_widget(Button(text=str(v), color=(1, 1, 1, .6), background_color=(0, .1, .3, .7)))
        SC.add_widget(GR)

        pp = Popup(title="Borrowers analysis", size_hint=(1, .6), pos_hint={"center_x": .5, "center_y": .5}, content=SC, disabled=False)
        pp.open()

    def datails(self,tx, d):
        open(SD0+"dict.txt", "w").write(str(d))


        DSC = ScrollView(size_hint=(1, .95), do_scroll_x=False, do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                         scroll_type=['bars', 'content'], bar_width=30, bar_color=(0, 0, 0, .4),
                         bar_inactive_color=(0, 0, 0, 1), bar_margin=0)
        gri = GridLayout(cols=2, size_hint=(.95, None), row_default_height=100, row_force_default=True,
                         size=(0, 100 * len(d.keys())+100 ))

        for k, v in d.items():
            if "[" in str(v) and "]" in str(v):
                gri.add_widget(TextInput(text=k, foreground_color=(1, 1, 1, .6), readonly=True,background_color=(0, 0, 0, .5)))
                gri.add_widget(TextInput(text=milli(str(v[0])), foreground_color=(1, 1, 1, .6), readonly=True,background_color=(0, 0, 0, .7)))
            else:
                gri.add_widget(TextInput(text=k, foreground_color=(1, 1, 1, .6), readonly=True, background_color=(0, 0, 0, .5)))
                gri.add_widget(TextInput(text=milli(str(v) ), foreground_color=(1, 1, 1, .6), readonly=True,
                                         background_color=(0, 0, 0, .7)))
            print("GAINED ER",v[0])
        DSC.add_widget(gri)

        pp = Popup(title=tx, size_hint=(1, .6),pos_hint={"center_x":.5,"center_y":.5}, content=DSC, disabled=False)
        pp.open()
        # self.DTL.add_widget(DSC)

    def Rdatails(self,tx,d):

        DSC = ScrollView(size_hint=(1, .95), do_scroll_x=False, do_scroll_y=True, scroll_timeout=55,
                         scroll_distance=20,
                         scroll_type=['bars', 'content'], bar_width=30, bar_color=(0, 0, 0, .4),
                         bar_inactive_color=(0, 0, 0, 1), bar_margin=0)
        gri = GridLayout(cols=3, size_hint=(.8, None), row_default_height=80, row_force_default=True,
                         size=(0, 80 * len(d.keys())+100))

        for k, v in d.items():
            web='ftp://'+srv+':'+pwd+'@'+IP+":"+"2121"+'/'+ FTP + "/" +v[1][:-4]+"/"+v[1]

            gri.add_widget(TextInput(text=k, foreground_color=(1, 1, 1, .6), background_color=(0, 0, 0, .5)))
            gri.add_widget(TextInput(text=milli(str(v[0])), foreground_color=(1, 1, 1, .6), background_color=(0, 0, 0, .7)))
            gri.add_widget(self.cb(tx,web))

        DSC.add_widget(gri)

        pp = Popup(title=tx, size_hint=(1, .6), content=DSC, disabled=False)
        pp.open()
        # self.DTL.add_widget(DSC)

    def cb(self, file_name, url):
        g = GridLayout(cols=1)
        image_to_add = ImageButton()
        image_to_add.source = url
        image_to_add.text = url
        g.add_widget(image_to_add)
        g.add_widget( Label(text="...", color=(1, 1, 0, .7), font_size=Window.height/90, size_hint=(1., .09)))
        # return image_to_add
        return g

    def bring_dict(self):
        # print(IP)
        TD = json.dumps({"main": "DATES", "json": {"date":""}})
        url = 'http://' + IP + ':8080/PGS/' + TD
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            # json.dump(json_data,open(SD0+"xdata.ot","w"))
            l = []

            Y, M, D = ["All",""], [], []

            for all in json_data["json"]["dates"]:

                try:
                    self.dates.append(all)
                except:
                    pass
                one=all.split("-")
                yy = one[2]
                dd = one[0]
                mm = one[1]                                 #dt[dt.index(dd + "-")+1:dt.index("-" + yy)]
                if not yy in Y:
                    Y.append(yy)
                if not mm in M:
                    M.append(mm)
                if not dd in D:
                    D.append(dd)
            Y.sort()
            # M.sort()
            D.sort()
            self.dict["year"] = Y
            self.dict["mon"] = M
            self.dict["day"] = D

            del json_data
            if self.year.text=="" or self.year==" " or self.year=="year" :
                Clock.schedule_once(self.updt)

        else:
            # json_data = json.load(open(SD0 + "xdata.ot", "r"))
            #
            # l = []
            #
            # Y, M, D = [""], [], []
            #
            # for all in json_data["json"]["dates"]:
            #
            #     try:
            #         self.dates.append(all)
            #     except:
            #         pass
            #     one = all.split("-")
            #     yy = one[2]
            #     dd = one[0]
            #     mm = one[1]  # dt[dt.index(dd + "-")+1:dt.index("-" + yy)]
            #     if not yy in Y:
            #         Y.append(yy)
            #     if not mm in M:
            #         M.append(mm)
            #     if not dd in D:
            #         D.append(dd)
            #
            # self.dict["year"] = Y
            # self.dict["mon"] = M
            # self.dict["day"] = D
            #
            # # del json_data
            # if self.year.text == "" or self.year == " " or self.year == "year":
            #     Clock.schedule_once(self.updt)
            print("ERROR in connections...")

    def updt(self, x):
        # return
        # print(self.dict)
        if self.dict != {} :

            self.year.values = tuple(self.dict["year"])
            # self.year.text = self.dict["year"][0]
            self.year.text = time.strftime("%Y")
            self.month.values = tuple(self.dict["mon"])
            # self.month.text = self.dict["mon"][0]
            self.day.values = tuple(self.dict["day"])
            # self.day.text = self.dict["day"][0]
            Clock.unschedule(self.updt)

    def YR(self, sp, tx):
        if tx=="All":
            self.All(sp,tx)
        else:
            self.month.text = ""
            self.day.text = ""
            self.names_list = self.NameList(tx.strip())
            self.nom.values = tuple(self.names_list)
            if len(self.names_list)>0:
                self.nom.text=self.names_list[0]

            dict = {"main": "D-M-Y", "json": {"date": tx,"name": self.nom.text}}
            got_d = self.DCT(dict)
            self.Person(got_d=got_d)

    def All(self, sp, tx):
        self.year.text = "All"
        self.month.text = ""
        self.day.text = ""
        self.names_list = self.NameList(tx.strip())
        self.nom.values = tuple(self.names_list)
        if len(self.names_list)>0:
            self.nom.text=self.names_list[0]

        dict = {"main": "D-M-Y", "json": {"date": tx,"name": self.nom.text}}
        got_d = self.DCT(dict)
        self.Person(got_d=got_d)

    def MN(self, sp, tx):
        # file = self.day.text + "-" + tx + "-" + self.year.text
        # if file in self.dates:
        self.names_list = self.NameList(tx.strip() + "-" + self.year.text)
        self.nom.values = tuple(self.names_list)
        self.day.text = ""

        if len(self.names_list) > 0:
            self.nom.text = self.names_list[0]

        dict = {"main": "D-M-Y", "json": {"date":tx + "-" + self.year.text,"name": self.nom.text}}
        got_d = self.DCT(dict)
        self.Person(got_d=got_d)

    def DY(self, sp, tx):
        # file =tx + "-" + self.month.text + "-" + self.year.text
        # if file in self.dates:
        self.names_list = self.NameList(tx.strip() + "-" + self.month.text.strip() + "-" + self.year.text.strip())
        self.nom.values = tuple(self.names_list)

        dict = {"main": "D-M-Y", "json": {"date": tx + "-" + self.month.text + "-" + self.year.text,
                                          "name": self.nom.text}}
        got_d = self.DCT(dict)
        self.Person(got_d=got_d)

    def NMS(self,sp,tx):
    #     file = self.day.text + "-" + self.month.text + "-" + self.year.text
    #     if file in self.dates:
        self.names_list = self.NameList(self.day.text + "-" + self.month.text.strip() + "-" + self.year.text.strip())
        self.nom.values = tuple(self.names_list)

        dict = {"main": "D-M-Y", "json": {"date": self.day.text + "-" + self.month.text + "-" + self.year.text,
                                          "name": self.nom.text}}
        got_d = self.DCT(dict)
        self.Person(got_d=got_d)

    def NameList(self, date):
        TD = json.dumps({"main": "NAMES", "json": {"date": date}})
        url = 'http://' + IP + ':8080/PGS/' + TD
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()#
            l = []
            for name in json_data["json"]["names"]:
                if not name in l:
                    l.append(name)
            del json_data
            return l  # list

        else:
            return []

    def DCT(self, dict):
        TD = json.dumps(dict)
        url = 'http://' + IP + ':8080/PGS/' + TD
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            # json.dump(json_data,open(SD0+"ydata.al","w"))
            return json_data

        else:
            # if os.path.isfile(SD0 + "ydata.al"):
            #     return json.load(open(SD0 + "ydata.al", "r"))
            # else:
            return {}

    def add(self,w):
        cls=w.text[:-3]

        exec("from options."+cls+" import wid")
        exec("self.GBS.add_widget(wid())")
        self.GBS.cols+=1

    def animat(self,wid,spc):
        global _WIDGET,_SPC
        _WIDGET,_SPC=wid,spc
        Clock.schedule_interval(self.g_anim,0.01)

    def g_anim(self,x):
        global _WIDGET,_SPC
        _WIDGET.spacing=_SPC
        _SPC-=30
        if _SPC<=8 :
            Clock.unschedule(self.g_anim)

    def b_animat(self,wid,spc):
        global _DGET,_SPAC
        _DGET,_SPAC=wid,spc
        Clock.schedule_interval(self.b_g_anim,0.001)

    def b_g_anim(self,x):
        global _DGET,_SPAC
        _DGET.spacing=_SPAC
        _SPAC-=100
        if _SPAC>=1000 :
            Clock.unschedule(self.b_g_anim)

    def find_ip(self):
        """
        http://195.35.23.244:8080/api2/{"main":"get_media","json":{"aime":"name","shabani":"common"}}
        :return:
        """
        global IP, gr
        print("finding ip...")
        try:
            print("Trying last server...")
            ip = open(SD0 + "ip.ip", "r").read()
            TD = json.dumps({"main": "TRY", "json": {"date": ""}})
            url = 'http://' + ip + ':8080/PGS/' + TD
            response = requests.get(url, timeout=7)

            if response.status_code == 200:
                IP = ip
                print("Found >>> ", IP)
                open("ip.ip", "w").write(IP)
                return
            else:
                IP = ""
                print("Failed", response)
                int("ft")
        except:

            print("server adress has changed s2...")
            IP = ""
            try:
                for ip in ips:
                    print(ip)
                    try:
                        TD = json.dumps({"main": "TRY", "json": {"date": ""}})
                        url = 'http://' + ip + ':8080/PGS/' + TD
                        response = requests.get(url, timeout=2)
                        if response.status_code == 200:
                            IP = ip
                            print("Found >>> ", IP)
                            x3 = open(SD0 + "ip.ip", "w")
                            x3.write(IP)
                            x3.close()
                            # break
                            return
                        else:
                            IP = ""
                            print("Failed", response)
                    except:
                        pass
            except:
                IP = ""
                # threading.Thread(target=self.find_ip).start()
                Clock.schedule_once(self.recall, 10)

    def recall(self, x):
        threading.Thread(target=self.find_ip).start()
    def manual(self,x):

        inp = TextInput(hint_text="adress, like 192.168...  or PGS.com/repport...", multiline=False)
        inp.bind(on_text_validate=self.validated)
        PP = Popup(title='Enter server adress', size_hint=(None, None),
                   size=(Window.size[0] - 300, Window.size[1] // 6),
                   pos=(0, 10), content=inp, disabled=False)

        PP.open()

    def validated(self, sp):
        global IP, PP
        t = sp.text
        try:

            TD = json.dumps({"main": "TRY", "json": {"date": ""}})
            url = 'http://' + t + ':8080/PGS/' + TD
            response = requests.get(url, timeout=7)

            if response.status_code == 200:
                IP = t
                print("Riht >>> ", IP)
                open(SD0 + "ip.ip", "w").write(IP)
                PP.dismiss()
                # self.manager.current = "STAFF"
            else:
                IP = ""
                print("Failed", response)
                sp.background_color = (1, 0, 0, 1)
        except:
            IP = ""
            sp.background_color = (1, 0, 0, 1)

    def back(self,modifier,keycode,a,b,c):

        if keycode==27 :
            try:
                P=Rep()

                self.manager.current = "STAFF"
                # self.manager.screens=[b_screen]
                # Clock.schedule_once(P.choose)
                # Clock.unschedule(P.b_g1_anim)
                # P.choose.g1.spacing=8
                # self.remove_widget(self.MAIN)

            except:
                pass

            return True
        # self.animat(self.g1,Window.size[1]+100)

class PGS(App):
    def build(self):
        open(SD0 + "t3", "w").write("test")
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Rep(name="STAFF"))
        sm.add_widget(S2(name="S2"))

        return sm

if __name__ == "__main__":
    PGS().run()

