import pygame
import random

# Inisialisasi pygame
pygame.init()
pygame.display.set_caption("Run Games")  # Mengatur judul layar
pygame.mixer.init()
pygame.mixer.music.load("dino_run.mp3")  # Memuat suara
pygame.mixer.music.play(-1)  # Memulai suara

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)


# Ukuran layar
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Kecepatan FPS
FPS = 60
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 30)

# Menginisialisasi gambar
dino_run_images = [
    pygame.image.load("0.png"),  # Gambar dinosaurus frame 1
    pygame.image.load("1.png"),  # Gambar dinosaurus frame 2
    pygame.image.load("2.png"),  # Gambar dinosaurus frame 3
    pygame.image.load("3.png"),  # Gambar dinosaurus frame 1
    pygame.image.load("4.png"),  # Gambar dinosaurus frame 2
    pygame.image.load("5.png"),  # Gambar dinosaurus frame 3
    pygame.image.load("6.png")   # Gambar dinosaurus frame 3
]

dino_jump_images = [
    pygame.image.load("junp1.png"),  # Gambar dinosaurus lompat frame 1
    pygame.image.load("jump2.png"),  # Gambar dinosaurus lompat frame 2
]

# Resize gambar dinosaurus
dino_run_images = [pygame.transform.scale(img, (60, 60)) for img in dino_run_images]
dino_jump_images = [pygame.transform.scale(img, (60, 60)) for img in dino_jump_images]

obstacle_image = pygame.image.load("obstacle.png")  # Gambar rintangan
obstacle_image = pygame.transform.scale(obstacle_image, (50, 50))  # Ukuran rintangan
background_image = pygame.image.load("background.png")  # Gambar latar belakang
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Ukuran latar belakang
menu_background_image = pygame.image.load("s.jpg")  # Gambar latar belakang menu
menu_background_image = pygame.transform.scale(menu_background_image, (WIDTH, HEIGHT))  # Ukuran latar belakang menu

# Checkpoint backgrounds
checkpoint_backgrounds = [
    pygame.image.load("checkpoint1.png"),
    pygame.image.load("checkpoint2.png"),
    pygame.image.load("checkpoint3.png"),
]
checkpoint_backgrounds = [pygame.transform.scale(bg, (WIDTH, HEIGHT)) for bg in checkpoint_backgrounds]

# Inisialisasi suara
jump_sound = pygame.mixer.Sound("jump.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")
pass_obstacle_sound = pygame.mixer.Sound("pass_obstacle.wav")

# Karakter Dinosaurus
dino_width = 50
dino_height = 40
dino_x = 50
dino_y = HEIGHT - dino_height - 40 
dino_velocity = 0

# Rintangan
obstacle_width = 20
obstacle_height = 20
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 30
obstacle_velocity = 5

# Fungsi untuk menampilkan skor dan level
def display_score(score, level, checkpoint):
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    checkpoint_text = font.render(f"Checkpoint: {checkpoint+1}", True, WHITE)  # Display checkpoint number
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))
    screen.blit(checkpoint_text, (WIDTH // 2 - checkpoint_text.get_width() // 2, HEIGHT - 390))

def game_over():
    # Displaying the custom Game Over image
    game_over_image = pygame.image.load("game_over_image.png")  # Path to your game over image
    game_over_image = pygame.transform.scale(game_over_image, (WIDTH - 400, HEIGHT - 200))  # Resize the image
    screen.blit(game_over_image, (0, 0))  # Draw the image on the screen

    # Creating a "Restart" button
    restart_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)  # Button area
    pygame.draw.rect(screen, (200, 0, 0), restart_button_rect)  # Drawing the button rectangle (Red)

    # Displaying the "Restart" text on the button
    restart_text = font.render("Restart Loop", True, WHITE)
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 10))

    # Display the "Quit" button (optional)
    quit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 50)  # Button area
    pygame.draw.rect(screen, (200, 0, 0), quit_button_rect)  # Drawing the quit button rectangle (Red)
    quit_text = font.render("Quit Games", True, WHITE)
    screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 70))

    pygame.display.update()  # Update the display
    return restart_button_rect, quit_button_rect  # Return button areas for interaction


def handle_game_over():
    # Loop for handling button clicks or keyboard presses after game over
    game_running = True
    restart_button_rect, quit_button_rect = game_over()

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse clicks
                mouse_pos = pygame.mouse.get_pos()  # Get mouse position
                if restart_button_rect.collidepoint(mouse_pos):  # Check if restart button is clicked
                    return "restart"  # Restart the game
                elif quit_button_rect.collidepoint(mouse_pos):  # Check if quit button is clicked
                    pygame.quit()  # Exit the game

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # 'R' key to restart
                    return "restart"
                elif event.key == pygame.K_q:  # 'Q' key to quit
                    pygame.quit()
                    return "quit"

