import matplotlib.pyplot as plt
from matplotlib.widgets import Button

state = {'button_clicked': False}

def on_button_click(event):
    state['button_clicked'] = True
    print("Button clicked!")

def check_button_state():
    if state['button_clicked']:
        print("Button was clicked!")
    else:
        print("Button has not been clicked.")

# Create a figure and a button
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
button_ax = plt.axes([0.1, 0.1, 0.1, 0.075])
button = Button(button_ax, 'Click Me')

# Register the callback
button.on_clicked(on_button_click)

print(f"'state['button_clicked']' ='", state['button_clicked'] )

# Show the plot
plt.show()

# After closing the plot window, you can check the button state
check_button_state()



































# def simulate_click(position):
#     """Simulate a click on a given position."""
#     x, y = position[1], position[0]
#     event = type('', (), {})()  # Create an empty object to mimic an event
#     event.inaxes = ax  # Assuming ax is the chessboard axis
#     event.xdata = x + 0.5  # Add 0.5 to ensure it's centered on the box
#     event.ydata = y + 0.5  # Same for y
#     onclick(event)

# def selecting_piece_by_ai():
#     ai_decided_coordinates = (1, 1)
#     simulate_click(ai_decided_coordinates)

# # Example usage
# ax, fig, button_white, button_black, text, ax_button_white, ax_button_black = displaying_chessboard()
# piece_positions, piece_images, artists = placing_initialImages()

# # Binding the button click events to functions
# button_white.on_clicked(on_white_button_click)
# button_black.on_clicked(on_black_button_click)

# # Connect the figure to the onclick event
# cid = fig.canvas.mpl_connect('button_press_event', onclick)

# # Simulate AI click
# selecting_piece_by_ai()

# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# # Create an 8x8 grid for the chessboard
# chessboard = np.zeros((8, 8, 3))

# # Fill the chessboard with colors (black and white squares)
# for i in range(8):
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             chessboard[i, j] = [1, 1, 1]  # White squares
#         else:
#             chessboard[i, j] = [0, 0, 0]  # Black squares

# # Define the positions of the chess pieces
# white_pieces = [
#     ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
#     ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
# ]
# black_pieces = [
#     ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
#     ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
# ]

# # Create a figure and axis
# fig, ax = plt.subplots()

# # Display the chessboard
# ax.imshow(chessboard)

# # Add the white pieces with dark yellow color
# for i in range(8):
#     ax.text(i, 6, white_pieces[0][i], ha='center', va='center', fontsize=24, color='#FFD700')  # Dark yellow
#     ax.text(i, 7, white_pieces[1][i], ha='center', va='center', fontsize=24, color='#FFD700')  # Dark yellow

# # Add the black pieces with red color
# for i in range(8):
#     ax.text(i, 0, black_pieces[0][i], ha='center', va='center', fontsize=24, color='red')  # Red
#     ax.text(i, 1, black_pieces[1][i], ha='center', va='center', fontsize=24, color='red')  # Red

# # Simulate AI's turn by highlighting the 'R' at position (0,0)
# ai_position = (0, 0)
# ax.add_patch(plt.Rectangle(ai_position, 1, 1, fill=False, edgecolor='blue', linewidth=3))

# # Set the ticks to be empty (no axis numbers)
# ax.set_xticks([])
# ax.set_yticks([])

# # Set the aspect of the plot to be equal
# ax.set_aspect('equal')

# # Display the plot
# plt.show()


# # import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.widgets import Button

# def create_chessboard():
#     chessboard = np.zeros((8,8))
#     chessboard[1::2,::2] = 1
#     chessboard[::2,1::2] = 1
#     return chessboard

# def displaying_chessboard():
#     # Creating chessboard
#     chessboard = create_chessboard()

#     # Displaying the chessboard
#     fig, ax = plt.subplots(figsize=(6,6))
#     ax.imshow(chessboard, cmap='gray', interpolation='nearest')

#     # Remove the ticks
#     ax.set_xticks([])
#     ax.set_yticks([])

