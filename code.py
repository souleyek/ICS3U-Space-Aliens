#!/usr/bin/env python3

#created by Souleye Keita
# Created on : December 2023
# This program is the "Space Aliens" program on the pybadge

import ugame
import stage

import constants 


def game_scene():
    # This function is the main game game_scene

    # image banks for circuitpython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    #set the background to image 0 in the image bank
    #    and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66) 

    #create a stage for the gackground to show up on 
    # and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    #set the layers, items to show up in order
    game.layers = [ship] + [background]
    # render the background and initial location of sprite list
    #most likely you will only render background once per scene
    game.render_block()

#repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

    
        #update game logic

        # redraw sprites
        game.render_sprites([ship])
        game.tick()
        

   
if __name__ == "__main__":
    game_scene()

