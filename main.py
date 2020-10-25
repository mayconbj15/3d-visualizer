import pygame
import pygame_gui
import view_3d_object as view3d

pygame.init()
display = (400, 600)

manager = pygame_gui.UIManager((800, 600), './themes/theme.json')
manager.ui_theme.load_theme('./themes/theme.json')

pygame.display.set_caption("Quick Start")
window_surface = pygame.display.set_mode(display)

background = pygame.Surface(display)
background.fill(pygame.Color("#2D3947"))

showButton = pygame_gui.elements.UIButton(    
    relative_rect=pygame.Rect((150, 170), (100, 50)), 
    text="Show", 
    manager=manager, 
)
openFileButton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((150, 240), (100, 50)), text="Open File", manager=manager
)

shaderLabel = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((100, 310), (200, 50)),
    text="Choose a shader:",
    manager=manager,
)

chooseShaderLeftButton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 380), (90, 50)), text="Prev.", manager=manager
)

chooseShaderRightButton = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((210, 380), (90, 50)), text="Next", manager=manager
)


clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == showButton:
                    # view3d.main()
                    view3d.main()

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
