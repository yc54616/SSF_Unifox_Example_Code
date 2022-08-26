"" # <= pygame 라이브러리 불러오기

"" # 파이게임 초기화
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BACKGROUND_LOCATION = (0, 0)
"" # <= 화면 창 설정

pygame.display.set_caption("UNIFOX OX퀴즈 게임")

"" # <= 여우 이미지 로드
pos_x = 500
pos_y = 300

clock = pygame.time.Clock()

while True:
    fps = clock.tick(30)
    event = pygame.event.poll() 
    if event.type == pygame.QUIT:
        break

    ############# 캐릭터 조작하기 #############
    
    ""

    screen.fill(WHITE)
    "" #<= 여우 이미지 그리기
    pygame.display.update()
pygame.quit()