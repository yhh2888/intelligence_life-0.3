import pygame, random

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 720 # 가로 크기
screen_height = 720 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\KDCA\\Desktop\\1231231.png")

character = pygame.transform.scale(character, (240, 160))
character_size = character.get_rect().size
character_width = int(character_size[0] / 12)
character_height = int(character_size[1] / 8)
character_x_pos = screen_width / 2 - character_size[0] / 2
character_y_pos = screen_height / 2 - character_size[1] / 2

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\KDCA\\Desktop\\grass.png")
background = pygame.transform.scale(background, (character_width*4, character_height*4))

tile_loc = [(i*20, j*20) for j in range(4) for i in range(4)]

pose = (character_width*3, character_height*0)
pre_loc = (character_x_pos, character_y_pos)

maptile = [([3, 5, 10, 11, 15]*2+[random.randint(0, 15)]*16)[random.randint(0, 24)] for i in range(36*36)]
    

# 이벤트 루프
running = True
turnpoint = 0
to_x = 0
to_y = 0
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pre_loc = (character_x_pos, character_y_pos)
                to_x = -character_width
                character_x_pos += to_x
                maptile[int(pre_loc[0]//character_width+pre_loc[1]//character_height*36)] = [3, 5, 10, 11, 15][random.randint(0, 4)]
                screen.blit(background, (list(pre_loc)),
                    pygame.Rect(*tile_loc[maptile[int(pre_loc[0]//character_width+pre_loc[1]//character_height*36)]], character_width, character_height))
                
            if event.key==pygame.K_RIGHT:
                pre_loc = (character_x_pos, character_y_pos)
                to_x = character_width
                character_x_pos += to_x
                maptile[int(pre_loc[0]//character_width+pre_loc[1]//character_height*36)] = [3, 5, 10, 11, 15][random.randint(0, 4)]
                screen.blit(background, (list(pre_loc)),
                    pygame.Rect(*tile_loc[maptile[int(pre_loc[0]//character_width+pre_loc[1]//character_height*36)]], character_width, character_height))
                
            if event.key==pygame.K_UP:
                pre_loc = (character_x_pos, character_y_pos)
                to_y = -character_height
                character_y_pos += to_y
                maptile[int(pre_loc[0]//character_width+pre_loc[1]//character_height*36)] = [3, 5, 10, 11, 15][random.randint(0, 4)]
                screen.blit(background, (list(pre_loc)),
                    pygame.Rect(*tile_loc[maptile[int(pre_loc[0]//character_width+pre_loc[1]//character_height*36)]], character_width, character_height))
                
            if event.key==pygame.K_DOWN:
                pre_loc = (character_x_pos, character_y_pos)
                to_y = character_height
                character_y_pos += to_y
                maptile[int(pre_loc[0]//character_width+pre_loc[1]//character_height*36)] = [3, 5, 10, 11, 15][random.randint(0, 4)]
                screen.blit(background, (list(pre_loc)),
                    pygame.Rect(*tile_loc[maptile[int(pre_loc[0]//character_width+pre_loc[1]//character_height*36)]], character_width, character_height))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    turnpoint += 1
    if turnpoint > 40:
        character_x_pos += to_x
        character_y_pos += to_y
        turnpoint = 0

    if to_y > 0:
        pose = (character_width*3, character_height*0)
    elif to_y < 0:
        pose = (character_width*3, character_height*3)
    elif to_x > 0:
        pose = (character_width*3, character_height*2)
    elif to_x < 0:
        pose = (character_width*3, character_height*1)
    
    for i in range(len(maptile)):    
        screen.blit(background, ((i%36)*character_width, (i//36)*character_height),
                    pygame.Rect(*tile_loc[maptile[i]], character_width, character_height))
        
    screen.blit(character, (character_x_pos, character_y_pos), pygame.Rect(*pose, character_width, character_height)) # 캐릭터 그리기

    pygame.display.update()

# pygame 종료
pygame.quit()
