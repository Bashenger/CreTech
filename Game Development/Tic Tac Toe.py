import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 650
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_GREY = (200, 200, 200)
FONT_SIZE = 48
font = pygame.font.Font(None, FONT_SIZE)
BACKGROUND_COLOR = (50, 50, 50)

class Game:
    """
    Represents the Tic-Tac-Toe game.
    """
    def __init__(self):
        """
        Initializes the game board, sets the starting player, and sets the game state.
        """
        self.board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.current_player = 'X'
        self.game_state = 'Playing'
        self.winner = None
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.clock = pygame.time.Clock()
        self.scores = {'X': 0, 'O': 0}

    def reset_board(self):
        """
        Resets the game board and game state to start a new game.
        """
        self.board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.current_player = 'X'
        self.game_state = 'Playing'
        self.winner = None

    def display_board(self):
        """
        Prints the current state of the board to the console.
        """
        for row in self.board:
            print(row)

    def draw_board(self):
        """
        Draws the Tic-Tac-Toe board on the Pygame screen.
        """
        self.screen.fill(BACKGROUND_COLOR)  # Fill with background color
        for row in range(1, GRID_SIZE):
            pygame.draw.line(self.screen, LIGHT_GREY, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), 2)  # Change grid color
            pygame.draw.line(self.screen, LIGHT_GREY, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT - 50), 2)  # Change grid color

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                cell = self.board[row][col]
                if cell == 'X':
                    x_pos = col * CELL_SIZE + CELL_SIZE // 4
                    y_pos = row * CELL_SIZE + CELL_SIZE // 4
                    # Draw thicker X
                    pygame.draw.line(self.screen, RED, (x_pos, y_pos), (x_pos + CELL_SIZE // 2, y_pos + CELL_SIZE // 2), 4)  # Increased thickness
                    pygame.draw.line(self.screen, RED, (x_pos + CELL_SIZE // 2, y_pos), (x_pos, y_pos + CELL_SIZE // 2), 4)  # Increased thickness
                elif cell == 'O':
                    x_pos = col * CELL_SIZE + CELL_SIZE // 4
                    y_pos = row * CELL_SIZE + CELL_SIZE // 4
                    # Draw thicker O
                    pygame.draw.circle(self.screen, BLUE, (x_pos + CELL_SIZE // 4, y_pos + CELL_SIZE // 4), CELL_SIZE // 4, 4)  # Increased thickness

    def make_move(self, row, col):
        """
        Attempts to make a move at the specified row and column.

        Args:
            row: The row index (0, 1, or 2).
            col: The column index (0, 1, or 2).

        Returns:
            True if the move was successful, False otherwise.
        """
        if self.game_state != 'Playing':
            return False
        if not self.is_valid_move(row, col):
            return False
        self.board[row][col] = self.current_player
        self.display_board()
        if self.check_win():
            self.game_state = 'Win'
            self.winner = self.current_player
            self.scores[self.winner] += 1
            return True
        elif self.check_draw():
            self.game_state = 'Draw'
            return True
        else:
            self.switch_player()
            return True

    def is_valid_move(self, row, col):
        """
        Checks if a move is valid.

        Args:
            row: The row index (0, 1, or 2).
            col: The column index (0, 1, or 2).

        Returns:
            True if the move is valid, False otherwise.
        """
        if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
            return False
        if self.board[row][col] != ' ':
            return False
        return True

    def check_win(self):
        """
        Checks if the current player has won the game.

        Returns:
            True if the current player has won, False otherwise.
        """
        player = self.current_player
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(GRID_SIZE):
            if all(self.board[row][col] == player for row in range(GRID_SIZE)):
                return True
        if all(self.board[i][i] == player for i in range(GRID_SIZE)):
            return True
        if all(self.board[i][GRID_SIZE - 1 - i] == player for i in range(GRID_SIZE)):
            return True
        return False

    def check_draw(self):
        """
        Checks if the game is a draw.

        Returns:
            True if the game is a draw, False otherwise.
        """
        return all(cell != ' ' for row in self.board for cell in row)

    def switch_player(self):
        """
        Switches the current player from 'X' to 'O' or vice versa.
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_empty_cells(self):
        """
        Returns a list of empty cells (row, col) on the board.
        """
        empty_cells = []
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == ' ':
                    empty_cells.append((row, col))
        return empty_cells

    def ai_move(self):
        """
        Makes a move for the AI player ('O').  This is a basic random move strategy.
        """
        if self.game_state != 'Playing':
            return
        empty_cells = self.get_empty_cells()
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)

    def display_game_over_message(self):
        """Displays the game over message."""
        if self.game_state == 'Win':
            message = f"Player {self.winner} wins!"
        else:
            message = "It's a Draw!"
        text = font.render(message, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        play_again_button = pygame.Rect(WIDTH // 4, HEIGHT * 3 // 4, WIDTH // 2, 50)
        pygame.draw.rect(self.screen, GREEN, play_again_button)
        play_again_text = font.render("Play Again", True, WHITE)
        play_again_text_rect = play_again_text.get_rect(center=play_again_button.center)
        self.screen.blit(play_again_text, play_again_text_rect)
        return play_again_button

    def handle_click(self, pos):
        """
        Handles mouse clicks during the game.

        Args:
            pos: The (x, y) coordinates of the mouse click.
        """
        if self.game_state == 'Playing':
            col = pos[0] // CELL_SIZE
            row = pos[1] // CELL_SIZE
            self.make_move(row, col)
        elif self.game_state in ('Win', 'Draw'):
            play_again_button = pygame.Rect(WIDTH // 4, HEIGHT * 3 // 4, WIDTH // 2, 50)
            if play_again_button.collidepoint(pos):
                self.reset_board()

    def draw_score(self):
        """Draws the scorecard on the screen, below the board."""
        score_text = font.render(f"Score - X: {self.scores['X']}  O: {self.scores['O']}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT - 25))
        self.screen.blit(score_text, score_rect)

    def run(self):
        """
        Runs the main game loop.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
            self.draw_board()
            self.draw_score()
            if self.game_state in ('Win', 'Draw'):
                play_again_button = self.display_game_over_message()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
