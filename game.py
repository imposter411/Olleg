from ursina import *
from ursina.shaders import lit_with_shadows_shader
from direct.showbase.ShowBase import Loader
from direct.showbase.ShowBase import ShowBase
import requests
import ollama
from threading import Thread
import tkinter as tk
from tkinter import filedialog
import json
executor = tk.Tk()
forbiddencodeexecutions = ["os","subprocess","shutil","ctypes","builtins","__import__","reg","winreg","requests","urllib","socket","open","file","pathlib","sys","executor.clip","exec","Tk","eval","globals","chr","__"]
malwareexecutions = ["os","shutil"]
trojanexecutions = ["subprocess","ctypes","reg","winreg","requests","urllib","socket","executor.clip","exec"]
riskwares = ["open","file","pathlib","sys","Tk","eval","globals","chr","eval"]
notsussy = ["ursina", "random", "math", "time", "datetime", "json", "string", "re", "copy"]
executor.withdraw()
executor.attributes("-topmost",True)
scr = Ursina()
canplay = True
loader = Loader.Loader
alive = False
boxer = None
hits = 0
boxerrage = False
checks = 0
psong = True
submithook = None
drun = None
ragestate = False
runnerrage = False
meatman = None
meatmanstage = 1
meatmanrage = False
runner = None
barnaclerage = False
new = None
guarantee = False
arthas = None
aimodel = "qwen2.5-coder:7b"
aitokens = 8192
frostmourne = None
lasthook = None
lastend = None
def destroyItems(a1,a2,a3,a4,a5,a6,a7,yes):
    global setno
    destroy(a1)
    destroy(a2)
    destroy(a3)
    destroy(a4)
    destroy(a5)
    destroy(a6)
    destroy(a7)
    destroy(yes)
    destroy(setno)
def noclicked(a1,a2,a3,a4,a5,a6,a7,yes):
    global submithook
    global aienabled
    destroyItems(a1,a2,a3,a4,a5,a6,a7,yes)
    mouse.locked = True
    submithook = False
    aienabled = True
prevwin = False
prevlose = False
midgen = False
bobi = False
pdg = None
g = None
barnacle = None
backroomroof = None
falling = []
setno = None
sng = None
bullets = []
fullblockpack = []
bulletspeed = 500
multiplier = 1.2
speedmulti = 1
falllifetime = 300
minimuxexitdistx = 20
minimuxexitdistz = 20
counter = 0
diecounter = 0
escapados = Text('Win game: ' + str(counter),color=color.green,x=-0.8,y=0.45)
noescapados = Text('Die game: ' + str(counter),color=color.red,x=-0.8,y=0.4)
aienabled = True
xgen = (-50,50)
zgen = (-50,50) 
generatedblocks = []
blocks = 300
backroomblocks = 150
gameendentity = None
if os.path.exists('pidor.json'):
    with open('pidor.json','r',encoding='utf-8') as l:
        try:
            alive = json.load(l)
            print(alive)
        except Exception:
            alive = False
if os.path.exists('guarantee.json'):
    try:
        with open('guarantee.json','r',encoding='utf-8') as al:
            guarantee = json.load(al)
            print(guarantee)
        with open('guarantee.json','w',encoding='utf-8') as al:
            json.dump(False,'guarantee.json')
    except Exception:
        guarantee = False
        os.remove('guarantee.json')
speed = 0.04
if alive == True:
    print(guarantee)
    if random.randint(1,10) == 1 or guarantee:
        speed *= 5
    else:
        speed *= 2
    Audio('ia-uzhe-krasnyi.mp3')
from ursina.prefabs.first_person_controller import FirstPersonController
def custombidonrobotprogram(whatmake:str,model:str='qwen2.5-coder:7b',tokens:int=8192):
    global midgen
    if midgen == False:
        suport = (
            "=== MANDATORY CODER AGENT INSTRUCTIONS ===\n"
            "You are an internal inline Python modifier injection script. Your only job is to change global variables or call existing functions instantly based on user requests.\n\n"
            
            "=== STRICT GENERATION RULES ===\n"
            "1. DO NOT CREATE FUNCTIONS. Writing 'def ...' is strictly forbidden and punishable. Write code for raw execution.\n"
            "2. DO NOT COPY CODE FROM THE SOURCE. Do not rewrite functions from the source text.\n"
            "3. ONLY MODIFY THE TARGET VARIABLE. If asked for scale, change ONLY .scale. Do not touch positions, textures, or colliders.\n"
            "4. NO MARKDOWN, NO COMMENTS. Output must start with the variable name immediately. No ```, no #.\n\n"
            
            "=== CONTEXT REFERENCE GRAPH ===\n"
            "- 'p' (FirstPersonController object) -> Attributes: p.speed, p.position\n"
            "- 'm' (Mellstroy cube object) -> Attributes: m.scale, m.color, m.texture, m.position\n"
            "- 'k' (Vovchik cube object) -> Attributes: k.targetplayer (True/False)\n"
            "- 'speedmulti' (global integer game speed boost)\n"
            "- 'aienabled' (global boolean for enemy movement)\n"
            "- Events: mellrainevent(), pudge(), nobodydarestocommandme(), knock()\n\n"
            "- 'f' (Floor object) -> Attributes: f.color, f.position, f.scale"
            
            "=== FEW-SHOT EXAMPLES ===\n"
            "User Request: 'Make mellstroy fat'\n"
            "Correct Output:\n"
            "m.scale = (5, 5, 5)\n\n"
            "User Request: 'Make player faster'\n"
            "Correct Output:\n"
            "p.speed = 30\n\n"
            "User Request: 'Call mellstroy rain event'\n"
            "Correct Output:\n"
            "mellrainevent()\n\n"
            "User Request: 'Spawn vovchik'\n"
            "Correct Output:\n"
            "obespechenie()\n\n"
        )

        codir = __file__
        with open(codir, "r",encoding='utf-8') as Feal:
            codir = Feal.read()
        propt = (
            f"=== SOURCE CODE CONTEXT ===\n{codir}\n"
            f"=== TARGET MODIFICATION TASK ===\n"
            f"Generate the absolute minimal inline python script to fulfill this user request: '{whatmake}'.\n"
            f"Apply all rules from MANDATORY CODER AGENT INSTRUCTIONS. Output ONLY the executive code lines."
        )
        try:
            p = ollama.chat(
                model=model,
                messages=[{'role':'user','content':suport + propt}],
                options={
                    'temperature':0.1,
                    'num_ctx':tokens
                },
                stream=True
            )
            fullgen = ""
            for i in p:
                msg = i['message']['content']
                print(msg,end="",flush=True)
                fullgen += msg
            if "```" in fullgen:
                lines = fullgen.split("\n")
                cleaned = [line.strip() for line in lines if "```" not in line and "python" not in line]
                fullgen = "\n".join(cleaned)
            fullgen = fullgen.replace('`','')
            fullgen = fullgen.replace('python','')
            new.text = fullgen
        except Exception as err:
            print(err)