#     # Add player selection text
#     text = ax.text(3, 8, 'Choose Your Player:', fontsize=14, ha='center')

#     # Add buttons for White and Black
#     ax_button_white = plt.axes([0.25, -0.01, 0.15, 0.05])  # position x, y, width, height
#     ax_button_black = plt.axes([0.6, -0.01, 0.15, 0.05])
#     button_white = Button(ax_button_white, 'White')
#     button_black = Button(ax_button_black, 'Black')

#     return ax, fig, button_white, button_black, text, ax_button_white, ax_button_black

# def on_white_click(event):
#     global selected_player
#     selected_player = 'White'
#     text.set_text(f'Player Chosen: {selected_player}')
#     print(f'Player selected: {selected_player}')
#     remove_buttons_and_text()

# def on_black_click(event):
#     global selected_player
#     selected_player = 'Black'
#     text.set_text(f'Player Chosen: {selected_player}')
#     print(f'Player selected: {selected_player}')
#     remove_buttons_and_text()

# def remove_buttons_and_text():
#     # Remove buttons and text
#     button_white.ax.remove()
#     button_black.ax.remove()
#     text.remove()
#     plt.draw()

# # Display the chessboard and prompt
# ax, fig, button_white, button_black, text, ax_button_white, ax_button_black = displaying_chessboard()

# # Connect the buttons to their respective functions
# button_white.on_clicked(on_white_click)
# button_black.on_clicked(on_black_click)

# # Start with no player selected
# selected_player = None

# plt.show()


#     if players_turn_color == 'b' and click_position in piece_positions and piece_positions[click_position].startswith('b'):
#         print("Good move!!")
#     elif players_turn_color == 'w' and click_position in piece_positions and piece_positions[click_position].startswith('w'):
#         print("Good move!!")
#     else:
#         print('Invalid click')
#         return

# tcs.his@mediassist.in

# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.widgets import Button

# def create_chessboard():
#     chessboard = np.zeros((8,8))
#     chessboard[1::2,::2] = 1
#     chessboard[::2,1::2] = 1
#     return chessboard

# def displaying_chessboard():
#     # Creating chessboard
#     chessboard = create_chessboard()

#     # Displaying the chessboard
#     fig, ax = plt.subplots(figsize=(6,6))
#     ax.imshow(chessboard, cmap='gray', interpolation='nearest')

#     # Remove the ticks
#     ax.set_xticks([])
#     ax.set_yticks([])

#     # Position adjustment for the entire plot area to fit buttons and text below the chessboard
#     plt.subplots_adjust(bottom=0.2)

#     # Add player selection text
#     text = fig.text(0.5, 0.13, 'Choose Your Player:', fontsize=14, ha='center')

#     # Add buttons for White and Black
#     ax_button_white = plt.axes([0.25, 0.02, 0.15, 0.05])  # position x, y, width, height
#     ax_button_black = plt.axes([0.6, 0.02, 0.15, 0.05])
#     button_white = Button(ax_button_white, 'White')
#     button_black = Button(ax_button_black, 'Black')

#     return ax, fig, button_white, button_black, text

# def on_white_click(event):
#     global selected_player
#     selected_player = 'White'
#     text.set_text(f'Player Chosen: {selected_player}')
#     print(f'Player selected: {selected_player}')

# def on_black_click(event):
#     global selected_player
#     selected_player = 'Black'
#     text.set_text(f'Player Chosen: {selected_player}')
#     print(f'Player selected: {selected_player}')

# # Display the chessboard and prompt
# ax, fig, button_white, button_black, text = displaying_chessboard()

# # Connect the buttons to their respective functions
# button_white.on_clicked(on_white_click)
# button_black.on_clicked(on_black_click)

# # Start with no player selected
# selected_player = None

# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.widgets import Button

# def create_chessboard():
#     chessboard = np.zeros((8,8))
#     chessboard[1::2,::2] = 1
#     chessboard[::2,1::2] = 1
#     return chessboard

