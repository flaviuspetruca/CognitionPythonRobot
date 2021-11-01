import pygame
pygame.key.set_repeat(1,10)

son = pygame.mixer.Sound("bip.wav")
sonlong = pygame.mixer.Sound("biplong.wav")
                    if event.key == pygame.K_TAB:
                        pygame.key.set_repeat(0)
                        chg_gamemode()
                        break