#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import re
import os
from art import *
from termcolor import cprint
from Manga_scanReader import reader
version = 1.2

def find_image_link(source, _manga_):
    #Return the link for the page.
    img_src_splitted = re.split('src=|"|/>', str(source))
    elemen_to_remove=[]
    for e in range(len(img_src_splitted)):
        if f"{_manga_}" in img_src_splitted[e]:
            pass
        else:
            elemen_to_remove.append(img_src_splitted[e])
    for i in range(len(elemen_to_remove)):
        img_src_splitted.remove(elemen_to_remove[i])
    return img_src_splitted[0].split()[0]

def get_pages(_url_):
    #Return the size of the chapter selected.
    p = requests.get(_url_).text
    src_page=BeautifulSoup(p, 'lxml')
    num_of_pages=src_page.find_all('img', class_='img-responsive')
    return len(num_of_pages)

def get_name_fillable(_manga_name_):
    if type(_manga_name_)==str:
        manga_name=_manga_name_.split(' ')
    elif type(_manga_name_)==list:
        manga_name=_manga_name_
    else:
        raise TypeError
    remove_space=0
    for e in range(len(manga_name)):
        if manga_name[e]=='':
            remove_space+=1
    for e in range(remove_space):
        manga_name.remove('')
    if len(manga_name)==0:
        cprint(f'Le nom sélectionné est invalide.', 'red')
        return None
    elif len(manga_name)==1:
        return str(manga_name[0].lower())
    elif len(manga_name)==2: 
        manga_name_fillable=manga_name[0].lower()+'-'+manga_name[1].lower()
        return manga_name_fillable
    elif len(manga_name)==3:
        manga_name_fillable=manga_name[0].lower()+'-'+manga_name[1].lower()+'-'+manga_name[2]
        return manga_name_fillable
    else:
        cprint(f'Cette version du logiciel ({version}) ne peut gérer des noms composé de plus de 3 mots.', 'red')
        return None
    
def get_is_available(_url_, _chapter_, _manga_):
    p = requests.get(_url_).text
    src_page=BeautifulSoup(p, 'lxml')
    chapter_available= src_page.find("ul", class_="chapters")
    #print(f"https://manga-fr.me/lecture-en-ligne/scan-{_manga_}/{_chapter_}")
    if f"https://manga-fr.me/lecture-en-ligne/scan-{_manga_}/{_chapter_}" in str(chapter_available):
        if not requests.get(f"https://manga-fr.me/lecture-en-ligne/scan-{_manga_}/{_chapter_}").ok:
            return False
        else:
            return True
    else:
        return False

def remove_space_from_list(_manga_value_):
    remove_space=0
    for e in range(len(_manga_value_)):
        if _manga_value_[e]=='':
            remove_space+=1
    for e in range(remove_space):
        _manga_value_.remove('')
    return _manga_value_

def verify_support_state(_support_):
    if requests.get(_support_).ok:
        cprint(f"Etat du support {_support_}: ", 'red', end='')
        cprint(f"Online", 'green')
    else:
        cprint(f"Etat du support {_support_}: ", 'red', end='')
        cprint(f"Offline", 'magenta')

def get_user_connection_state(support_tester, k):
    no_internet_message=f"!!Attention!!, vous n'êtes pas connecté a internet! {k} de l'application ne fonctionnerons pas."
    try:
        r=requests.get(support_tester)
        return True
    except BaseException:
        cprint(no_internet_message, 'magenta')
        return False
    
def download1(_manga, _chapter):
    url=f'https://manga-fr.me/lecture-en-ligne/scan-{_manga}/{_chapter}'
    n=0
    print(f"downloading chapter {_chapter}...")
    for i in range(get_pages(url)-1):
        n+=1
        r = requests.get(url+f'/{n}').text
        soup = BeautifulSoup(r, 'lxml')

        img_src=soup.find('img', class_="img-responsive scan-page")

        image=find_image_link(img_src, _manga)
        #print(f"Downloading page{n}...")
        os.system(f"curl -s {image} --output C:\ScansManga\{_manga}\chapitre{_chapter}\page{n}.jpg")
    if (os.listdir(f"C:\ScansManga\{_manga}\chapitre{_chapter}"))==[]:
                os.system("cd C:\ ")
                os.system(f"rmdir C:\ScansManga\{_manga}\chapitre{_chapter}")
                cprint("Le chapitre sélectionné ou le manga est inexistant.", 'magenta')
    else:
        cprint(f"Chapitre {_chapter} de {_manga}: ", 'cyan', end='')
        cprint(f"Installed(C:\ScansManga\{_manga}\chapitre{_chapter})", 'green')

def process_several_chapter(input):
    chapters=[]
    input=str(input)
    input = re.split("-", input)
    if int(input[0])+1==int(input[1]):
        return [int(input[0]),int(input[1])]
    else:
        for e in range(int(input[0]), int(input[1])+1):
            chapters.append(e)
        return chapters
