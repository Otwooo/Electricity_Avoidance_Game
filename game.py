import random
import pygame
##################################################################
#기본 초기화 (반드시 해야하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀(제목) 설정
pygame.display.set_caption("떨어지는 거 조심~!")

# FPS 초당 프레임 변수 설정
clock = pygame.time.Clock()
##################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
#배경 만들기
background = pygame.image.load("C:\\Users\\ADMIN\\OneDrive - 대전대신고등학교 (1)\\문서\\카카오톡 받은 파일\\전력 수송게임\\전력 수송게임\\배경.png")

#캐릭터 만들기
character = pygame.image.load("C:\\Users\\ADMIN\\OneDrive - 대전대신고등학교 (1)\\문서\\카카오톡 받은 파일\\전력 수송게임\\전력 수송게임\\사람.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

#이동 위치
to_x = 0
character_speed = 0.8

#적 만들기
enemy = pygame.image.load("C:\\Users\\ADMIN\\OneDrive - 대전대신고등학교 (1)\\문서\\카카오톡 받은 파일\\전력 수송게임\\전력 수송게임\\전기.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)  
enemy_y_pos = 0
enemy_speed = 10

enemy1 = pygame.image.load("C:\\Users\\ADMIN\\OneDrive - 대전대신고등학교 (1)\\문서\\카카오톡 받은 파일\\전력 수송게임\\전력 수송게임\\전기.png")
enemy1_size = enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]
enemy1_x_pos = random.randint(0, screen_width - enemy1_width)  
enemy1_y_pos = 0
enemy1_speed = 8

enemy2 = pygame.image.load("C:\\Users\\ADMIN\\OneDrive - 대전대신고등학교 (1)\\문서\\카카오톡 받은 파일\\전력 수송게임\\전력 수송게임\\전기.png")
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_x_pos = random.randint(0, screen_width - enemy2_width)  
enemy2_y_pos = 0
enemy2_speed = 6

# 폰트 정의
game_font = pygame.font.Font(None, 40)

#총 시간

#시작 
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴

running = True 
while running:
    dt = clock.tick(60) 

    # 2. 이벤트 처리 (키보드, 마우스 등) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            to_x -= character_speed
        elif event.key == pygame.K_RIGHT    :
            to_x += character_speed

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x 

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed
    enemy1_y_pos += enemy1_speed
    enemy2_y_pos += enemy2_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
    if enemy1_y_pos > screen_height:
        enemy1_y_pos = -100
        enemy1_x_pos = random.randint(0, screen_width - enemy1_width)
    if enemy2_y_pos > screen_height:
        enemy2_y_pos = -100
        enemy2_x_pos = random.randint(0, screen_width - enemy2_width)


    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    enemy1_rect = enemy.get_rect()
    enemy1_rect.left = enemy1_x_pos
    enemy1_rect.top = enemy1_y_pos
    enemy2_rect = enemy.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌!")
        running = False
    if character_rect.colliderect(enemy1_rect):
        print("충돌!")
        running = False
    if character_rect.colliderect(enemy2_rect):
        print("충돌!")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(enemy, (enemy1_x_pos, enemy1_y_pos))
    screen.blit(enemy, (enemy2_x_pos, enemy2_y_pos))

    #타이머 집어넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(elapsed_time)), True, (255, 255, 255))

    screen.blit(timer, (10, 10))

    pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) #2초 정도 대기 (ms)

pygame.quit()