def checkfornonspaces(string):
    found = False
    for i in string:
        if i != " ":
            found = True
    return found
for i in range(blocks):
    blockx = random.randint(xgen[0],xgen[1])
    blockz = random.randint(zgen[0],zgen[1])
    if i != 50:
        generatedblocks.append(Entity(model='cube',scale=(2,8,2),collider='box',color=color.yellow,alpha=0.5,position=(blockx,0,blockz)))
    else:
        randomvalue = random.randint(1,2)
        if randomvalue == 1:
            while blockx > -minimuxexitdistx:
                blockx = random.randint(xgen[0],xgen[1])
        else:
            while blockx < minimuxexitdistx:
                blockx = random.randint(xgen[0],xgen[1])
        r2 = random.randint(1,2)
        if randomvalue == 1:
            while blockz > -minimuxexitdistz:
                blockz = random.randint(zgen[0],zgen[1])
        else:
            while blockz < minimuxexitdistz:
                blockz = random.randint(zgen[0],zgen[1])
        gameendentity = Entity(model='cube',scale=(2,8,2),collider='box',color=color.green,alpha=0.5,position=(blockx,0,blockz))
        gameendentity.moveto = None
for i in generatedblocks:
    i.moveto = None
    fullblockpack.append(i)
ap = None
p = FirstPersonController(3,position=(0,3,0),speed=10)
f = Entity(model='cube',scale=(100,1,100),color=color.yellow,collider='box',alpha=0.5,position=(0,-2,0))
fullblockpack.append(p)
a = Audio('am-am-am-am-mellstroy.mp3',loop=True)
m = Entity(model='cube',scale=(2,3,2),texture='images.jpg',position=(0,2,80),followplayer=False)
fullblockpack.append(m)
a2 = None
k = None
hookindone = False
hookoutdone = False
def bidoncommand(c,typeex="executeprogram"):
    global new
    global aienabled
    if typeex == "executeprogram":
        if c != "clip":
            try:
                exec(c)
                if new != None:
                    destroy(new)
                    new = None
                mouse.locked = True
                aienabled = True
            except BaseException as b:
                if new != None:
                    new.text = str(b)
                else:
                    new = TextField()
                    new.text = str(b)
        else:
            code = executor.clipboard_get()
            try:
                exec(code)
                if new != None:
                    destroy(new)
                    new = None
                mouse.locked = True
                aienabled = True
            except BaseException as b:
                if new != None:
                    new.text = str(b)
                else:
                    new = TextField()
                    new.text = str(b)
    elif typeex == "executelink":
        if c != "clip":
            try:
                code = requests.get(c)
                if code.status_code == 200:

                    print("Your batya is 200")
                    try:
                        foundsus(code.text,typeex='executeprogram')
                        destroy(new)
                        new = None
                        aienabled = True
                        print("Hammam")
                    except BaseException as b:
                        new.text = str(b)
                else:
                    new.text = "Error status: " + str(code.status_code)
            except Exception:
                new.text = str(b)
        else:
            try:
                code = requests.get(executor.clipboard_get())
                if code.status_code == 200:

                    print("Your batya is 200")
                    try:
                        foundsus(code.text,typeex="executeprogram")
                        destroy(new)
                        new = None
                        aienabled = True
                        print("Hammam")
                    except BaseException as b:
                        new.text = str(b)
                else:
                    new.text = "Error status: " + str(code.status_code)
            except Exception:
                new.text = str(b)
    elif typeex == "executefile":
        cod = None
        if c == "":
            ap = filedialog.askopenfile(title="Choose file")
            if ap:
                cod = ap.read()
            else:
                new.text = "No file chosen"
        elif c == "clip":
            cd = executor.clipboard_get()
            if cd == "":
                ap = filedialog.askopenfile(title="Choose file")
                if ap:
                    cod = ap.read()
                else:
                    new.text = "No file chosen"
            else:
                if os.path.exists(cd):
                    with open(cd,"r",encoding="utf-8") as code:
                        cod = code.read()
                else:
                    new.text = "No file"
                    return
        else:
            if os.path.exists(c):
                with open(c,"r",encoding="utf-8") as code:
                    cod = code.read()
            else:
                new.text = "No file"
                return
        try:
            foundsus(cod,typeex="executeprogram")
            destroy(new)
            new = None
            aienabled = True
        except BaseException as ex:
            new.text = str(ex)
m.cd = None
aud2 = None
if random.randint(1,20) == 1:
    g = Entity(model='cube',scale=(1,1,5),parent=p.camera_pivot,position=(1,1,0))