# def displaying_chessboard():
#     # Creating chessboard
#     chessboard = create_chessboard()

#     # Displaying the chessboard
#     fig, ax = plt.subplots(figsize=(6,6))
#     ax.imshow(chessboard, cmap='gray', interpolation='nearest')

#     # Remove the ticks
#     ax.set_xticks([])
#     ax.set_yticks([])
#     plt.plot()

#     # Add player selection text
#     text = ax.text(3, 8, 'Choose Your Player:', fontsize=14, ha='center')

#     # Add buttons for White and Black
#     ax_button_white = plt.axes([0.25, -0.01, 0.15, 0.05])  # position x, y, width, height
#     ax_button_black = plt.axes([0.6, -0.01, 0.15, 0.05])
#     button_white = Button(ax_button_white, 'White')
#     button_black = Button(ax_button_black, 'Black')

#     return ax, fig, button_white, button_black, text

# def on_white_click(event):
#     global selected_player
#     selected_player = 'White'
#     text.set_text(f'Player Chosen: {selected_player}')
#     print(f'Player selected: {selected_player}')

# def on_black_click(event):
#     global selected_player
#     selected_player = 'Black'
#     text.set_text(f'Player Chosen: {selected_player}')
#     print(f'Player selected: {selected_player}')

# # Display the chessboard and prompt
# ax, fig, button_white, button_black, text = displaying_chessboard()

# # Connect the buttons to their respective functions
# button_white.on_clicked(on_white_click)
# button_black.on_clicked(on_black_click)

# # Start with no player selected
# selected_player = None

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# import matplotlib.image as mpimg
# import matplotlib.patches as patches
# from PIL import Image, ImageEnhance, ImageOps

# def create_chessboard():
#     chessboard = np.zeros((8,8))
#     chessboard[1::2,::2] = 1
#     chessboard[::2,1::2] = 1
#     return chessboard

# def displaying_chessboard():
#     # Creating chessboard
#     chessboard = create_chessboard()

#     # Displaying the chessboard
#     # fig, ax = plt.subplots(figsize=(10,10))
#     fig, ax = plt.subplots()
#     ax.imshow(chessboard, cmap='gray', interpolation='nearest')

#     # Remove the ticks
#     ax.set_xticks([])
#     ax.set_yticks([])
#     return ax, fig

# ax, fig = displaying_chessboard()

# def placing_initialImages():
#     piece_images = {
#         'wr' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_rook.jpg'),
#         'wn' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_knight.jpg'),
#         'wq' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_queen.jpg'),
#         'wk' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_king.jpg'),
#         'wp' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_pawn.jpg'),
#         'wb' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_bishop.jpg'),
#         'br' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_rook.jpg'),
#         'bn' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_knight.jpg'),
#         'bq' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_queen.jpg'),
#         'bk' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_king.jpg'),
#         'bp' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_pawn.jpg'),
#         'bb' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_bishop.jpg'),
#     }

#     piece_positions = {
#         (0,0):'wr', (0,1):'wb', (0,2):'wn', (0,3):'wq', (0,4):'wk', (0,5):'wn', (0,6):'wb', (0,7):'wr',
#         **{(1,i):'wp' for i in range(8)},
#         **{(6,i):'bp' for i in range(8)},
#         (7,0):'br', (7,1):'bb', (7,2):'bn', (7,3):'bq', (7,4):'bk', (7,5):'bn', (7,6):'bb', (7,7):'br'
#     }
    
#     artists = {}  # To keep track of the positions of pieces and their corresponding artists
    
#     # Overlay the piece positions on the chessboard
#     for position, piece in piece_positions.items():
#         row, col = position
#         img = piece_images[piece]
        
#         imagebox = OffsetImage(img, zoom=0.51)
#         ab = AnnotationBbox(imagebox, (col, row), frameon=False)
#         ax.add_artist(ab)
#         artists[position] = ab

#     return piece_positions, piece_images, artists

