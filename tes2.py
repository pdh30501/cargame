import pygame
import sys
from pygame.locals import *
import random
# Khởi tạo Pygame
pygame.init()
#Mau nen
red=(200,0,0)
white=(255,255,255)
width=816
height=612
screen=pygame.display.set_mode((width,height))
###########
clock=pygame.time.Clock()

bg=pygame.image.load('./images/race1.png')
btn_play=pygame.image.load('./images/Playbtn1.jpg')
btn_exit=pygame.image.load('./images/exitbtn1.jpg')
bb1=pygame.image.load('./images/bienbao1.png').convert_alpha()
bb2=pygame.image.load('./images/bienbao2.png').convert_alpha()
bb3=pygame.image.load('./images/bienbao3.png').convert_alpha()
bb4=pygame.image.load('./images/bienbao4.png').convert_alpha()
bb_pos= (300, 0)
btn_play_pos = (150, 100)
btn_exit_pos = (150, 300)
pygame.display.set_caption('Car game')
#Khoi tao bien
font = pygame.font.Font(pygame.font.get_default_font(), 16)
gameover=False
win=False
speed=2
score=0
lives=3
high_score=0
# road_width=500
street_width=10
street_height=50
#Lan duong
lane_1=170
lane_2=325
lane_3=480
lane_4=640
lanes=[lane_1, lane_2, lane_3, lane_4]
lane_move_y=0
#Vi tri ban dau xe nguoi choi
player_x=330
player_y=550
#Doi tuong xe luu thong - vehicle
class Vehicle(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        #Scale images
        image_scale=50/image.get_rect().width
        new_width = image.get_rect().width *image_scale
        new_height = image.get_rect().height *image_scale
        self.image=pygame.transform.scale(image,(new_width,new_height))
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
#Doi tuong xe player
class PlayerVehicle(Vehicle):
    def __init__(self,x,y):
        image=pygame.image.load('./images/car.png')
        super().__init__(image,x,y)
#Doi tuong dong xu
class Coin(Vehicle):
    def __init__(self,x,y):
        image=pygame.image.load('./images/coin.png')
        super().__init__(image,x,y)
#Sprite groups
player_group=pygame.sprite.Group()
Vehicle_group=pygame.sprite.Group()
Coin_group=pygame.sprite.Group()
#Tao xe player
player = PlayerVehicle(player_x,player_y)
player_group.add(player)
#Load xe lưu thông
image_name=['car1.png','car2.png','car3.png','car4.png','car5.png']
Vehicle_images=[]
for name in image_name:
    image=pygame.image.load('./images/'+name)
    Vehicle_images.append(image)
#Load hinh va cham - end game
crash=pygame.image.load('./images/crash.png')
crash_rect=crash.get_rect()
#Cai dat fps
clock=pygame.time.Clock()
fps=120
#Chen am thanh
skid_sound=pygame.mixer.Sound('./sound/skid.wav')
lose_sound=pygame.mixer.Sound('./sound/Lose.wav')
win_sound=pygame.mixer.Sound('./sound/win.wav')
coin_sound=pygame.mixer.Sound('./sound/Coin.wav')
s1=pygame.mixer.Sound('./sound/1.wav')
s2=pygame.mixer.Sound('./sound/2.wav')
s3=pygame.mixer.Sound('./sound/3.wav')
########
running=False
bienbao=False
btn=True
# Vòng lặp game
while btn:
    #Tieu de game
    title= pygame.image.load("./images/title123.jpg")
    title_pos = (-100,-100)
    screen.blit(title, title_pos)
    # Tải,xac dinh vi tri, ve  nút play
    play_button = pygame.image.load("./images/Playbtn1.jpg")
    play_button_pos = (50, 450)
    screen.blit(play_button, play_button_pos)
    # Tải,xac dinh vi tri, ve  nút exit
    exit_button = pygame.image.load("./images/exitbtn1.jpg")
    exit_button_pos = (430, 450)
    screen.blit(exit_button, exit_button_pos)
    # Cập nhật màn hình
    pygame.display.update()
    # Xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Xác định vị trí chuột
            mouse_pos = pygame.mouse.get_pos()
            # Kiểm tra xem chuột có được nhấn vào nút play hay không
            if mouse_pos[0] >= play_button_pos[0] and mouse_pos[0] <= play_button_pos[0] + play_button.get_width() \
            and mouse_pos[1] >= play_button_pos[1] and mouse_pos[1] <= play_button_pos[1] + play_button.get_height():
                # Khởi động trò chơi tại đây
                print("Chơi game!")
                running=True
                btn=False
            if mouse_pos[0] >= exit_button_pos[0] and mouse_pos[0] <= exit_button_pos[0] + exit_button.get_width() \
            and mouse_pos[1] >= exit_button_pos[1] and mouse_pos[1] <= exit_button_pos[1] + exit_button.get_height():
                pygame.quit()
                sys.exit()
if running:
    # Hiển thị biển báo ban đầu
    screen.blit(bg, (0, 0))
    screen.blit(bb1, bb_pos)
    pygame.display.update()

    # Sau khi hiển thị biển báo, tạm dừng 1 giây trước khi hiển thị hình tiếp theo
    pygame.time.delay(1000)

    # Hiển thị hình tiếp theo
    s1.play()
    screen.blit(bb2, bb_pos)
    pygame.display.update()

    # Tiếp tục tạm dừng và hiển thị các hình tiếp theo tương tự
    pygame.time.delay(1000)
    s2.play()
    screen.blit(bb3, bb_pos)
    pygame.display.update()

    pygame.time.delay(1000)
    s3.play()
    screen.blit(bb4, bb_pos)
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.mixer.music.load("./sound/bg.wav")
    pygame.mixer.music.play(-1)  # -1 để lặp lại âm thanh nền liên tục
while running:
    #Chinh frame hinh tren giay
    clock.tick(fps)
    for event in pygame.event.get():
        #Dieu khien xe:
        if event.type==KEYDOWN:
            if (event.key==K_LEFT or event.key==K_a) and player.rect.center[0]>300:
                player.rect.x-=145
            if (event.key==K_RIGHT or event.key==K_d) and player.rect.center[0]<500:
                player.rect.x+=145
            # Kiem tra va cham KHI DIEU KHIEN
            for vehicle in Vehicle_group:
                if pygame.sprite.collide_rect(player,vehicle):
                    lives -= 1
                    skid_sound.play()
                    crash_rect.center = [player.rect.center[0], player.rect.top]
                    if lives == 0:
                        skid_sound.play()
                        gameover = True
                        break

    #Kiem tra va cham khi xe dung yen
    if pygame.sprite.spritecollide(player,Vehicle_group,True):
        lives-=1
        skid_sound.play()
        crash_rect.center=[player.rect.center[0],player.rect.top]
        if lives==0:
            skid_sound.play()
            gameover=True
            running=False
    # Kiem tra cham voi coin thi tang diem
    if pygame.sprite.spritecollide(player, Coin_group, True):
        score+=1
        coin_sound.play()
    # Xet Diem cao
    if gameover:
        if score > high_score:
            high_score = score
    #
    screen.blit(bg, (0, 0))
    #Ve lane duong
    lane_move_y+=speed * 2
    if lane_move_y >=street_height*2:
        lane_move_y=0
    for y in range(street_height*-2,height,street_height*2):
        pygame.draw.rect(screen,white,(250,y+lane_move_y,street_width,street_height))
        pygame.draw.rect(screen,white,(400,y+lane_move_y,street_width,street_height))
        pygame.draw.rect(screen,white,(550,y+lane_move_y,street_width,street_height))
    #Ve xe player
    player_group.draw(screen)
    #Ve phuong tien giao thong
    if running:
        add_vehicle=True
        for vehicle in Vehicle_group:
            if vehicle.rect.top<vehicle.rect.height * 1.5:
                add_vehicle=False
        if add_vehicle:
            lane=random.choice(lanes) #Chon ngau nhien lane
            image=random.choice(Vehicle_images)   #Chon ngau nhien xe
            vehicle=Vehicle(image,lane,height/-2)
            Vehicle_group.add(vehicle)
    #Ve dong xu
    if running:
        add_coin=True
        for coin in Coin_group:
            if coin.rect.top<coin.rect.height*2:
                add_coin=False
        if add_coin:
            lane=random.choice(lanes) #Chon ngau nhien lane
            coin=Coin(lane,height/-2)
            Coin_group.add(coin)
            # # Kiem tra xe lưu thong có va chạm với coin không, nếu có thì
            # pygame.sprite.spritecollide(coin, Vehicle_group, Fla)

    #Cho xe va coin luu thong chay
    counter=0
    for vehicle in Vehicle_group:
        vehicle.rect.y+=speed
        #Remove vehicle
        if vehicle.rect.top>=height:
            vehicle.kill()
            counter+=1
            #Tang toc do kho - chay moi khi chay qua 5 chiec xe
            if counter>0 and counter%4==0:
                speed+=3
    for coin in Coin_group:
        coin.rect.y+=speed
            # Remove coin
        # if coin.rect.top <= height:
        #     coin.kill()
        #     score -= 1
    #Ve nhom xe luu thong
    Vehicle_group.draw(screen)
    # Ve dong xu
    Coin_group.draw(screen)
    #Hien thi diem
    text_score=font.render('Score: '+str(score),True,white)
    text_score_rect=text_score.get_rect()
    text_score_rect.center=(50,40)
    screen.blit(text_score,text_score_rect)
    #Hien thi mang song
    text_lives=font.render('Lives: '+str(lives),True,white)
    text_lives_rect=text_lives.get_rect()
    text_lives_rect.center=(50,70)
    screen.blit(text_lives,text_lives_rect)

    # Hien thi diem cao nhat
    text_highscore=font.render('HighScore: '+str(high_score),True,white)
    text_highscore=font.render('HighScore: '+str(high_score),True,white)
    text_highscore_rect=text_highscore.get_rect()
    text_highscore_rect.center=(52,100)
    screen.blit(text_highscore,text_highscore_rect)

    # Sau khi hiển thị xong các hình, bạn có thể chạy trò chơi tiếp tục
    if gameover:
        pygame.mixer.music.stop()
        lose_sound.play()
        # Xet Diem cao
        if score > high_score:
            high_score = score
        # Hiển thị ảnh gameover
        text_gameover = pygame.image.load("./images/GameOver.png")
        text_gameover_pos = (105, 290)
        screen.blit(text_gameover, text_gameover_pos)
        #Hien thi crash
        screen.blit(crash,crash_rect)
        #Ve hop thoai
        pygame.draw.rect(screen,red,(0,50,width,100))
        #hien thi dong chu
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Your high score is: '+str(high_score), True, white)
        text_rect = text.get_rect()
        text_rect.center = (390, 90)
        screen.blit(text, text_rect)
        text = font.render('Press Y to play again or Prees N to stop', True, white)
        screen.blit(text,(250, 110) )
    pygame.display.update()
    #################################################
    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                gameover=False
            if event.type == KEYDOWN:
                if event.key == K_y:
                    #reset game
                    gameover=False
                    score=0
                    lives=3
                    speed=2
                    Vehicle_group.empty()
                    player.rect.center=[player_x,player_y]
                    running=True
                    pygame.mixer.music.play(-1)
                elif event.key == K_n:
                    gameover = False
                    running = False