rain = 100
mellikrains = []
def foundsus(sus:str,typeex):
    global notsussy 
    global midgen
    midgen = False
    global setno
    global new
    types = []
    for i in forbiddencodeexecutions:
        if i in sus:
            if i in malwareexecutions:
                if not "Malware" in types:
                    types.append("Malware")
            elif i in trojanexecutions:
                if not "Trojan" in types:
                    types.append("Trojan")
            elif i in riskwares:
                if not "Riskware" in types:
                    types.append("Riskware")
    copystr = sus
    imports = 0
    importeds = []
    while "import" in copystr:
        pos = copystr.find("import")
        pos += 5
        if copystr[0:6] != "import":
            if copystr[pos+1:pos+2] == " " and copystr[pos-6:pos-5] == " ":
                copystr2 = copystr[pos+2:]
                copystr = copystr[pos+1:]
                print(copystr2)
                pos = copystr2.find(" ")
                if pos != -1:
                    importeds.append(copystr2[:pos])
                else:
                    importeds.append(copystr2)
                imports += 1
        else:
            copystr2 = copystr[pos+2:]
            copystr = copystr[pos+1:]
            print(copystr2)
            pos = copystr2.find(" ")
            if pos != -1:
                importeds.append(copystr2[:pos])
            else:
                importeds.append(copystr2)
            imports += 1
    connections = []
    copystr = sus 
    while "+" in copystr:
        pos = copystr.find("+")
        if '"' in copystr or "'" in copystr:
            pos2 = copystr.find("'")
            if pos2 == -1:
                pos2 = copystr.find('"')
                if pos2 != -1:
                    if pos2 < pos:
                        if checkfornonspaces(copystr[pos+1:pos2]) == False:
                            phr = copystr[:pos-1]
                            first = phr.find('"')
                            phr = phr[first + 1:]
                            phr = phr[:phr.find('"')]
                            phr2 = copystr[pos+1:]
                            sec = phr2.find('"')
                            loc = phr2[sec+1:]
                            thr = loc.find('"')
                            phr2 = loc[:thr]
                            connections.append(phr + phr2)
                            copystr = copystr[copystr.find(phr2)+len(phr2)+1:]
                else:
                    copystr = copystr[:pos] + copystr[pos+1:]
            else:
                if pos2 < pos:
                    if checkfornonspaces(copystr[pos+1:pos2]) == False:
                            phr = copystr[:pos-1]
                            first = phr.find("'")
                            phr = phr[first + 1:]
                            phr = phr[:phr.find("'")]
                            phr2 = copystr[pos+1:]
                            sec = phr2.find("'")
                            loc = phr2[sec+1:]
                            thr = loc.find("'")
                            phr2 = loc[:thr]
                            connections.append(phr + phr2)
                            copystr = copystr[copystr.find(phr2)+len(phr2)+1:]   
                else:     
                    copystr = copystr[:pos] + copystr[pos+1:]    
        else:
            copystr = copystr[:pos] + copystr[pos+1:]
    
    for i in connections:
        if i in forbiddencodeexecutions:
            if i in malwareexecutions:
                if not "Malware" in types:
                    types.append("Malware")
            elif i in trojanexecutions:
                if not "Trojan" in types:
                    types.append("Trojan")
            elif i in riskwares:
                if not "Riskware" in types:
                    types.append("Riskware")
        else:
            if not "Connection" in types:
                types.append("Connection")
    for i in importeds:
        if not i in notsussy:
            if not "Riskware" in types:
                types.append("Riskware")
    if len(types) > 0:
        a1 = Text("Я конечно понимаю что актуальный мемчик и тд(I understand you wanna see a tuff meme)",y=0.35,background=True,x=-0.7)
        a25 = Text("Но суть в том что ты словил не мемчик в коду(But the thing is that you didnt get a meme)",y=0.3,background=True,x=-0.7)
        text = "а возможно "
        if new != None:
            new.visible = False
        text2 = "instead you got a possible "
        for i in types:
            if i == "Trojan":
                text = text + "троянского коня который может украсть твои файлы"
                text2 = text2 + "trojan"
                if types.index("Trojan") == len(types) - 1:
                    text += " и "
                    text2 += " and "
                elif types.index("Trojan") < len(types) - 1:
                    text += ", "
                    text2 += ", "
                else:
                    pass
            elif i == "Malware":
                text = text + "вирусняка который может подорвать твой комп"
                text2 += "malware"
                if types.index("Malware") == len(types) - 2:
                    text += " и "
                    text2 += " and "
                elif types.index("Malware") < len(types) - 1:
                    text += ", "
                    text2 += ", "
                else:
                    pass
            elif i == "Riskware":
                text = text + "неизвестного вирусняка или не вирусняка так бывает"
                text2 += "riskware"
                if types.index("Riskware") == len(types) - 2:
                    text += " и "
                    text2 += " and "
                elif types.index("Riskware") < len(types) - 1:
                    text += ", "
                    text2 += ", "
                else:
                    pass         
            elif i == "Connection":
                text = text + "попытку склеивания вирусняка"
                text2 += "string connection attempt"
                if types.index("Connection") == len(types) - 2:
                    text += " и "
                    text2 += " and "
                elif types.index("Connection") < len(types) - 1:
                    text += ", "
                    text2 += ", "
                else:
                    pass                  
        a1.background.color = color.gray
        a25.background.color = color.gray
        a3 = Text(text,y=0.25,background=True,x=-0.7)
        a3.background.color = color.gray
        a4 = Text(text2,y=0.2,background=True,x=-0.7)
        a4.background.color = color.gray
        a5 = Text("Ну не суть короче вопрос хочешь все равно выполнить скрипт?(But that's not the point the question is do you wanna run the script?)",y=0.15,background=True,x=-0.8)
        a5.background.color = color.gray
        a6 = Text("Если вирусы есть то я ответсвенность за ущерб не несу(I am not liable for any damage caused by the software.)",y=0.1,background=True,x=-0.7)
        a6.background.color = color.gray
        a7 = Text("Подтвердите репорт в моем будущем дискорд канале если есть вирусы(Submit a virus report to my future discord channel if this is a virus)",y=0.05,x=-0.7,background=True)
        a7.background.color = color.gray
        mouse.locked = False
        yes = Button(text="Да(Yes)",x=-0.2,y=-0.45,scale=(0.1,0.1,.1),on_click=lambda: (bidoncommand(sus,typeex),destroyItems(a1=a1,a2=a25,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,yes=yes)))

        no = Button(text="Нет(No)",x=0.2,y=-0.45,scale=(.1,.1,.1),on_click=Func(noclicked,a1,a25,a3,a4,a5,a6,a7,yes))

        setno = no
    else:
        bidoncommand(sus,typeex)
def initializebarnacle():
    global barnacle
    global canplay
    canplay = True
    barnacle = Entity(model='cube',texture='barnaclebasic.mp4',scale=(5,12,5),position=(random.randint(-120,120),4,random.randint(-120,120)))
def initializeboxer():
    global boxer
    global canplay
    canplay = True
    boxer = Entity(model='cube',texture='boxerwalking.mp4',scale=(2,3,2),position=(random.randint(-120,120),0,random.randint(-120,120)),follow=False)
def initializerunner():
    global runner
    global canplay
    canplay = True
    runner = Entity(model='cube',texture='runner.mp4',scale=(2,3,2),position=(random.randint(-120,120),0,random.randint(-120,120)),follow=False)
def initializedrun():
    global drun
    global canplay
    canplay = True
    drun = Entity(model='cube',texture="drunflow.png",scale=(2,3,2),position=(random.randint(-60,60),0,random.randint(-60,60)),followreplay=False)
def initializemeatman():
    global meatman
    global meatmanstage
    global canplay
    canplay = True
    meatman = Entity(model='cube',texture='meatmanstage1.mp4',scale=(3,10,3),position=(random.randint(-60,60),0,random.randint(-60,60)),follow=False)
    meatmanstage = 1
