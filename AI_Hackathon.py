import pygame
import sys
import math
import time
import random
import json
from huskylib import HuskyLensLibrary

pygame.init()
pygame.display.set_caption('kiosk')

def main():
         #hl = HuskyLensLibrary("SERIAL", "/dev/ttyUSB1", 3000000)
         hl = HuskyLensLibrary("I2C","", address=0x32)

         algorthimsByteID = {
             "ALGORITHM_OBJECT_TRACKING": "0100",
             "ALGORITHM_FACE_RECOGNITION": "0000",
             "ALGORITHM_OBJECT_RECOGNITION": "0200",
             "ALGORITHM_LINE_TRACKING": "0300",
             "ALGORITHM_COLOR_RECOGNITION": "0400",
             "ALGORITHM_TAG_RECOGNITION": "0500",
             "ALGORITHM_OBJECT_CLASSIFICATION": "0600",
             "ALGORITHM_QR_CODE_RECOGNTITION": "0700",
             "ALGORITHM_BARCODE_RECOGNTITION": "0800",
         }
         commandList = ['knock()', 
             'setCustomName() #Random String & Cords', 
             'customText() #Random String & Cords', 
             'clearText()', 
             'requestAll()', 
             'saveModelToSDCard(1)', 
             'loadModelFromSDCard(1)', 
             'savePictureToSDCard()', 
             'count()',
             'learnedObjCount()',
             'saveScreenshotToSDCard()', 
             'blocks()', 
             'arrows()', 
             'learned()', 
             'learnedBlocks()', 
             'learnedArrows()', 
             'getObjectByID(1)', 
             'getBlocksByID(1)', 
             'getArrowsByID(1)', 
             'algorthim() #Random Choice', 
             'learn(1)', 
             'forget()', 
             'frameNumber()',
             ""
         ]
         real_num = 1 
         screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
         fps = pygame.time.Clock()

         # 매장 포장 이미지
         img_mj1 = pygame.image.load('매장1.png')
         img_mj1 = pygame.transform.scale(img_mj1, (450, 450))
         img_pj1 = pygame.image.load('포장1.png')
         img_pj1 = pygame.transform.scale(img_pj1, (450, 450))
         img_mj2 = pygame.image.load('매장2.png')
         img_mj2 = pygame.transform.scale(img_mj2, (450, 450))
         img_pj2 = pygame.image.load('포장2.png')
         img_pj2 = pygame.transform.scale(img_pj2, (450, 450))

         # 시계 이미지
         img_time = []
         img_time.append(pygame.image.load('time0.png'))
         img_time[0] = pygame.transform.scale(img_time[0], (100, 100))
         img_time.append(pygame.image.load('time1.png'))
         img_time[1] = pygame.transform.scale(img_time[1], (100, 100))
         img_time.append(pygame.image.load('time2.png'))
         img_time[2] = pygame.transform.scale(img_time[2], (100, 100))
         img_time.append(pygame.image.load('time3.png'))
         img_time[3] = pygame.transform.scale(img_time[3], (100, 100))
         img_time.append(pygame.image.load('time4.png'))
         img_time[4] = pygame.transform.scale(img_time[4], (100, 100))
         img_time.append(pygame.image.load('time5.png'))
         img_time[5] = pygame.transform.scale(img_time[5], (100, 100))
         img_time.append(pygame.image.load('time6.png'))
         img_time[6] = pygame.transform.scale(img_time[6], (100, 100))
         img_time.append(pygame.image.load('time7.png'))
         img_time[7] = pygame.transform.scale(img_time[7], (100, 100))
         img_time.append(pygame.image.load('time8.png'))
         img_time[8] = pygame.transform.scale(img_time[8], (100, 100))


         # 카테고리 이미지
         img_tbk = pygame.image.load('떡볶이.png')
         img_tbk = pygame.transform.scale(img_tbk, (400, 400))
         img_mr = pygame.image.load('면류.png')
         img_mr = pygame.transform.scale(img_mr, (400, 400))
         img_br = pygame.image.load('밥류.png')
         img_br = pygame.transform.scale(img_br, (400, 400))
         img_tgr = pygame.image.load('튀김류.png')
         img_tgr = pygame.transform.scale(img_tgr, (400, 400))
         img_tbk_dark = pygame.image.load('어두운떡볶이.png')
         img_tbk_dark = pygame.transform.scale(img_tbk_dark, (400, 400))
         img_mr_dark = pygame.image.load('어두운면류.png')
         img_mr_dark = pygame.transform.scale(img_mr_dark, (400, 400))
         img_br_dark = pygame.image.load('어두운밥류.png')
         img_br_dark = pygame.transform.scale(img_br_dark, (400, 400))
         img_tgr_dark = pygame.image.load('어두운튀김류.png')
         img_tgr_dark = pygame.transform.scale(img_tgr_dark, (400, 400))

         # 떡볶이 이미지
         img_tbk_1 = pygame.image.load('떡볶이_1.png')
         img_tbk_1 = pygame.transform.scale(img_tbk_1, (800, 260))
         img_tbk_2 = pygame.image.load('떡볶이_2.png')
         img_tbk_2 = pygame.transform.scale(img_tbk_2, (790, 260))
         img_tbk_3 = pygame.image.load('떡볶이_3.png')
         img_tbk_3 = pygame.transform.scale(img_tbk_3, (800, 260))
         img_tbk_dark_1 = pygame.image.load('어두운떡볶이_1.png')
         img_tbk_dark_1 = pygame.transform.scale(img_tbk_dark_1, (800,260))
         img_tbk_dark_2 = pygame.image.load('어두운떡볶이_2.png')
         img_tbk_dark_2 = pygame.transform.scale(img_tbk_dark_2, (790, 260))
         img_tbk_dark_3 = pygame.image.load('어두운떡볶이_3.png')
         img_tbk_dark_3 = pygame.transform.scale(img_tbk_dark_3, (800, 260))

         # 면 이미지
         img_mr_1 = pygame.image.load('면_1.png')
         img_mr_1 = pygame.transform.scale(img_mr_1, (800, 260))
         img_mr_2 = pygame.image.load('면_2.png')
         img_mr_2 = pygame.transform.scale(img_mr_2, (800, 260))
         img_mr_3 = pygame.image.load('면_3.png')
         img_mr_3 = pygame.transform.scale(img_mr_3, (800, 260))
         img_mr_dark_1 = pygame.image.load('어두운면_1.png')
         img_mr_dark_1 = pygame.transform.scale(img_mr_dark_1, (800, 260))
         img_mr_dark_2 = pygame.image.load('어두운면_2.png')
         img_mr_dark_2 = pygame.transform.scale(img_mr_dark_2, (800, 260))
         img_mr_dark_3 = pygame.image.load('어두운면_3.png')
         img_mr_dark_3 = pygame.transform.scale(img_mr_dark_3, (800, 260))

         # 밥 이미지
         img_br_1 = pygame.image.load('밥_1.png')
         img_br_1 = pygame.transform.scale(img_br_1, (800, 260))
         img_br_2 = pygame.image.load('밥_2.png')
         img_br_2 = pygame.transform.scale(img_br_2, (800, 260))
         img_br_3 = pygame.image.load('밥_3.png')
         img_br_3 = pygame.transform.scale(img_br_3, (800, 260))
         img_br_dark_1 = pygame.image.load('어두운밥_1.png')
         img_br_dark_1 = pygame.transform.scale(img_br_dark_1, (800, 260))
         img_br_dark_2 = pygame.image.load('어두운밥_2.png')
         img_br_dark_2 = pygame.transform.scale(img_br_dark_2, (800, 260))
         img_br_dark_3 = pygame.image.load('어두운밥_3.png')
         img_br_dark_3 = pygame.transform.scale(img_br_dark_3, (800, 260))

         # 튀김 이미지
         img_tgr_1 = pygame.image.load('튀김_1.png')
         img_tgr_1 = pygame.transform.scale(img_tgr_1, (800, 260))
         img_tgr_2 = pygame.image.load('튀김_2.png')
         img_tgr_2 = pygame.transform.scale(img_tgr_2, (800, 260))
         img_tgr_3 = pygame.image.load('튀김_3.png')
         img_tgr_3 = pygame.transform.scale(img_tgr_3, (800, 260))
         img_tgr_dark_1 = pygame.image.load('어두운튀김_1.png')
         img_tgr_dark_1 = pygame.transform.scale(img_tgr_dark_1, (800, 260))
         img_tgr_dark_2 = pygame.image.load('어두운튀김_2.png')
         img_tgr_dark_2 = pygame.transform.scale(img_tgr_dark_2, (800, 260))
         img_tgr_dark_3 = pygame.image.load('어두운튀김_3.png')
         img_tgr_dark_3 = pygame.transform.scale(img_tgr_dark_3, (800, 260))

         # 장바구니에 넣을 이미지
         img_tbk_small_1 = pygame.image.load('작은떡볶이_1.png')
         img_tbk_small_1 = pygame.transform.scale(img_tbk_small_1, (100, 100))
         img_tbk_small_2 = pygame.image.load('작은떡볶이_2.png')
         img_tbk_small_2 = pygame.transform.scale(img_tbk_small_2, (100, 100))
         img_tbk_small_3 = pygame.image.load('작은떡볶이_3.png')
         img_tbk_small_3 = pygame.transform.scale(img_tbk_small_3, (100, 100))
         img_mr_small_1 = pygame.image.load('작은면_1.png')
         img_mr_small_1 = pygame.transform.scale(img_mr_small_1, (100, 100))
         img_mr_small_2 = pygame.image.load('작은면_2.png')
         img_mr_small_2 = pygame.transform.scale(img_mr_small_2, (100, 100))
         img_mr_small_3 = pygame.image.load('작은면_3.png')
         img_mr_small_3 = pygame.transform.scale(img_mr_small_3, (100, 100))
         img_br_small_1 = pygame.image.load('작은밥_1.png')
         img_br_small_1 = pygame.transform.scale(img_br_small_1, (100, 100))
         img_br_small_2 = pygame.image.load('작은밥_2.png')
         img_br_small_2 = pygame.transform.scale(img_br_small_2, (100, 100))
         img_br_small_3 = pygame.image.load('작은밥_3.png')
         img_br_small_3 = pygame.transform.scale(img_br_small_3, (100, 100))
         img_tgr_small_1 = pygame.image.load('작은튀김_1.png')
         img_tgr_small_1 = pygame.transform.scale(img_tgr_small_1, (100, 100))
         img_tgr_small_2 = pygame.image.load('작은튀김_2.png')
         img_tgr_small_2 = pygame.transform.scale(img_tgr_small_2, (100, 100))
         img_tgr_small_3 = pygame.image.load('작은튀김_3.png')
         img_tgr_small_3 = pygame.transform.scale(img_tgr_small_3, (100, 100))

         # 카드 현금 이미지
         img_hg = pygame.image.load('hg.png')
         img_hg = pygame.transform.scale(img_hg, (350, 175))
         img_hg_dark = pygame.image.load('hg_dark.png')
         img_hg_dark = pygame.transform.scale(img_hg_dark, (350, 175))
         img_card = pygame.image.load('card.png')
         img_card = pygame.transform.scale(img_card, (350, 175))
         img_card_dark = pygame.image.load('card_dark.png')
         img_card_dark = pygame.transform.scale(img_card_dark, (350, 175))


         # no gyeongwoo
         img_name = pygame.image.load('name.png')
         img_name = pygame.transform.scale(img_name, (1100, 170))
         img_camera_mjpj = pygame.image.load('camera_mjpj.png')
         img_camera_mjpj = pygame.transform.scale(img_camera_mjpj, (1080, 170))
         img_camera_hgcard = pygame.image.load('camera_hgcard.png')
         img_camera_hgcard = pygame.transform.scale(img_camera_hgcard, (1080, 170))
         img_camera_ilban = pygame.image.load('camera_ilban.png')
         img_camera_ilban = pygame.transform.scale(img_camera_ilban, (1080, 340))
         img_ysj = pygame.image.load('ysj.png')
         img_ysj = pygame.transform.scale(img_ysj, (940, 1000))

         img_jumun_wan = pygame.image.load('jumun_wan.png')
         img_jumun_wan = pygame.transform.scale(img_jumun_wan, (1100, 170))

         
         myFont1 = pygame.font.SysFont("arial", 40, True, False)
         tp = 0

         num_mjpj = 0
         menu_golla = 0

         i = 0

         menu_damgi = []
         menu_damgi_sum = 0
         jangbaguni = [] # 메뉴 이름 담는

         price = {"tbk_1":4500, "tbk_2":5000, "tbk_3":5000, "mr_1":3000, "mr_2":4000, "mr_3":4500, "br_1":2000, "br_2":5000, "br_3":5000, "tgr_1":2000, "tgr_2":2500, "tgr_3":2500}


         firstpage = True
         nextpage1 = False
         nextpage2_1 = False
         nextpage2_2 = False
         nextpage2_3 = False
         nextpage2_4 = False
         dirogagi = False
         reset = False
         nextpage3 = False # 계산 화면
         lastpage = False
         
         num_mjpj = 0
         menu_golla = 0
         tbk_golla = 0
         mr_golla = 0
         br_golla = 0
         tgr_golla = 0

         past_number = 0
         ok = False
         reset = False         

         while True:
                  #while(True):
                           #obj = hl.blocks()
                           #number = obj.__dict__['ID']
                           #if(number!=6 and number!=0):
                                    #break
                  obj = hl.blocks()
                  number = obj.__dict__['ID']
                  #print(number,i,firstpage,nextpage1,nextpage2_1,nextpage2_2,nextpage2_3,nextpage2_4,nextpage3,lastpage,num_mjpj,menu_golla,tbk_golla, mr_golla,br_golla,tgr_golla,ok,dirogagi)
                  if(past_number != number):
                           i = 0
                           num_mjpj = 0
                           menu_golla = 0
                           tbk_golla = 0
                           mr_golla = 0
                           br_golla = 0
                           tgr_golla = 0
                           dirogagi = False
                           hgcard = 0
                           ok = False
                           reset = False
                  past_number = number
                  
                  for event in pygame.event.get():
                           if event.type == pygame.MOUSEBUTTONUP:
                                    pygame.quit()
                                    sys.exit()
                  if number != 0:
                           if number==1:
                                    num_mjpj = 1
                                    menu_golla = 1
                                    tbk_golla = 1
                                    mr_golla = 1
                                    br_golla = 1
                                    tgr_golla = 1
                                    hgcard = 1
                           elif number==2:
                                    num_mjpj = 2
                                    menu_golla = 2
                                    tbk_golla = 2
                                    mr_golla = 2
                                    br_golla = 2
                                    tgr_golla = 2
                                    hgcard = 2
                           elif number==3:
                                    menu_golla = 3
                                    tbk_golla = 3
                                    mr_golla = 3
                                    br_golla = 3
                                    tgr_golla = 3
                           elif number==4:
                                    menu_golla = 4
                           elif number==5 and menu_damgi_sum !=0:
                                    ok = True
                           elif number==6:
                                    dirogagi = True
                           elif number==7:
                                    reset = True
                                             
                  else:
                           num_mjpj = 0
                           menu_golla = 0
                           tbk_golla = 0
                           mr_golla = 0
                           br_golla = 0
                           tgr_golla = 0
                           dirogagi = False
                           hgcard = 0
                           ok = False
                           reset = False

                  if firstpage == True:
                           screen.fill((255, 255, 255))

                           screen.blit(img_mj1, (50, 700)) # gojeong
                           screen.blit(img_pj1, (560, 700)) # gojeong
                           screen.blit(img_name, (0, 30))
                           screen.blit(img_camera_mjpj, (0, 1700))
                           
                           if num_mjpj == 1:
                                    screen.blit(img_mj2, (50, 700))
                                    screen.blit(img_time[i], (50, 65))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             nextpage1 = True
                                             firstpage = False

                           elif num_mjpj == 2:
                                    screen.blit(img_pj2, (560, 700))
                                    screen.blit(img_time[i], (50, 65))
                                    i = i + 1
                                    time.sleep(0.25)
                                    if i > 8:
                                            i = 0
                                            nextpage1 = True
                                            firstpage = False

                  if nextpage1 == True:
                           screen.fill((255, 255, 255))
                           screen.blit(img_tbk, (120, 360))
                           screen.blit(img_mr, (565, 360))
                           screen.blit(img_br, (120, 810))
                           screen.blit(img_tgr, (565, 810))
                           screen.blit(img_camera_ilban, (0, 1550))

                           if menu_golla == 1:
                                    screen.blit(img_tbk_dark, (120, 360))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             nextpage2_1 = True
                                             nextpage1 = False
                                    
                           elif menu_golla == 2:
                                    screen.blit(img_mr_dark, (565, 360))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             nextpage2_2 = True
                                             nextpage1 = False
                                    
                           elif menu_golla == 3:
                                    screen.blit(img_br_dark, (120, 810))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             nextpage2_3 = True
                                             nextpage1 = False
                                    
                           elif menu_golla == 4:
                                    screen.blit(img_tgr_dark, (565, 810))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             nextpage2_4 = True
                                             nextpage1 = False

                           if dirogagi:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 매장, 포장 초기화
                                             firstpage = True
                                             dirogagi = False
                                             nextpage1 = False
                                             nextpage2_1 = False
                                             nextpage2_2 = False
                                             nextpage2_3 = False
                                             nextpage2_4 = False
                           if ok:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             nextpage3 = True
                                             ok = False
                           if reset:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             firstpage = True
                                             nextpage1 = False
                                             nextpage2_1 = False
                                             nextpage2_2 = False
                                             nextpage2_3 = False
                                             nextpage2_4 = False
                                             dirogagi = False
                                             nextpage3 = False # 계산 화면
                                             lastpage = False
                                             tp = 0
                                             num_mjpj = 0
                                             menu_golla = 0
                                             i = 0
                                             menu_damgi.clear() # 이미지 저장
                                             menu_damgi_sum = 0 # 저장된 이미지 수
                                             jangbaguni.clear() # 메뉴 이름 담는
                                             reset = False
                           
                                             pygame.display.update()
                                             fps.tick(30)
                                    

                  if nextpage2_1 == True:
                           screen.fill((255, 255, 255))
                           screen.blit(img_tbk_1, (143, 300))
                           screen.blit(img_tbk_2, (143, 650))
                           screen.blit(img_tbk_3, (130, 1000))
                           screen.blit(img_camera_ilban, (0, 1550))

                           if tbk_golla == 1:
                                    screen.blit(img_tbk_dark_1, (143, 300))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_tbk_small_1)
                                             #screen.blit(img_tbk_small_1, (400 - menu_damgi_sum, 1200))
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("tbk_1")
                                             
                                             
                                    
                           elif tbk_golla == 2:
                                    screen.blit(img_tbk_dark_2, (143, 650))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_tbk_small_2)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("tbk_2")
                                             
                                    
                           elif tbk_golla == 3:
                                    screen.blit(img_tbk_dark_3, (130, 1000))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_tbk_small_3)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("tbk_3")
                                             

                           if dirogagi:
                                    print("back")
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 매장, 포장 초기화
                                             nextpage1 = True
                                             dirogagi = False
                                             nextpage2_1 = False

                           if ok:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             nextpage3 = True
                                             ok = False
                           if reset:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             firstpage = True
                                             nextpage1 = False
                                             nextpage2_1 = False
                                             nextpage2_2 = False
                                             nextpage2_3 = False
                                             nextpage2_4 = False
                                             dirogagi = False
                                             nextpage3 = False # 계산 화면
                                             lastpage = False
                                             tp = 0
                                             num_mjpj = 0
                                             menu_golla = 0
                                             i = 0
                                             menu_damgi.clear() # 이미지 저장
                                             menu_damgi_sum = 0 # 저장된 이미지 수
                                             jangbaguni.clear() # 메뉴 이름 담는
                                             reset = False
                           
                                             pygame.display.update()
                                             fps.tick(30)
                                    

                  if nextpage2_2 == True:
                           screen.fill((255, 255, 255))
                           screen.blit(img_mr_1, (143, 300))
                           screen.blit(img_mr_2, (143, 650))
                           screen.blit(img_mr_3, (143, 1000))
                           screen.blit(img_camera_ilban, (0, 1550))

                           if mr_golla == 1:
                                    screen.blit(img_mr_dark_1, (143, 300))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_mr_small_1)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("mr_1")
                                             
                                    
                           elif mr_golla == 2:
                                    screen.blit(img_mr_dark_2, (143, 650))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_mr_small_2)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("mr_2")
                                             
                                    
                           elif mr_golla == 3:
                                    screen.blit(img_mr_dark_3, (143, 1000))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_mr_small_3)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("mr_3")
                                             

                           if dirogagi:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 매장, 포장 초기화
                                             nextpage1 = True
                                             dirogagi = False
                                             nextpage2_2 = False
                           if ok:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             nextpage3 = True
                                             ok = False
                           if reset:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             firstpage = True
                                             nextpage1 = False
                                             nextpage2_1 = False
                                             nextpage2_2 = False
                                             nextpage2_3 = False
                                             nextpage2_4 = False
                                             dirogagi = False
                                             nextpage3 = False # 계산 화면
                                             lastpage = False
                                             tp = 0
                                             num_mjpj = 0
                                             menu_golla = 0
                                             i = 0
                                             menu_damgi.clear() # 이미지 저장
                                             menu_damgi_sum = 0 # 저장된 이미지 수
                                             jangbaguni.clear() # 메뉴 이름 담는
                                             reset = False
                           
                                             pygame.display.update()
                                             fps.tick(30)

                  if nextpage2_3 == True:
                           screen.fill((255, 255, 255))
                           screen.blit(img_br_1, (143, 300))
                           screen.blit(img_br_2, (143, 650))
                           screen.blit(img_br_3, (143, 1000))
                           screen.blit(img_camera_ilban, (0, 1550))

                           if br_golla == 1:
                                    screen.blit(img_br_dark_1, (143, 300))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_br_small_1)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("br_1")
                                             
                                    
                           elif br_golla == 2:
                                    screen.blit(img_br_dark_2, (143, 650))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_br_small_2)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("br_2")
                                             
                                    
                           elif br_golla == 3:
                                    screen.blit(img_br_dark_3, (143, 1000))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_br_small_3)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("br_3")
                                             

                           if dirogagi:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 매장, 포장 초기화
                                             nextpage1 = True
                                             dirogagi = False
                                             nextpage2_3 = False
                           if ok:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             nextpage3 = True
                                             ok = False

                           if reset:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             firstpage = True
                                             nextpage1 = False
                                             nextpage2_1 = False
                                             nextpage2_2 = False
                                             nextpage2_3 = False
                                             nextpage2_4 = False
                                             dirogagi = False
                                             nextpage3 = False # 계산 화면
                                             lastpage = False
                                             tp = 0
                                             num_mjpj = 0
                                             menu_golla = 0
                                             i = 0
                                             menu_damgi.clear() # 이미지 저장
                                             menu_damgi_sum = 0 # 저장된 이미지 수
                                             jangbaguni.clear() # 메뉴 이름 담는
                                             reset = False
                           
                                             pygame.display.update()
                                             fps.tick(30)

                  if nextpage2_4 == True:
                           screen.fill((255, 255, 255))
                           screen.blit(img_tgr_1, (143, 300))
                           screen.blit(img_tgr_2, (143, 650))
                           screen.blit(img_tgr_3, (143, 1000))
                           screen.blit(img_camera_ilban, (0, 1550))

                           if tgr_golla == 1:
                                    screen.blit(img_tgr_dark_1, (143, 300))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_tgr_small_1)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("tgr_1")
                                             
                                    
                           elif tgr_golla == 2:
                                    screen.blit(img_tgr_dark_2, (143, 650))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_tgr_small_2)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("tgr_2")
                                             
                                    
                           elif tgr_golla == 3:
                                    screen.blit(img_tgr_dark_3, (143, 1000))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 장바구니에 담는 코드
                                             menu_damgi.append(img_tgr_small_3)
                                             menu_damgi_sum = menu_damgi_sum + 1
                                             jangbaguni.append("tgr_3")
                                             

                           if dirogagi:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 매장, 포장 초기화
                                             nextpage1 = True
                                             dirogagi = False
                                             nextpage2_4 = False
                           if ok:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             nextpage3 = True
                                             ok = False
                           if reset:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             firstpage = True
                                             nextpage1 = False
                                             nextpage2_1 = False
                                             nextpage2_2 = False
                                             nextpage2_3 = False
                                             nextpage2_4 = False
                                             dirogagi = False
                                             nextpage3 = False # 계산 화면
                                             lastpage = False
                                             tp = 0
                                             num_mjpj = 0
                                             menu_golla = 0
                                             i = 0
                                             menu_damgi.clear() # 이미지 저장
                                             menu_damgi_sum = 0 # 저장된 이미지 수
                                             jangbaguni.clear() # 메뉴 이름 담는
                                             reset = False
                           
                                             pygame.display.update()
                                             fps.tick(30)
                           

                  for j in range (0, menu_damgi_sum):
                           screen.blit(menu_damgi[j], (1070 - ((menu_damgi_sum-j)*115), 1400))


                  if nextpage3 == True :
                           nextpage2_1 = False
                           nextpage2_2 = False
                           nextpage2_3 = False
                           nextpage2_4 = False
                           for j in range (0, menu_damgi_sum):
                                    tp = tp + price[jangbaguni[j]]
                           screen.fill((255, 255, 255))
                           screen.blit(img_hg, (110, 1400))
                           screen.blit(img_card, (620, 1400))
                           screen.blit(img_camera_hgcard, (0, 1700))
                           screen.blit(img_ysj, (75, 200))

                           count_tbk_1 = jangbaguni.count("tbk_1")
                           count_tbk_2 = jangbaguni.count("tbk_2")
                           count_tbk_3 = jangbaguni.count("tbk_3")
                           count_mr_1 = jangbaguni.count("mr_1")
                           count_mr_2 = jangbaguni.count("mr_2")
                           count_mr_3 = jangbaguni.count("mr_3")
                           count_br_1 = jangbaguni.count("br_1")
                           count_br_2 = jangbaguni.count("br_2")
                           count_br_3 = jangbaguni.count("br_3")
                           count_tgr_1 = jangbaguni.count("tgr_1")
                           count_tgr_2 = jangbaguni.count("tgr_2")
                           count_tgr_3 = jangbaguni.count("tgr_3")

                           total_count_tbk_1 = count_tbk_1*4500
                           total_count_tbk_2 = count_tbk_2*5000
                           total_count_tbk_3 = count_tbk_3*5000
                           total_count_mr_1 = count_mr_1*3000
                           total_count_mr_2 = count_mr_2*4000
                           total_count_mr_3 = count_mr_3*4500
                           total_count_br_1 = count_br_1*2000
                           total_count_br_2 = count_br_2*5000
                           total_count_br_3 = count_br_3*5000
                           total_count_tgr_1 = count_tgr_1*2000
                           total_count_tgr_2 = count_tgr_2*2500
                           total_count_tgr_3 = count_tgr_3*2500

                           total_cnt_tbk_1 = myFont1.render(str(total_count_tbk_1), True, (0, 0, 0))
                           total_cnt_tbk_2 = myFont1.render(str(total_count_tbk_2), True, (0, 0, 0))
                           total_cnt_tbk_3 = myFont1.render(str(total_count_tbk_3), True, (0, 0, 0))
                           total_cnt_mr_1 = myFont1.render(str(total_count_mr_1), True, (0, 0, 0))
                           total_cnt_mr_2 = myFont1.render(str(total_count_mr_2), True, (0, 0, 0))
                           total_cnt_mr_3 = myFont1.render(str(total_count_mr_3), True, (0, 0, 0))
                           total_cnt_br_1 = myFont1.render(str(total_count_br_1), True, (0, 0, 0))
                           total_cnt_br_2 = myFont1.render(str(total_count_br_2), True, (0, 0, 0))
                           total_cnt_br_3 = myFont1.render(str(total_count_br_3), True, (0, 0, 0))
                           total_cnt_tgr_1 = myFont1.render(str(total_count_tgr_1), True, (0, 0, 0))
                           total_cnt_tgr_2 = myFont1.render(str(total_count_tgr_2), True, (0, 0, 0))
                           total_cnt_tgr_3 = myFont1.render(str(total_count_tgr_3), True, (0, 0, 0))

                           cnt_tbk_1 = myFont1.render(str(count_tbk_1), True, (0, 0, 0))
                           cnt_tbk_2 = myFont1.render(str(count_tbk_2), True, (0, 0, 0))
                           cnt_tbk_3 = myFont1.render(str(count_tbk_3), True, (0, 0, 0))
                           cnt_mr_1 = myFont1.render(str(count_mr_1), True, (0, 0, 0))
                           cnt_mr_2 = myFont1.render(str(count_mr_2), True, (0, 0, 0))
                           cnt_mr_3 = myFont1.render(str(count_mr_3), True, (0, 0, 0))
                           cnt_br_1 = myFont1.render(str(count_br_1), True, (0, 0, 0))
                           cnt_br_2 = myFont1.render(str(count_br_2), True, (0, 0, 0))
                           cnt_br_3 = myFont1.render(str(count_br_3), True, (0, 0, 0))
                           cnt_tgr_1 = myFont1.render(str(count_tgr_1), True, (0, 0, 0))
                           cnt_tgr_2 = myFont1.render(str(count_tgr_2), True, (0, 0, 0))
                           cnt_tgr_3 = myFont1.render(str(count_tgr_3), True, (0, 0, 0))

                           screen.blit(cnt_tbk_1, (650, 285))
                           screen.blit(total_cnt_tbk_1, (855, 285))
                           screen.blit(cnt_tbk_2, (650, 355))
                           screen.blit(total_cnt_tbk_2, (855, 355))
                           screen.blit(cnt_tbk_3, (650, 425))
                           screen.blit(total_cnt_tbk_3, (855, 425))
                           screen.blit(cnt_mr_1, (650, 495))
                           screen.blit(total_cnt_mr_1, (855, 495))
                           screen.blit(cnt_mr_2, (650, 565))
                           screen.blit(total_cnt_mr_2, (855, 565))
                           screen.blit(cnt_mr_3, (650, 635))
                           screen.blit(total_cnt_mr_3, (855, 635))
                           screen.blit(cnt_br_1, (650, 705))
                           screen.blit(total_cnt_br_1, (855, 705))
                           screen.blit(cnt_br_2, (650, 775))
                           screen.blit(total_cnt_br_2, (855, 775))
                           screen.blit(cnt_br_3, (650, 845))
                           screen.blit(total_cnt_br_3, (855, 845))
                           screen.blit(cnt_tgr_1, (650, 915))
                           screen.blit(total_cnt_tgr_1, (855, 915))
                           screen.blit(cnt_tgr_2, (650, 985))
                           screen.blit(total_cnt_tgr_2, (855, 985))
                           screen.blit(cnt_tgr_3, (650, 1055))
                           screen.blit(total_cnt_tgr_3, (855, 1055))

                           total_count = myFont1.render(str(menu_damgi_sum), True, (0, 0, 0))
                           total_cnt = myFont1.render(str(tp), True, (0, 0, 0))
                           screen.blit(total_count, (650, 1125))
                           screen.blit(total_cnt, (855, 1125))
                           tp = 0

                           if hgcard == 1:
                                    screen.blit(img_hg_dark, (110, 1400))
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             lastpage = True
                                             nextpage2_1 = False
                                             nextpage2_2 = False
                                             nextpage2_3 = False
                                             nextpage2_4 = False
                                             nextpage3 = False
                                             
                           elif hgcard == 2:
                                    screen.blit(img_card_dark, (630, 1400))
                                    screen.blit(img_time[i], (50, 50))
                                    i = i + 1
                                    time.sleep(0.25)
                                    if i > 8:
                                            i = 0
                                            lastpage = True
                                            nextpage2_1 = False
                                            nextpage2_2 = False
                                            nextpage2_3 = False
                                            nextpage2_4 = False
                                            nextpage3 = False
 
                           if dirogagi:
                                    screen.blit(img_time[i], (50, 50))
                                    time.sleep(0.25)
                                    i = i + 1
                                    if i > 8:
                                             i = 0
                                             # 매장, 포장 초기화
                                             nextpage1 = True
                                             dirogagi = False
                                             nextpage3 = False
                                    
                  if lastpage == True:
                           screen.fill((255, 255, 255))
                           screen.blit(img_jumun_wan, (0, 600))
                           firstpage = True
                           tp = 0
                           num_mjpj = 0
                           menu_golla = 0
                           
                           i = 0
                           menu_damgi.clear() # 이미지 저장
                           menu_damgi_sum = 0 # 저장된 이미지 수
                           jangbaguni.clear() # 메뉴 이름 담는
                           lastpage = False
                           pygame.display.update()
                           fps.tick(30)
                           time.sleep(5)
                           nextpage3 = False
                                             
                  pygame.display.update()
                  fps.tick(30)

if __name__ == '__main__':
    main()
