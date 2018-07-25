#lib import
import sys, os, shutil
sys.path.append('..\\..\\')
import derpapi
import pygame
import github as git
from urllib.request import urlretrieve as GET

RUN = False

#screen init
try:
    pygame.init()
except:
    pygame.display.init()

def install(app_files, name):
    if os.path.exists('..\\' + name):
        shutil.rmtree('..\\' + name)
    print(app_files)
    print(name)
    os.mkdir('..\\' + name)
    pys = []
    for file in app_files:
        ipath = '..\\'
        mkpath = file[1].split('/')[:len(file[1].split('/')) - 1]
        for folder in mkpath:
            ipath = ipath + '\\' + folder
            if not os.path.exists(ipath):
                os.mkdir(ipath)
        GET(file[0], ipath + '\\' + file[1].split('/')[len(file[1].split('/')) - 1])
        if file[0].endswith('.py'):
            print(ipath + '\\' + file[1].split('/')[len(file[1].split('/')) - 1])
            pys.append(ipath + '\\' + file[1].split('/')[len(file[1].split('/')) - 1])
    for f in pys:
        pyfile = open(f, 'r')
        _code = pyfile.read()
        code = []
        for i in _code:
            code.append(i)
        c = 0
        for i in code:
            if i == '\\' and code[c + 1] == '\\':
                code.pop(c + 1)
                code[c] = '/'
            c += 1
        pyfile.close()
        pyfile = open(f, 'w')
        pyfile.write(''.join(code))
        pyfile.close()

def main():
    global RUN, derpapi, git, pygame, install, GET
    
    #place main code here
    screen = pygame.display.set_mode([480, 320], pygame.NOFRAME)
    screen.fill((230,230,230))
    
    try:
        font = pygame.font.Font('..\\..\\font_main.otf', 32)
    except:
        font = pygame.font.Font('font_main.otf', 32)
    screen.blit(font.render('LOADING...', True, (0,0,0)), (10, 10))
    pygame.display.flip()
    #load _apps from github
    store = git.Github('iTecAI', 'Mi$ita6hc')
    CStore = store.get_user().get_repo('Derpi-apps').get_contents('/STORE/')
    _apps = {}
    for i in CStore:
        _apps[i.path] = []
    app_display = {}
    for app in _apps.keys():
        dirs = [app]
        app_display[app.split('/')[len(app.split('/')) - 1]] = app
        while len(dirs) > 0:
            cur_dirs = dirs
            dirs = []
            for i in cur_dirs:
                for file in store.get_user().get_repo('Derpi-apps').get_contents(i):
                    if file.type == 'dir':
                        dirs.append(file.path)
                    else:
                        _apps[app].append([file.download_url, file.path.strip('STORE/')])               
    #start store

    #load images
    l_arrow = pygame.image.load('img\\LArrow.png')
    r_arrow = pygame.image.load('img\\RArrow.png')
    download = pygame.image.load('img\\download.png')

                        
    RUN = True
    selected = 0
    while RUN:
        screen.fill((230,230,230))
        screen.blit(l_arrow, (10, 10))
        screen.blit(r_arrow, (440, 10))
        screen.blit(download, (215, 10))
        screen.blit(font.render(list(app_display.keys())[selected], True, (0,0,0)), ((len(list(app_display.keys())[selected]) * 27) / 2, 150))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if derpapi.collision((10, 10), (30, 30), event.pos):
                    selected -= 1
                    if selected < 0:
                        selected = len(list(app_display.keys())) - 1
                if derpapi.collision((440, 10), (30, 30), event.pos):
                    selected += 1
                    if selected == len(list(app_display.keys())):
                        selected = 0
                if derpapi.collision((215, 10), (50, 50), event.pos):
                    install(_apps[app_display[list(app_display.keys())[selected]]], list(app_display.keys())[selected])
                print(selected)
            if event.type == pygame.KEYDOWN:
                print(event.unicode)
                if event.unicode == 'x':
                    print('EX')
                    pygame.quit()
                    sys.exit()
main()
pygame.display.quit()