# Fungsi untuk menampilkan menu utama
def main_menu():
    screen.fill(WHITE)
    screen.blit(menu_background_image, (0, 0))  # Menampilkan latar belakang menu
    
    # Menampilkan gambar judul Dino Run Game
    title_image = pygame.image.load("dino_run_game.png")  # Ganti dengan path gambar Anda
    title_image = pygame.transform.scale(title_image, (400, 200))  # Ukuran gambar judul
    screen.blit(title_image, (WIDTH // 2 - title_image.get_width() // 2, HEIGHT // 3 - 100))  # Posisi gambar judul
    
    # Membuat efek kelap-kelip pada teks "Press Enter to Start"
    start_text = font.render("Press Enter to Start", True, BLACK)
    
    # Menentukan interval kelap-kelip
    current_time = pygame.time.get_ticks()
    if (current_time // 500) % 2 == 0:  # Ganti teks setiap 500ms
        start_text = font.render("Press Enter to Start", True, (150, 150, 150))  # Teks redup
    
    # Menampilkan teks kelap-kelip
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.update()

# Fungsi untuk permainan
def game_loop():
    global dino_y, dino_velocity, obstacle_x, obstacle_velocity, obstacle_y
    score = 0
    level = 1
    checkpoint = 0  # To track which checkpoint the player has reached
    jump = False
    game_running = True
    passed_obstacles = 0

    # Background movement variables
    bg_x1 = 0
    bg_x2 = WIDTH

    # Dinosaur animation frames
    frame_counter = 0  # Counter to cycle through frames
    dino_run_frame = 0  # Current running frame to display
    dino_jump_frame = 0  # Current jumping frame to display
    jump_frame_counter = 0  # Counter for jump frames

    checkpoint_positions = []  # To store the positions of the checkpoints

    while game_running:
        # Change background every checkpoint
        screen.blit(checkpoint_backgrounds[checkpoint], (0, 0))

        # Move background
        bg_x1 -= 5  # Background speed
        bg_x2 -= 5  # Background speed
        
        if bg_x1 <= -WIDTH:
            bg_x1 = WIDTH
        if bg_x2 <= -WIDTH:
            bg_x2 = WIDTH

        # Draw moving background
        screen.blit(background_image, (bg_x1, 0))
        screen.blit(background_image, (bg_x2, 0))

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        # Control dino movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not jump:
            dino_velocity = -15
            jump = True
            jump_sound.play()  # Play jump sound

        # Move dino
        dino_velocity += 1  # gravity
        dino_y += dino_velocity

        if dino_y > HEIGHT - dino_height - 40:
            dino_y = HEIGHT - dino_height - 40
            jump = False

        # Move obstacles
        obstacle_x -= obstacle_velocity

        # If obstacle passes the screen, create a new one
        if obstacle_x < -obstacle_width:
            obstacle_x = WIDTH
            obstacle_y = HEIGHT - random.randint(20, 70)  # Randomize obstacle height
            score += 1
            passed_obstacles += 1
            pass_obstacle_sound.play()  # Play obstacle pass sound

            # Update level every 5 obstacles
            if passed_obstacles % 5 == 0:
                level += 1
                obstacle_velocity += 1  # Increase obstacle speed

            # Check if player reached a checkpoint
            if passed_obstacles % 10 == 0:
                checkpoint += 1  # Advance to next checkpoint
                if checkpoint >= len(checkpoint_backgrounds):  # Limit checkpoint number
                    checkpoint = len(checkpoint_backgrounds) - 1

                # Add new checkpoint position to the list
                checkpoint_positions.append(obstacle_x + 100)  # You can adjust the x position as needed

        # Draw checkpoint markers
        for checkpoint_position in checkpoint_positions:
            pygame.draw.circle(screen, (255, 0, 0), (checkpoint_position, HEIGHT - 50), 10)  # Red circle marker

        # Detect collision with obstacles
        if (dino_x + dino_width > obstacle_x and dino_x < obstacle_x + obstacle_width) and (dino_y + dino_height > obstacle_y):
            game_running = False
            game_over_sound.play()  # Play game over sound

        # Change dinosaur animation frames every few frames
        frame_counter += 1
        if frame_counter >= 10:  # Every 10 frames, change image
            dino_run_frame = (dino_run_frame + 1) % 3  # Cycle through frames 0, 1, 2
            frame_counter = 0

        # Jump animation
        if jump:
            jump_frame_counter += 1
            if jump_frame_counter >= 5:  # Change jump frame every 5 frames
                dino_jump_frame = (dino_jump_frame + 1) % 2  # Cycle through jump frames 0, 1
                jump_frame_counter = 0
            screen.blit(dino_jump_images[dino_jump_frame], (dino_x, dino_y))  # Display jump frame
        else:
            screen.blit(dino_run_images[dino_run_frame], (dino_x, dino_y))  # Display run frame

        # Display obstacles
        screen.blit(obstacle_image, (obstacle_x, obstacle_y))

        # Display score, level, and checkpoint
        display_score(score, level, checkpoint)

        # Check if game over
        if not game_running:
            result = handle_game_over()
            if result == "restart":
                game_loop()  # Restart the game
            else:
                break  # Quit the game

        pygame.display.update()
        clock.tick(FPS)

# Menampilkan menu utama
def start_game():
    game_started = False
    while not game_started:
        main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_started = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Menekan Enter untuk mulai
                    game_started = True
    game_loop()

# Memulai permainan
start_game()

# Menutup pygame
pygame.quit()