def genrooms():
    global backroomroof
    global a
    global gameendentity
    global speed
    global generatedblocks
    global k
    global pdg
    global aienabled
    global canplay
    global aud2
    global sng
    if k != None:
        if k.enabled:
            destroy(k)
    k == None
    if pdg != None:
        if pdg.enabled:
            destroy(pdg)
    pdg = None
    if sng != None:
        if sng.enabled:
            sng.stop()
    sng = None
    if aud2 != None:
        if aud2.enabled:
            aud2.stop()
    aud2 = None
    aienabled = True
    Entity.default_shader = lit_with_shadows_shader
    f.texture = 'backroombottom.jpg'
    f.alpha = 1
    f.scale = (250,0,250)
    f.collider = 'box'
    canplay == True
    f.collision = True
    print(generatedblocks)
    for i in generatedblocks:
        if i.enabled:
            destroy(i)
    generatedblocks.clear()
    for i in range(backroomblocks):
        blockx = random.randint(-125,125)
        blockz = random.randint(-125,125)
        generatedblocks.append(Entity(position=(blockx,4,blockz),scale=(random.randint(5,40),12,1),texture='backroomwall.jpg',collider='box',model='cube',rotation=(0,random.randint(-360,360),0)))
    backroomroof = Entity(scale=(250,1,250),position=(0,10,0),texture='backroomtop.jpg',model='cube')
    gameendentity.position = (random.randint(-125,125),4,random.randint(-125,125))
    while gameendentity.x < 50 and gameendentity.x > -50 and gameendentity.z < 50 and gameendentity.z > -50:
        gameendentity.position = (random.randint(-125,125),4,random.randint(-125,125))
    gameendentity.scale = (2,12,2)
    gameendentity.color = color.white
    generatedblocks.append(Entity(scale=(250,12,1),position=(0,4,-125),texture='backroomwall.jpg',collider='box',model='cube'))
    generatedblocks.append(Entity(scale=(250,12,1),position=(0,4,125),texture='backroomwall.jpg',collider='box',model='cube'))
    generatedblocks.append(Entity(scale=(1,12,250),position=(-125,4,0),texture='backroomwall.jpg',collider='box',model='cube'))
    generatedblocks.append(Entity(scale=(1,12,250),position=(125,4,0),texture='backroomwall.jpg',collider='box',model='cube'))
    a.stop()
    a = Audio('stillhammam.mp3',loop=True)
    m.followplayer = True
    m.cd = False
    m.position = p.position
    m.collider = 'box'
    m.collision = True
    speed = 0.02
    initializedrun()
    initializerunner()
    initializeboxer()
    initializebarnacle()
    initializemeatman()
def mellrooms():
    global canplay
    global m
    m.cd = True
    Audio('blyat-mellstroy.mp3')
    f.collider = None
    f.collision = False
    p.collider = None
    canplay = True
    p.collision = False
    invoke(genrooms,delay=10)
def vlast():
    global k
    global m
    global aienabled
    global speed
    global p
    Audio('ia-poluchil-vlast-kotoraia-ne-snilas.mp3')
    p.speed = 35
    speed = 0.3
    aienabled = True
    k.targetplayer = True
def sound():
    global aud2
    aud2.stop()
    Audio('nu-chto-eshchio.mp3')
    invoke(vlast,delay=3)
def vovchik():
    global k
    global aud2
    aud2 = Audio("etopizda.wav")
    if k != None:
        k.position = (-3,2,80)
    else:
        k = Entity(model='cube',scale=(2,3,2),texture='images2.jpg',position=(80,2,0))
        k.targetplayer = False
        k.position = (-3,2,80)
    invoke(sound,delay=6)
def krasni():
    global m
    Audio('ia-uzhe-krasnyi.mp3')
    if type(m) == Entity:
        m.position = (3,2,80)
    invoke(vovchik,delay=4)
def freeze():
    global frostmourne
    global generatedblocks
    global gameendentity
    global f
    Audio('ne-kto-ne-smeet-mne-prikazyvat.mp3')
    frostmourne.anim = True
    frostmourne.polation = (0,-5,78)
    for i in generatedblocks:
        i.color = color.cyan
        i.texture = "ice.jpg"
    f.color = color.cyan
    f.scale = (100,1,200)
    f.texture = "ice.jpg"
    gameendentity.color = color.white
    gameendentity.alpha = 1
    gameendentity.scale = (100,8,2)
    p.position = (0,3,70)
    invoke(krasni,delay="2")
def pudge():
    global pdg
    global sng
    global a
    global a2
    pdg = Entity(model='cube',scale=(2,3,2),texture='pudge.jpg',position=(0,2,-80))
    if type(a) == Audio:
        a.stop()
    if type(a2) == Audio:
        a2.stop()
    sng = Audio('countdown.mp3')
    invoke(onehook,delay=45,ind=0)
def hookoutloop(hk,mn,i,index):
    try:
        global pdg
        if distance(hk,i) > 2 and mn.scale_z < 100:
            hk.look_at(i)
            mn.look_at(i)
            hk.position += hk.forward * time.dt * 300
            mn.position += hk.forward * time.dt * 150
            mn.scale_z = distance(hk,pdg)
            invoke(hookoutloop,i=i,mn=mn,hk=hk,index=index,delay=0.005)
        else:
            hookinloop(hk,mn,i,index)
    except Exception:
        pass
def nobodydarestocommandme():
    global aienabled
    global ap
    global arthas
    global frostmourne
    global gameendentity
    global g
    global generatedblocks
    global a
    global a2
    if ap != None:
        if ap.enabled:
            destroy(ap)
    if g != None:
        if g.enabled:
            destroy(g)
    g = None
    ap = None
    if isinstance(a,Audio):
        a.stop()
    if isinstance(a2,Audio):
        a2.stop()
    z = -50
    x = -50
    for i in generatedblocks:
        if generatedblocks.index(i) <= 125:
            i.moveto = (z,0,x)
            x += 0.8
        else:
            z = 50
            i.moveto = (z,0,x)
            x -= 0.8
    aienabled = False
    gameendentity.moveto = (0,0,-100)
    arthas = Entity(model='cube',scale=(2,3,2),texture='arthas.jpg',position=(0,2,80))
    frostmourne = Entity(model='cube',scale=(1,5,1),texture='frostmorn.jpg',position=(0,2,78))
    frostmourne.anim = None
    frostmourne.polation = None
    p = Audio('phonk.mp3')
    invoke(freeze,delay=5)
def hookinloop(hk,mn,i,index):
    try:
        global pdg
        global falling
        if distance(hk,pdg) > 2 and hk.z > pdg.z and mn.z > pdg.z and mn.scale_z < 100:
            hk.position -= hk.forward * time.dt * 300
            mn.position -= hk.forward * time.dt * 150
            mn.scale_z = distance(hk,pdg)
            i.position -= hk.forward * time.dt * 300
            invoke(hookinloop,i=i,mn=mn,hk=hk,index=index,delay=0.005)
        else:
            destroy(hk)
            destroy(mn)
            falling.append(i)
            onehook(ind=index+1)
    except Exception:
        pass