def download_several(manga_, chapters_):
    chapters_available=[]
    for k in chapters_:
        if get_is_available(f"https://manga-fr.me/lecture-en-ligne/scan-{manga_}",k, manga_):
            chapters_available.append(k)
            print(f"Chapter {k} of {manga_}: ", end='')
            cprint("Available", 'green')
        else:
            print(f"Chapter {k} of {manga_}: ", end='')
            cprint("Not-Available", 'red')
    if len(chapters_available)==0:
        cprint("Aucun des chapitres séléctionnés n'est disponibles au telechargement.", 'magenta')
    else:
        for i in chapters_available:
            try:
                    os.mkdir(f"C:\ScansManga\{manga_}")
            except FileExistsError:
                pass

            try:
                    os.mkdir(f"C:\ScansManga\{manga_}\chapitre{i}")
            except FileExistsError:
                pass
            download1(manga_, i)

        
"""link=f"https://manga-fr.me/lecture-en-ligne/scan-{manga}/{chapter}"
    if link in r:
        print("trouvé")
        dictionnary[manga]=link
        print(dictionnary)
    else:
        print("Ce chapitre n'existe pas.")"""
os.system("cls")
dictionnary = {'one-piece':''}
cprint(text2art("MS-Installer"), 'cyan')
cprint('by Nono.\n\n'.center(130), 'red')
cprint("Enter 'help'", 'red')
support = "https://manga-fr.me"
listofcommandmessage="help: cette commande affiche le message de base du logiciel\nis_available --[manga name][chapters]: détermine si un chapitre est disponible au telechargement\nstt: renvoie l'etat du support de téléchargement des scans\nget_version: renvoie la version de l'outil\nread --[manga name][chapter]: lis le chapitre du manga sélectionnés avec le Manga_Scan -Reader\n[manga name]: en entrant le nom d'un manga, vous pourrez télécharger un ou plusieurs chapitre(s) au choix"
helpmessage=f"Bienvenue sur la console du Manga_Scan -Installer\n\nEntrez le nom d'un manga dont vous voulez lire les scans\n\nVous pourrez lire les chapitres téléchargés grace au Manga_Scan -Reader, ou dans le fichier local 'C:\ScansManga'\nEnter 'get_command'"
get_user_connection_state(support, "La majorité des fonctionnalités")
while True:
    manga=input(">>>")
    if manga=='':
        print("veuillez entrer une commande, entrez 'get_command' pour voir la liste des commandes")  
    elif manga=="help":
        cprint(helpmessage.center(150), 'red')
    elif "is_available" in manga.lower():
        if not get_user_connection_state(support, "Cette fonctionnalité"):
            pass
        else:
            if "--" in manga:
                manga_value=re.split("is_available|--|:| ", manga)
                manga_value=remove_space_from_list(manga_value)
                manga_name_value=[]
                manga_chapter_value=0
                for e in manga_value:
                    try:
                        k=int(e)
                        manga_chapter_value=k
                    except ValueError:
                        manga_name_value.append(e)
                manga=get_name_fillable(manga_name_value)
                print(f"Searching for : {manga}-{manga_chapter_value}")
                if get_is_available(f"https://manga-fr.me/lecture-en-ligne/scan-{manga}",manga_chapter_value, manga):
                    print(f"Chapter {manga_chapter_value} of {manga}: ", end='')
                    cprint("Available", 'green')
                else:
                    print(f"Chapter {manga_chapter_value} of {manga}: ", end='')
                    cprint("Not-Available", 'red')
            else:
                cprint("Veuillez respecter la syntaxe de la commande.", 'red')
    elif manga.lower()=="get_command":
        cprint(f"Les commande disponible sur la version {version} sont:", 'red')
        cprint(listofcommandmessage.center(100), 'red')
    elif manga.lower()=="stt":
        if not get_user_connection_state(support, "Cette fonctionnalité"):
            pass
        else:
            verify_support_state(support)
    elif manga.lower()=="get_version":
        cprint(f"v{version}")
    elif "read" in manga.lower():
        if "--" in manga:
            manga=re.split("read|--| ", manga)
            manga=remove_space_from_list(manga)
            print(manga)
            manga_nametofill=[]
            chapterFinal=0
            for e in manga:
                try:
                    chapterFinal=int(e)
                except:
                    manga_nametofill.append(e)
            mangaFinal=get_name_fillable(manga_nametofill)
            print(mangaFinal)
            try:
                reader.read(mangaFinal, chapterFinal)
            except FileNotFoundError:
                print("Le chapitre sélectionné n'existe pas ou n'est pas téléchargé.")
                pass
        else:
            cprint("Veuillez respecter la syntaxe de la commande.", 'red')
    else:
        if not get_user_connection_state(support, "cette fonctionnalité"):
            pass
        else:
            manga=get_name_fillable(manga)
            chapter=input("Quel(s) chapitres(s) voulez-vous télécharger?(min-max):")
            if "-" in chapter:
                chs=process_several_chapter(chapter)
                download_several(manga, chs)
            else:
                try:
                    os.mkdir(f"C:\ScansManga\{manga}")
                except FileExistsError:
                    pass

                try:
                    os.mkdir(f"C:\ScansManga\{manga}\chapitre{chapter}")
                except FileExistsError:
                    pass
                download1(manga, chapter)
            