# piece_positions, piece_images, artists = placing_initialImages()

# def remove_defeated_pieces_from_artist(img_position):
#     if img_position in artists:
#         artists[img_position].remove()
#         del artists[img_position]
    
#     # if img_position in piece_positions:
#     #     del piece_positions[img_position]

#     plt.draw()

# def onclick(event):
#     x, y = event.xdata, event.ydata
#     print(x, y)
#     if x is None or y is None:
#         print(" Click was outside the axes")
#     col = int(round(x))
#     row = int(round(y))
#     click_position = (row, col)
#     remove_defeated_pieces_from_artist(click_position)
    
    
    
    # if defeate_highlighted_pieces:
    #     print('defeate_highlighted_pieces=',defeate_highlighted_pieces)
    #     remove_defeat_highlightes_from_pieces(defeate_highlighted_pieces)
    # if defeate_highlighted_pieces and click_position in defeate_highlighted_pieces:
    #     print('you defeated opponent')
    #     remove_defeated_pieces_from_artist(click_position )


    # if defeate_highlighted_pieces:
    #     # Clear the list after removing highlights
    #     defeate_highlighted_pieces.clear() 
    # # if highlighted moves exists
    # if highlighted_boxes: # Clear previous highlights
    #     print("highlighted_boxes=", highlighted_boxes)
        
    #     # check the click, if it is inside the highlighted moves or not
    #     if click_position in highlighted_boxes_coordinates:
    #         print('you clicked inside highlighted box')
    #         for highlight in highlighted_boxes:
    #             highlight.remove()
    #         highlighted_boxes.clear()
    #         highlighted_boxes_coordinates.clear()
    #         # move the piece to the selected box
    #         move_piece_to_selected_box(click_position)
    #     else:
    #         print('you clicked outside highlighted area')
    #         for highlight in highlighted_boxes:
    #             highlight.remove()
    #         highlighted_boxes.clear()

    #         # check if it is clicked on piece
    #         if click_position in piece_positions:
    #             print('Showing possible highlights')

    #             # if clicked on piece then show possible moves
    #             highlight_possible_moves(click_position)            

    #         # check if it is clicked on empty space
    #         else:
    #             print('you clicked on the empty space')

    # # check the click, if it is not inside highlighted moves
    # else:
    #     # check if it is clicked on piece
    #     if click_position in piece_positions:
    #         print('Showing possible highlights')

    #         # if clicked on piece then show possible moves
    #         highlight_possible_moves(click_position)            

    #     # check if it is clicked on empty space
    #     else:
    #         print('you clicked on the empty space')

# connect the click event to the handler
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()









































# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# import matplotlib.image as mpimg
# import time

# def create_chessboard():
#     chessboard = np.zeros((8, 8))
#     chessboard[1::2, ::2] = 1
#     chessboard[::2, 1::2] = 1
#     return chessboard

# def displaying_chessboard():
#     chessboard = create_chessboard()
#     fig, ax = plt.subplots(figsize=(10, 10))
#     ax.imshow(chessboard, cmap='gray', interpolation='nearest')
#     ax.set_xticks([])
#     ax.set_yticks([])
#     return ax, fig

# ax, fig = displaying_chessboard()

# def placing_initialImages():
#     piece_images = {
#         'wr': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_rook.jpg'),
#         'wn': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_knight.jpg'),
#         'wq': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_queen.jpg'),
#         'wk': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_king.jpg'),
#         'wp': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_pawn.jpg'),
#         'wb': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_bishop.jpg'),
#         'br': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_rook.jpg'),
#         'bn': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_knight.jpg'),
#         'bq': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_queen.jpg'),
#         'bk': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_king.jpg'),
#         'bp': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_pawn.jpg'),
#         'bb': mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_bishop.jpg'),
#     }