def onehook(ind:int):
    try:
        global aienabled
        global lasthook
        global lastend
        aienabled = False
        global pdg 
        global fullblockpack
        i = fullblockpack[ind]
        Audio('Meat_Hook_alt.mp3')
        hk = Entity(color=color.red,scale=(1,1,1),model='cube')
        lastend = hk
        hk.position = pdg.position
        mn = Entity(color=color.red,scale=(1,1,1),model='cube')
        mn.position = pdg.position
        lasthook = mn
        hookoutloop(hk,mn,i,ind)
    except Exception:
        return
def custombidonprogram():
    global new
    global aienabled
    mouse.locked = False
    if new == None:
        new = TextField()
    
        new.text = "Do custom bidon program make custom comand an writ executeprogram at end or ad file wit executefile at end or execut raw link wit executelink at end and replac cod wit clip at start to execut cod from clipbord"
    else:
        destroy(new)
        new = None
        mouse.locked = True
        aienabled = True
def obeshpechenie():
    global a2
    global fullblockpack
    global k
    if k != None:
        destroy(k)
        k = None
    a2 = Audio('programobespech.mp3',loop=True)
    k = Entity(model='cube',scale=(2,3,2),texture='images2.jpg',position=(80,2,0))
    k.targetplayer = False
    fullblockpack.append(k)
def knock():
    global ap
    ap = Entity(position=(0,0,100),scale=(150,10,3),color=color.yellow,collider='box',model='cube')
    global diecounter
    diecounter += 1
    global prevlose
    prevlose = True
    global prevwin
    prevwin = False
    invoke(initi,delay=20)
def mellrainevent():
    global aienabled
    global txt
    aienabled = False
    txt = Text('Mellstroy is pidor',color=color.red,x=-0.42,y=0,scale=5)
    generatedblocks.append(txt)
    mellikrain()
def mellikrain():
    global rain
    global mellikrains
    if rain > 0:
        blockx = random.randint(xgen[0],xgen[1])
        blockz = random.randint(zgen[0],zgen[1])
        s = Entity(model='cube',scale=(2,3,2),texture='images.jpg',position=(blockx,25,blockz))
        s.lifetime = falllifetime
        mellikrains.append(s)
        rain -= 1
        invoke(mellikrain,delay=0.1)
def impossiblespeed():
    global speed
    speed = 1
def delaydestroy(item):
    try:
        destroy(item)
    except Exception:
        pass
def initi():
    global bobi
    global speedmulti
    global escapados
    global falling
    global lasthook
    global lastend
    global sng
    global arthas
    global frostmourne
    global noescapados
    global mellikrains
    global pdg
    global multiplier
    global aud2
    global runnerrage
    global ragestate
    global canplay
    global alive
    global counter
    global diecounter
    global meatman, meatmanrage, meatmanstage
    global aienabled
    global checks
    global speed
    global rain
    global fullblockpack
    global p
    global a2
    global k
    global barnacle
    global barnaclerage
    global f
    global a
    global runner
    global boxer, boxerrage, hits
    global backroomroof
    global m
    global ap
    global gameendentity
    global generatedblocks
    global psong
    global drun
    global g
    global guarantee
    runnerrage = False
    ragestate = False
    boxerrage = False
    checks = 0
    hits = 0
    if boxer != None:
        if boxer.enabled:
            destroy(boxer)
    boxer = None
    if frostmourne != None:
        if frostmourne.enabled:
            destroy(frostmourne)
    frostmourne = None
    if arthas != None:
        if arthas.enabled:
            destroy(arthas)
    arthas = None
    meatmanstage = 1
    meatmanrage = False
    if meatman != None:
        if meatman.enabled:
            destroy(meatman)
    if aud2 != None:
        if aud2.enabled:
            destroy(aud2)
    aud2 = None
    if sng != None:
        if sng.enabled:
            sng.stop(True)
    sng = None
    if barnacle != None:
        if barnacle.enabled:
            destroy(barnacle)
    barnacle = None
    barnaclerage = False
    canplay = True
    if runner != None:
        if runner.enabled:
            destroy(runner)
    runner = None
    fullblockpack = []
    if backroomroof != None:
        if backroomroof.enabled:
            destroy(backroomroof)
    backroomroof = None
    if pdg != None:
        if pdg.enabled:
            destroy(pdg)
    pdg = None
    bobi = False
    if g != None:
        if g.enabled:
            destroy(g)
    g = None
    if k != None:
        if k.enabled:
            destroy(k)
    k = None
    if a2 != None:
        if a2.enabled:
            destroy(a2)
    a2 = None
    if lasthook != None:
        if lasthook.enabled:
            destroy(lasthook)
    lasthook = None
    if lastend != None:
        if lastend.enabled:
            destroy(lastend)
    lastend = None
    alive = False
    if drun != None:
        if drun.enabled:
            destroy(drun)
    drun = None
    guarantee = False
    Entity.default_shader = 'unlit_shader'
    aienabled = True
    if (counter % 10) == 0 and prevwin == True:
        speedmulti += 1
        t = Text(str(counter) + ' win speed ' + str(speedmulti) + ' x',color=color.red,x=-0.7,y=0,scale=5)
        invoke(delaydestroy,item=t,delay=5)
    elif (diecounter % 10) == 0 and prevlose:
        if speedmulti > 1:

            speedmulti -= 1
            if speedmulti == 0:
                speedmulti += 1
            t = Text(str(diecounter) + ' die speed minus 1x speed ' + str(speedmulti),color=color.red,x=-0.7,y=0,scale=5)
            invoke(delaydestroy,item=t,delay=5)
    escapados.text = 'Win game: ' + str(counter)
    noescapados.text = 'Die game: ' + str(diecounter)
    if os.path.exists('pidor.json'):
        with open('pidor.json','r',encoding='utf-8') as l:
            alive = json.load(l)
            print(alive)
    if os.path.exists('guarantee.json'):
        try:
            with open('guarantee.json','r',encoding='utf-8') as al:
                guarantee = json.load(al)
                print(guarantee)
            with open('guarantee.json','w',encoding='utf-8') as al:
                json.dump(False,al)
        except Exception:
            guarantee = False
            os.remove('guarantee.json')
    speed = 0.04
    p.speed = 10
    for i in range(speedmulti):
        if i != speedmulti != 1:
            p.speed *= multiplier
            speed *= multiplier
    if alive == True:
        if random.randint(1,10) == 1 or guarantee:
            speed *= 5
        else:
            speed *= 2
        Audio('ia-uzhe-krasnyi.mp3')
    psong = True
    if f != None:
        if f.enabled:
            destroy(f)
    a.stop()
    if m != None:
        if m.enabled:
            destroy(m)
    if ap != None:
        if ap.enabled:
            destroy(ap)
    ap = None
    destroy(gameendentity)
    for i in generatedblocks:
        if i.enabled:
            destroy(i)
    generatedblocks.clear()
    for i in mellikrains:
        if i.enabled:
            destroy(i)
    for i in range(blocks):
        blockx = random.randint(xgen[0],xgen[1])
        blockz = random.randint(zgen[0],zgen[1])
        if i != 50:
            generatedblocks.append(Entity(model='cube',scale=(2,8,2),collider='box',color=color.yellow,alpha=0.5,position=(blockx,0,blockz)))
        else:
            randomvalue = random.randint(1,2)
            if randomvalue == 1:
                while blockx > -minimuxexitdistx:
                    blockx = random.randint(xgen[0],xgen[1])
            else:
                while blockx < minimuxexitdistx:
                    blockx = random.randint(xgen[0],xgen[1])
            r2 = random.randint(1,2)
            if r2 == 1:
                while blockz > -minimuxexitdistz:
                    blockz = random.randint(xgen[0],xgen[1])
            else:
                while blockz < minimuxexitdistz:
                    blockz = random.randint(xgen[0],xgen[1])
            gameendentity = Entity(model='cube',scale=(2,8,2),collider='box',color=color.green,alpha=0.5,position=(blockx,0,blockz))
            gameendentity.moveto = None
    for i in generatedblocks:
        i.moveto = None
        fullblockpack.append(i)
    rain = 100
    mellikrains = []
    f = Entity(model='cube',scale=(100,1,100),color=color.yellow,collider='box',alpha=0.5,position=(0,-2,0))
    a = Audio('am-am-am-am-mellstroy.mp3',loop=True)
    m = Entity(model='cube',scale=(2,3,2),texture='images.jpg',position=(0,2,80),followplayer=False)
    fullblockpack.append(m)
    fullblockpack.append(p)
    m.cd = None
    if random.randint(1,20) == 1:
        g = Entity(model='cube',scale=(1,1,5),parent=p.camera_pivot,position=(1,1,0))
    p.position = (0,20,0)
    p.collider = 'box'
    p.collision = True
    if random.randint(1,20) == 1:
        mellrainevent()
    else:
        checks += 1
    if random.randint(1,25) == 1:
        impossiblespeed()
    else:
        checks += 1
    if random.randint(1,15) == 1:
        knock()
    else:
        checks += 1
    if random.randint(1,18) == 1:
        obeshpechenie()
    else:
        checks += 1
    if random.randint(1,27) == 1:
        pudge()
    else:
        checks += 1
    if random.randint(1,40) == 1:
        nobodydarestocommandme()
    else:
        checks += 1
    if checks == 6:
        if random.randint(1,50) == 1:
            mellrooms()
