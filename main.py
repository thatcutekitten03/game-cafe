import pygame
from pygame.locals import *

try:
    import data.stage.KinopoEntrance as STG_KinopoEntrance
except ImportError:
    print("Could not load a stage!")


pygame.init()

class Cafe():
    RequestedStartup = False
    Editor = False
    GameTitle = "<uncofingured game>"
    GameVersion = "Hidden"
    GameLanguage = "Hidden"
    def GetConfig(self):
        print("Initialising Cafe...")
        Cafe_Editor = open('data/cafe/editor.xc','r')
        self.Editor = Cafe_Editor.read()
        Cafe_Editor.close()
        Cafe_Game = open('data/cafe/game.xc','r')
        Game = Cafe_Game.read()
        Game = Game.split(",")
        self.GameTile = Game[0]
        self.GameVersion = Game[1]
        self.GameLanguage = Game[2]
        Cafe_Game.close()
    def RequestStartup(self):
        self.RequestedStartup = True
    screen_width = 800
    screen_height = 800
    tile_size = 64  
Cafe.GetConfig(Cafe)
screen = pygame.display.set_mode((Cafe.screen_width, Cafe.screen_height))

class Load():
    pass

class GameState():
    Game_IsRunning = True
    pygame.display.set_caption(Cafe.GameTitle)

class Editor():
    def DisplayGrid():
        for line in range(0,6):
            pygame.draw.line(screen, (255,255,255), (0, line*Cafe.tile_size), (Cafe.screen_width, line*Cafe.tile_size))
            pygame.draw.line(screen, (255,255,255), (line*Cafe.tile_size, 0), (line*Cafe.tile_size, Cafe.screen_height*3))
    def DisplayStartup(Cafe):
        if not Cafe.RequestedStartup:
            print(f"Game   {Cafe.GameTitle}\nVers   {Cafe.GameVersion}\nLang   {Cafe.GameLanguage}")

class Stage():
    def __init__(self,data,Cafe=Cafe):
        self.tile_list = []
        #load images
        OBJ_Dirt_Top = pygame.image.load("data/objects/TileDirt/0.png")
        OBJ_Dirt = pygame.image.load("data/objects/TileDirt/0.png")
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(OBJ_Dirt, (Cafe.tile_size, Cafe.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * Cafe.tile_size
                    img_rect.y = row_count * Cafe.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def drawStage(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])

Game_Stage = Stage(STG_KinopoEntrance.world_data)

while GameState.Game_IsRunning:
    
    Game_Stage.drawStage()
    if Cafe.Editor:
        if not Cafe.RequestedStartup:
            Editor.DisplayStartup(Cafe)
            Cafe.RequestStartup(Cafe)
        Editor.DisplayGrid()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            GameState.Game_IsRunning = False
    pygame.display.update()
pygame.quit()