#     piece_positions = {
#         (0, 0): 'wr', (0, 1): 'wb', (0, 2): 'wn', (0, 3): 'wq', (0, 4): 'wk', (0, 5): 'wn', (0, 6): 'wb', (0, 7): 'wr',
#         **{(1, i): 'wp' for i in range(8)},
#         **{(6, i): 'bp' for i in range(8)},
#         (7, 0): 'br', (7, 1): 'bb', (7, 2): 'bn', (7, 3): 'bq', (7, 4): 'bk', (7, 5): 'bn', (7, 6): 'bb', (7, 7): 'br'
#     }

#     artists = {}
#     for position, piece in piece_positions.items():
#         row, col = position
#         img = piece_images[piece]
#         imagebox = OffsetImage(img, zoom=0.51)
#         ab = AnnotationBbox(imagebox, (col, row), frameon=False)
#         ax.add_artist(ab)
#         artists[position] = ab

#     return piece_positions, piece_images, artists

# piece_positions, piece_images, artists = placing_initialImages()

# highlighted_areas = []
# global_possibleMoves = []
# image_position = []

# def highlight_possible_pawn_moves(position):
#     image_position.clear()
#     image_position.append(position)

#     row, col = position
#     possible_moves = []

#     if position in piece_positions and piece_positions[position].endswith('p'):
#         if piece_positions[position].startswith('w'):
#             if row < 7:
#                 if (row + 1, col) not in piece_positions:
#                     possible_moves.append((row + 1, col))
#                 if row == 1 and (row + 2, col) not in piece_positions:
#                     possible_moves.append((row + 2, col))

#     for move in possible_moves:
#         highlight = plt.Rectangle((move[1] - 0.5, move[0] - 0.5), 1, 1, color='yellow', alpha=0.5)
#         ax.add_patch(highlight)
#         highlighted_areas.append(highlight)
#     global_possibleMoves.extend(possible_moves)

#     plt.draw()

# def move_image_to_selected_box(new_piece_position, img_position):
#     piece = piece_positions[img_position]
#     img = piece_images[piece]

#     n_frames = 10  # Number of frames for the animation
#     old_col, old_row = img_position
#     new_col, new_row = new_piece_position

#     for i in range(n_frames + 1):
#         x = old_col + (new_col - old_col) * i / n_frames
#         y = old_row + (new_row - old_row) * i / n_frames

#         # Remove previous artist at the old position
#         if i > 0:
#             artists[img_position].remove()

#         # Draw the image at the interpolated position
#         imagebox = OffsetImage(img, zoom=0.51)
#         ab = AnnotationBbox(imagebox, (y, x), frameon=False)
#         ax.add_artist(ab)
#         artists[img_position] = ab

#         plt.pause(0.05)  # Pause to create the animation effect

#     # Update the piece's final position
#     piece_positions[new_piece_position] = piece
#     del piece_positions[img_position]
#     artists[new_piece_position] = artists.pop(img_position)

# def click_inside_highlighted_moves(click_position):
#     if click_position in global_possibleMoves:
#         global_possibleMoves.clear()
#         move_image_to_selected_box(click_position, image_position[0])

# def onclick(event):
#     x, y = event.xdata, event.ydata
#     if x is None or y is None:
#         return
#     col = int(round(x))
#     row = int(round(y))
#     position = (row, col)
    
#     if global_possibleMoves:
#         click_inside_highlighted_moves(position)
    
#     if highlighted_areas:
#         for highlight in highlighted_areas:
#             highlight.remove()
#         highlighted_areas.clear()
    
#     highlight_possible_pawn_moves(position)

# cid = fig.canvas.mpl_connect('button_press_event', onclick)

# plt.show()


#####################################################################

# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# import matplotlib.image as mpimg
# from matplotlib.patches import Rectangle

# def create_chessboard():
#     chessboard = np.zeros((8,8))
#     chessboard[1::2,::2] = 1
#     chessboard[::2,1::2] = 1
#     return chessboard

# def displaying_chessboard():
#     chessboard = create_chessboard()
#     fig, ax = plt.subplots()
#     ax.imshow(chessboard, cmap='gray', interpolation='nearest')
#     ax.set_xticks([])
#     ax.set_yticks([])
#     return ax, fig