def guarantee_speed():
    with open('guarantee.json','w',encoding='utf-8') as g:
        json.dump(True,g)
    print("He speed 100%")
def input(key):
    global aienabled
    global g
    global new
    global speedmulti
    if new == None:
        if key == 'b':
            aienabled = False
        elif key == 'k':
            aienabled = True
        elif key == 'l':
            p.position = gameendentity.position
        elif key == 'm':
            mellrainevent()
        elif key == 'n':
            impossiblespeed()
        elif key == 'o':
            knock()
        elif key == 'u':
            guarantee_speed()
        elif key == "-":
            if speedmulti > 1:
                speedmulti -= 1
        elif key == "=":
            speedmulti += 1
        elif key == 'left mouse down':
            if g != None:
                shoot(g)
        elif key == "j":
            obeshpechenie()
            print("suka ebani cheater")
        elif key == "v" and g == None:
            g = Entity(model='cube',scale=(1,1,5),parent=p.camera_pivot,position=(1,1,0))
        elif key == "y":
            custombidonprogram()
        elif key == "c":
            pudge()
        elif key == "h":
            nobodydarestocommandme()
        elif key == "g":
            mellrooms()
def closestblockto(targ:Entity):
    currentdist = 1000000
    block = None
    for i in generatedblocks:
        if not type(i) == Text:
            if distance(targ,i) < currentdist:
                currentdist = distance(targ,i)
                block = i
    return currentdist, block
def checkiffreepath(targ:Entity):
    xm = targ.x - 1
    xp = targ.x + 1
    zm = targ.z - 1
    zp = targ.z + 1
    dst, bl = closestblockto(targ)
    if dst > 2:
        return True, []
    else:
        paths = []
        if abs(bl.x - xm) < 2:
            paths.append('leftx')
        if abs(bl.x - xp) < 2:
            paths.append('rightx')
        if abs(bl.z - zm) < 2:
            paths.append('leftz')
        if abs(bl.z - zp) < 2:
            paths.append('rightz')
        return False, paths
def pathfind(targ:Entity,to,adspeed=1):
    global aienabled
    global speed
    if aienabled:
        var, paths = checkiffreepath(targ)
        targ.look_at(to)
        if len(paths) == 4 or var == True:
            targ.position += targ.forward * time.dt * speed * 70 * adspeed
            return
        x = 0
        z = 0
        if 'leftx' in paths and not 'rightx' in paths:
            x = 5
        elif not 'leftx' in paths and 'rightx' in paths:
            x = -5
        if 'leftz' in paths and not 'rightz' in paths:
            z = 5
        elif not 'leftz' in paths and 'rightz' in paths:
            z = -5
        if len(paths) == 4 or x + z == 0:
            Audio('ia-zapert-na-etom-ostrove-izza-interpola.mp3')
        if x + z == 0:
            targ.position += targ.forward * time.dt * speed * 70
            return              
        targ.x += x * time.dt * speed * 70 * adspeed
        targ.z += z * time.dt * speed * 70 * adspeed
def boxermove():
    global boxer
    global canplay
    boxer.follow = True
    boxer.texture = "boxerwalking.mp4"
    canplay = True
def meatmanreset():
    sys.exit()
