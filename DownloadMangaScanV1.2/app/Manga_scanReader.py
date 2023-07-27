import pygame
from PIL import Image
import os
class reader:
        

    def resize(image_from_local_disk, maxx, maxy):
        im=Image.open(image_from_local_disk)
        x, y=im.size
        if x> maxx:
            x_resize=x-(x-maxx)
        else:
            x_resize=x
        if y>maxy:
            y_resize=y-(y-maxy)
        else:
            y_resize=y
        imresized=im.resize((x_resize, y_resize))
        imresized.save(image_from_local_disk)
        return image_from_local_disk
    
    def get_num_ofpages(_manga_, _chapter_):
        path = f"C:\ScansManga\{_manga_}\chapitre{_chapter_}"
        p=len(os.listdir(path))
        return p
    
    def get_centered_topleft(imx_, surface_x):
        centered_x=round((surface_x-imx_)/2)
        return centered_x



    def read(_manga_, _chapter_):
        from Manga_scanReader import reader
        path = "C:\ScansManga"
        path_to_icon="C:\ScansMangaExecutable\img\msicon.ico"
        path_to_button="C:\ScansMangaExecutable\img\Button.png"
        p=reader.get_num_ofpages(_manga_, _chapter_)
        #INIT WINDOW
        pygame.init()
        fullscreen=False
        window_resolution=(1600, 1000)
        chapter_surface=[1400, 1000]
        button_surface=[100, 100]
        pygame.display.set_caption("Manga_Scan -Reader")
        #pygame.display.set_icon(path_to_icon)
        main_surface=pygame.display.set_mode(window_resolution)
        button=pygame.image.load(path_to_button)
        button=pygame.transform.scale(button, button_surface)
        button2=pygame.transform.rotate(button, -180)
        button_rect= button.get_rect()
        button_rect2= button2.get_rect()
        topleft_button=[main_surface.get_width()-100, (main_surface.get_height()/2)-(button_surface[1]/2)]
        topleft_button2=[0, (main_surface.get_height()/2)-(button_surface[1]/2)]
        running = True
        n=1
        while running:
            #update chapter
            imageLue = (f'{path}\{_manga_}\chapitre{_chapter_}\page{n}.jpg')
            chapitre=pygame.image.load(reader.resize(imageLue, chapter_surface[0],chapter_surface[1] ))
            topleft_chapter=[reader.get_centered_topleft(chapitre.get_width(), chapter_surface[0])+100, 0]
            #Init all images
            main_surface.blit(chapitre, topleft_chapter)
            if n<p:
                main_surface.blit(button, topleft_button)
            else:
                button_rect.topleft=topleft_button
                pygame.Surface.fill(main_surface, color="black", rect=button_rect)
            if n>1:
                main_surface.blit(button2, topleft_button2)
            else:
                button_rect2.topleft=topleft_button2
                pygame.Surface.fill(main_surface, color="black", rect=button_rect2)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                elif event.type==pygame.MOUSEBUTTONUP:
                    button_rect.topleft=topleft_button
                    button_rect2.topleft=topleft_button2
                    if n<p:
                        if button_rect.collidepoint(event.pos):
                            n+=1
                            chapitre_rect=chapitre.get_rect()
                            chapitre_rect.topleft=topleft_chapter
                            pygame.Surface.fill(main_surface, color="black", rect=chapitre_rect)
                        else:
                            pass
                    if n>1:
                        if button_rect2.collidepoint(event.pos):
                            n-=1
                            chapitre_rect=chapitre.get_rect()
                            chapitre_rect.topleft=topleft_chapter
                            pygame.Surface.fill(main_surface, color="black", rect=chapitre_rect)
                    else:
                        pass
                    
            
            pygame.display.flip()
        pygame.display.quit()