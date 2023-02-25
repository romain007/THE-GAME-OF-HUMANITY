def signe(a,b):
  if a<b:
    return -1
  if a>b:
    return 1
  else:
    return 0
    
#A partir de la matrice, affichage de tous les élèments avec pygame
def affichage(var=0):
  """lance pygame et affiche la matrice. Option d'écart entre chaque point matricielle et de décallage pour centrer la matrice"""
  global save

  screen.fill((99,199,77))
  ecart = diviseur[parametre["ZOOM"]]
  param=["food","player_red","player_blue"]
  historique=[]


  for loop in range(ecart):
    for position in save:


        if save[position]["objet"] in param:
          

          new_position = [key for key, value in statistique.items() if value['IDENTIFIANT'] == save[position]['IDENTIFIANT']][0]
          print("POSITION INITIALE :",position,"POSITION FINALE :",new_position)
          
          coordonnée = (position[0]*ecart,position[1]*ecart)


          historique.append((coordonnée[0]+1*signe(position[0],new_position[0]),coordonnée[1]+1*signe(position[1],new_position[1])))

  for i in historique:          
  #historique.append((new_position[0]*ecart+1,new_position[1]*ecart+1))
    screen.blit(image[save[position]["objet"]],i)

  pygame.display.update()
  time.sleep(0.1)
  time.sleep(var)

        
  



  save=statistique.copy()

  time.sleep(var)