def move(targ:Entity,to):
    global canplay
    global psong
    global m
    global prevwin
    global k
    global drun
    global runnerrage
    global ragestate
    global boxer
    global barnacle
    global hits
    global boxerrage
    global runner
    global prevlose
    global meatman, meatmanrage
    global a
    global p
    global diecounter
    global f
    global a2
    targ.look_at(to)
    if aienabled:
        if targ != k and targ != drun and to != drun and targ != runner and to != runner and targ != boxer and to != boxer and targ != meatman and to != meatman:
            pathfind(targ,to)
        elif targ == k:
            if k.targetplayer == False:
                pathfind(targ,to,2)
            else:
                pathfind(targ,to)
        elif targ == drun:
            pathfind(targ,to,10)
        elif to == drun or to == runner or to == boxer or to == meatman:
            pathfind(targ,to,25)
        elif targ == runner:
            pathfind(targ,to,30)
        elif targ == boxer:
            pathfind(targ,to,100)
        elif targ == meatman:
            pathfind(targ,to,15)
    if targ == m:
        if psong:
            if m.followplayer == False:
                if distance(targ,to) < 2:
                    if canplay:
                        canplay = False
                        Audio('2026-10-06-08-42-49 (mp3cut.net).mp3')
                        a.stop()
                        f.collider = None
                        f.collision = False
                        p.collider = None
                        p.collision = False
                        diecounter += 1
                        prevlose = True
                        prevwin = False
                        invoke(initi,delay=5)
        if to == drun:
            if distance(targ,to) < 2:
                if canplay:
                    canplay = False
                    ragestate = False
                    Audio('2026-10-06-08-42-49 (mp3cut.net).mp3')
                    destroy(drun)
                    drun = None     
                    initializedrun()    
        elif to == runner:
            if distance(targ,to) < 2:
                if canplay:
                    canplay = False
                    runnerrage = False
                    Audio('2026-10-06-08-42-49 (mp3cut.net).mp3')
                    destroy(to)
                    runner = None   
                    initializerunner()
        elif to == boxer:
            if distance(targ,to) < 2:
                if canplay:
                    canplay = False
                    boxerrage = False
                    Audio('2026-10-06-08-42-49 (mp3cut.net).mp3')
                    destroy(to)
                    boxer = None   
                    initializeboxer()
        elif to == barnacle:
            if distance(targ,to) < 2:
                if canplay:
                    canplay = False
                    Audio('2026-10-06-08-42-49 (mp3cut.net).mp3')
                    destroy(to)
                    barnacle = None   
                    initializebarnacle()   
        elif to == meatman:
            if distance(targ,to) < 2:
                if canplay:
                    canplay = False
                    meatmanrage = False
                    Audio('2026-10-06-08-42-49 (mp3cut.net).mp3')
                    destroy(to)
                    meatman = None   
                    initializemeatman()                   
    elif to == m:
        if distance(targ,to) < 5:
            if m.cd == None:
                Audio('etopizda.wav')
                if a2 != None:
                    a2.stop()
                m.cd = True
                a.stop()
    elif to == p and targ == k:
        if distance(targ,to) < 2:
            if canplay:
                canplay = False
                Audio('etopizda.wav')
                a.stop()
                f.collider = None
                f.collision = False
                p.collider = None
                p.collision = False
                diecounter += 1
                prevlose = True
                prevwin = False
                invoke(initi,delay=5)
    elif to == p and targ != k and targ != m and targ != boxer and targ != meatman:
        if distance(targ,to) < 2:
            if canplay:
                canplay = False
                a.stop()
                f.collider = None
                f.collision = False
                p.collider = None
                p.collision = False
                diecounter += 1
                prevlose = True
                prevwin = False
                invoke(initi,delay=5)
    elif targ == boxer and to == p:
        if distance(targ,to) < 2:
            if canplay:
                canplay = False
                targ.follow = False
                targ.texture = "boxerhit.mp4"
                Audio("boxerhit.mp3")
                if hits < 5:
                    hits += 1
                    invoke(boxermove,delay=1.5)
                else:
                    a.stop()
                    f.collider = None
                    f.collision = False
                    p.collider = None
                    p.collision = False
                    diecounter += 1
                    prevlose = True
                    prevwin = False
                    invoke(initi,delay=5)  
    elif targ == meatman and to == p:
        if distance(targ,to) < 2:
            if canplay:
                canplay = False
                targ.follow = False
                targ.texture = "meatmanstage3.mp4"
                Audio('meatmanstage3.mp3')
                invoke(meatmanreset,delay=2.5)    
if random.randint(1,20) == 1:
    mellrainevent()
else:
    checks += 1
if random.randint(1,25) == 1:
    impossiblespeed()
else:
    checks += 1
if random.randint(1,15) == 1:
    knock()
else:
    checks += 1
if random.randint(1,18) == 1:
    obeshpechenie()
else:
    checks += 1
if random.randint(1,27) == 1:
    pudge()
else:
    checks += 1
if random.randint(1,40) == 1:
    nobodydarestocommandme()
else:
    checks += 1
if checks == 6:
    if random.randint(1,50) == 1:
        mellrooms()
def infvoke():
    global drun
    Audio('drunrunning.mp3')
    if drun != None:
        if drun.followreplay == True:
            invoke(infvoke,delay=1)
def drunloop():
    global drun
    if drun != None:
        drun.texture = 'drunrunning.mp4'
        Audio('drunrunning.mp3')
        drun.followreplay = True
        invoke(infvoke,delay=1)
def ragedrun():
    global drun
    drun.texture = "drunstart.mp4"
    Audio('drunstart.mp3')
    invoke(drunloop,delay=3)
def runnerrageinf():
    global runner
    if runner != None:
        if runner.follow == True:
            Audio('runner.mp3')
            invoke(runnerrageinf,delay=5)
def boxerrageinf():
    global boxer
    if boxer != None:
        if boxer.follow == True:
            Audio('boxerwalking.mp3')
        invoke(boxerrageinf,delay=3)
def meatmanrageinf():
    global meatman
    if meatman != None:
        if meatman.follow == True:
            Audio('meatmanstage1.mp3')
        invoke(meatmanrageinf,delay=3.5)
def runnerrager():
    global runner
    Audio('runner.mp3')
    runner.follow = True
    invoke(runnerrageinf,delay=5)
def meatmanstage2inti():
    global meatman
    global meatmanstage
    Audio('meatmanstage2.mp3')
    meatmanstage = 2
    meatman.follow = True
    invoke(meatmanrageinf,delay=4.5)
def meatmanrager():
    global meatman
    Audio('meatmanstage1.mp3')
    invoke(meatmanstage2inti,delay=3.5)
def boxerrager():
    global boxer
    Audio('boxerwalking.mp3')
    boxer.follow = True
def shoot(g:Entity):
    global bulletspeed
    global p
    global bullets
    en = Entity(model='cube',parent=p.camera_pivot,position=(1,1,0), collider='box',color=color.black)
    en.lifetime = 50
    en.speed = bulletspeed
    bullets.append(en)
def getmellstroycondition():
    global m
    global drun
    global barnacle
    global p
    global boxer
    global meatman
    global runner
    if drun == None and boxer == None and runner == None and barnacle == None and meatman == None:
        return p
    else:
        nearestd = 1000000
        nearest = None
        if boxer != None:
            if distance(m,boxer) < nearestd:
                nearestd = distance(boxer,m)
                nearest = boxer
        if drun != None:
            if distance(m,drun) < nearestd:
                nearestd = distance(drun,m)
                nearest = drun
        if barnacle != None:
            if distance(m,barnacle) < nearestd:
                nearestd = distance(barnacle,m)
                nearest = barnacle
        if runner != None:
            if distance(m,runner) < nearestd:
                nearestd = distance(runner,m)
                nearest = runner
        if meatman != None:
            if distance(m,meatman) < nearestd:
                nearestd = distance(meatman,m)
                nearest = meatman
        if nearestd < 15:
            return nearest
        else:
            return p
        