# def placing_initialImages():
#     piece_images = {
#         'wr' : mpimg.imread('path_to_white_rook_image'),
#         # Other pieces...
#         'bb' : mpimg.imread('path_to_black_bishop_image'),
#     }

#     piece_positions = {
#         (0,0):'wr', (0,1):'wb', (0,2):'wn', (0,3):'wq', (0,4):'wk', (0,5):'wn', (0,6):'wb', (0,7):'wr',
#         **{(1,i):'wp' for i in range(8)},
#         **{(6,i):'bp' for i in range(8)},
#         (7,0):'br', (7,1):'bb', (7,2):'bn', (7,3):'bq', (7,4):'bk', (7,5):'bn', (7,6):'bb', (7,7):'br'
#     }
    
#     artists = {}
    
#     for position, piece in piece_positions.items():
#         row, col = position
#         img = piece_images[piece]
        
#         imagebox = OffsetImage(img, zoom=0.51)
#         ab = AnnotationBbox(imagebox, (col, row), frameon=False)
#         ax.add_artist(ab)
#         artists[position] = ab

#     return piece_positions, piece_images, artists

# def remove_defeated_pieces_from_artist(img_position):
#     if img_position in artists:
#         artists[img_position].remove()
#         del artists[img_position]
    
#     if img_position in piece_positions:
#         del piece_positions[img_position]

#     plt.draw()

# def highlight_possible_moves(position):
    
#     # Checking which piece is selected
#     if piece_positions[position].startswith('w'):
#         print("White is selected")
#         if piece_positions[position].endswith('p'):
#             print('White pawn is selected')
#             highlight_possible_moves_white_pawn(position)
#         elif piece_positions[position].endswith('r'):
#             print('white rook is selected')
#             highlight_possible_moves_white_rook(position)
#         elif piece_positions[position].endswith('b'):
#             print('White bishop is selected')
#         elif piece_positions[position].endswith('n'):
#             print('White Knight is selected')
#         elif piece_positions[position].endswith('q'):
#             print('White queen is selected')
#         elif piece_positions[position].endswith('k'):
#             print('White king is selected')

#     else:
#         print('Black is selected')
#         if piece_positions[position].endswith('p'):
#             print('Black pawn is selected')
#             highlight_possible_moves_black_pawn(position)
#         elif piece_positions[position].endswith('r'):
#             print('Black rook is selected')
#         elif piece_positions[position].endswith('b'):
#             print('Black bishop is selected')
#         elif piece_positions[position].endswith('n'):
#             print('Black Knight is selected')
#         elif piece_positions[position].endswith('q'):
#             print('Black queen is selected')
#         elif piece_positions[position].endswith('k'):
#             print('Black king is selected')

# def onclick(event):
#     if event.xdata is None or event.ydata is None:
#         print("Click was outside the axes")
#         return
    
#     x = int(round(event.xdata))
#     y = int(round(event.ydata))
#     click_position = (y, x)

#     if click_position in piece_positions:
#         print(f"Clicked on piece at position {click_position}")
#         if click_position in artists:
#             remove_defeated_pieces_from_artist(click_position)
#         else:
#             print(f"No artist found for position {click_position}")
#     else:
#         print("Clicked on an empty space")
    
#     if highlighted_boxes:
#         for highlight in highlighted_boxes:
#             highlight.remove()
#         highlighted_boxes.clear()
#         highlighted_boxes_coordinates.clear()
        
#     if click_position in piece_positions:
#         print('Showing possible highlights')
#         highlight_possible_moves(click_position)
#     else:
#         print('You clicked on the empty space')

# ax, fig = displaying_chessboard()
# piece_positions, piece_images, artists = placing_initialImages()
# highlighted_boxes = []
# highlighted_boxes_coordinates = []
# image_position = []
# defeate_highlighted_pieces = []

# cid = fig.canvas.mpl_connect('button_press_event', onclick)
# plt.show()