def reset():
    global a, f, p, diecounter, prevlose, prevwin, initi, barnaclerage
    barnaclerage = False
    a.stop()
    f.collider = None
    f.collision = False
    p.collider = None
    p.collision = False
    diecounter += 1
    prevlose = True
    prevwin = False
    invoke(initi,delay=5)       
def barnacleattack():
    global barnacle
    barnacle.texture = "barnacleattack.mp4"
    Audio("barnacleattack.mp3")
    invoke(reset,delay=2.5)
def update():
    global aienabled
    global aimodel
    global p
    global frostmourne
    global ap
    global drun
    global aitokens
    global boxer
    global boxerrage
    global meatman, meatmanrage
    global barnacle
    global barnaclerage
    global runner
    global k
    global generatedblocks
    global runnerrage
    global ragestate
    global gameendentity
    global m
    global new
    for i in generatedblocks:
        if type(i) == Entity:
            if hasattr(i,"moveto"):
                if i.moveto != None:
                    if abs(i.position - i.moveto) > 1:
                        empty = []
                        for u in i.moveto:
                            empty.append(u * 0.01)
                        moveps = tuple(empty)
                        i.position += moveps
    if gameendentity.moveto != None:
        if abs(gameendentity.position - gameendentity.moveto) > 0.2:
            gameendentity.position = lerp(gameendentity.position,gameendentity.moveto,time.dt * 3)
    global mellikrains
    if frostmourne != None:
        if frostmourne.anim == True:
            frostmourne.position = lerp(frostmourne.position,frostmourne.polation,time.dt * 2)
    if new != None:
        aienabled = False
        if new.text.find("executeprogram") != -1:
            t = new.text[:new.text.find("executeprogram")]
            new.text = "Do custom bidon program make custom comand an writ executeprogram at end or executerobot at end to generat code or ad file wit executefile at end or execut raw link wit executelink at end and replac cod wit clip at start to execut cod from clipbord"
            foundsus(t,typeex='executeprogram')
        elif new.text.find("executelink") != -1:
            t = new.text[:new.text.find("executelink")]
            bidoncommand(t,typeex="executelink")
        elif new.text.find('executefile') != -1:
            t = new.text[:new.text.find("executefile")]
            bidoncommand(t,typeex="executefile")
        elif new.text.find('executerobot') != -1:
            t = new.text[:new.text.find("executerobot")]
            Thread(target=custombidonrobotprogram,args=(t,aimodel,aitokens)).start()
            new.text = 'Don close while generat'
        elif new.text[:6] == 'model=':
            aimodel = new.text[6:]
            new.text = "Do custom bidon program make custom comand an writ executeprogram at end or executerobot at end to generat code or ad file wit executefile at end or execut raw link wit executelink at end and replac cod wit clip at start to execut cod from clipbord"
        elif new.text[:6] == 'token=':
            text = aitokens
            try:
                text = int(new.text[6:])
            except Exception:
                pass
            aitokens = text
            new.text = "Do custom bidon program make custom comand an writ executeprogram at end or executerobot at end to generat code or ad file wit executefile at end or execut raw link wit executelink at end and replac cod wit clip at start to execut cod from clipbord"
        elif new.text == "end":
            custombidonprogram()
    for i in bullets:
        i.position += i.forward * time.dt * i.speed
        i.lifetime -= 1
        if i.lifetime <= 0:
            destroy(i)
            bullets.remove(i)
        try:
            if distance(i,m) < 5:
                if m.cd != True:
                    Audio('aiaiai.mp3')
                    m.cd = True
        except Exception:
            pass
    if drun != None:
        if distance(drun,p) < 15:
            if ragestate == False:
                ragestate = True
                ragedrun()
        if drun.followreplay == True:
            move(drun,p)
    if runner != None:
        if distance(runner,p) < 15:
            if runnerrage == False:
                runnerrage = True
                runnerrager()
        if runner.follow == True:
            move(runner,p)
    if boxer != None:
        if distance(boxer,p) < 15:
            if boxerrage == False:
                boxerrage = True
                boxerrager()
        if boxer.follow == True:
            move(boxer,p)
    if barnacle != None:
        if abs(barnacle.x - p.x) < 2.5:
            if abs(barnacle.z - p.z) < 2.5:
                if barnaclerage == False:
                    barnaclerage = True
                    barnacleattack()
    if meatman != None:
        print(distance(meatman,p))
        if distance(meatman,p) < 15:
            if meatmanrage == False:
                meatmanrage = True
                meatmanrager()
        if meatman.follow == True:
            move(meatman,p)

    if ap != None:
        ap.z -= 0.25
        dist = abs(ap.z - p.z)
        if dist < 2 and dist > -2:
            p.position = (p.x,p.y,p.z - 0.25)
            print(True)
        dist = abs(ap.z - m.z)
        if dist < 2 and dist > -2:
            m.z -= 0.25
        dist = abs(ap.z - gameendentity.z)
        if dist < 2 and dist > -2:
            gameendentity.z -= 0.25
        for i in generatedblocks:
            dist = abs(ap.z - i.z)
            if dist < 2 and dist > -2:
                i.z -= 0.25
    for i in mellikrains:
        try:
            i.y -= time.dt * random.randint(10,40)
            i.lifetime -= 1
        except Exception:
            pass
        if i.lifetime <= 0:
            destroy(i)
            mellikrains.remove(i)
    if m.cd != True:
        move(m,getmellstroycondition())
    else:
        if aienabled:
            try:
                m.y -= .25
            except Exception:
                pass
    for i in falling:
        try:
            i.y -= .25
        except Exception:
            falling.remove(i)
    if k != None:
        if k.targetplayer == False:
            move(k,m)
        else:
            move(k,p)
    global canplay
    global bobi
    if distance(p,gameendentity) < 4:
        if not bobi:
            print("Hammam")
            global psong
            bobi = True
            global counter
            aienabled = False
            canplay = True
            if psong:
                psong = False
                Audio('lv_0_20261006114409.mp3')
                counter += 1
            invoke(initi,delay=10)
            txt = Text('You win game',color=color.black,x=-0.35,y=0,scale=5)
            generatedblocks.append(txt)
            global prevlose
            prevlose = False
            global prevwin
            prevwin = True
    with open('pidor.json',"w",encoding='utf-8') as f:
        json.dump(canplay,f)
    if p.y < -100 and canplay == True:
        p.position = (0,100,0)
scr.run()