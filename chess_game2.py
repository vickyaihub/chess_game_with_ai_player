import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import matplotlib.patches as patches
from matplotlib.widgets import Button
from ai_simulator import chessAI




# from ai_simulator import simulating_positions_bu_ai
def create_chessboard():
    chessboard = np.zeros((8,8))
    chessboard[1::2,::2] = 1
    chessboard[::2,1::2] = 1
    return chessboard

def displaying_chessboard():
    # Creating chessboard
    chessboard = create_chessboard()

    # Displaying the chessboard
    # fig, ax = plt.subplots(figsize=(10,10))
    fig, ax = plt.subplots(figsize=(4.7,6.5))
    ax.imshow(chessboard, cmap='gray', interpolation='nearest')

    # Remove the ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Add player selection text
    text = ax.text(3, 8, 'Choose Your Player:', fontsize=14, ha='center')

    # Add buttons for White and Black
    ax_button_white = plt.axes([0.25, 0.1, 0.15, 0.05])  # position x, y, width, height
    ax_button_black = plt.axes([0.6, 0.1, 0.15, 0.05])
    button_white = Button(ax_button_white, 'White')
    button_black = Button(ax_button_black, 'Black')

    return ax, fig, button_white, button_black, text, ax_button_white, ax_button_black


def placing_initialImages():
    piece_images = {
        'wr' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_rook.jpg'),
        'wn' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_knight.jpg'),
        'wq' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_queen.jpg'),
        'wk' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_king.jpg'),
        'wp' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_pawn.jpg'),
        'wb' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\white_bishop.jpg'),
        'br' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_rook.jpg'),
        'bn' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_knight.jpg'),
        'bq' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_queen.jpg'),
        'bk' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_king.jpg'),
        'bp' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_pawn.jpg'),
        'bb' : mpimg.imread('C:\\Users\\sha\\Documents\\my_work\\vickyaihub\\chess_pieces_images_reduced\\black_bishop.jpg'),
    }

    piece_positions = {
        (0,0):'wr', (0,1):'wb', (0,2):'wn', (0,3):'wq', (0,4):'wk', (0,5):'wn', (0,6):'wb', (0,7):'wr',
        **{(1,i):'wp' for i in range(8)},
        **{(6,i):'bp' for i in range(8)},
        (7,0):'br', (7,1):'bb', (7,2):'bn', (7,3):'bq', (7,4):'bk', (7,5):'bn', (7,6):'bb', (7,7):'br'
    }
    
    artists = {}  # To keep track of the positions of pieces and their corresponding artists
    
    # Overlay the piece positions on the chessboard
    for position, piece in piece_positions.items():
        row, col = position
        img = piece_images[piece]
        
        imagebox = OffsetImage(img, zoom=0.51)
        ab = AnnotationBbox(imagebox, (col, row), frameon=False)
        ax.add_artist(ab)
        artists[position] = ab

    return piece_positions, piece_images, artists





def plotting_yellow_rectangles(possible_moves):
    print('possible_moves=', possible_moves)
    for move in possible_moves:
        highlight = plt.Rectangle((move[1] - 0.5, move[0] - 0.5), 1, 1, color='yellow', alpha=0.5)
        ax.add_patch(highlight)
        highlighted_boxes.append(highlight)
    plt.draw()
    highlighted_boxes_coordinates.extend(possible_moves)
    possible_moves.clear()


def highlight_possible_moves_white_pawn(position):
    image_position.clear()
    image_position.append(position)
    possible_moves = []
    row, col = position
    if row < 7:
        if (row + 1, col) not in piece_positions:
            possible_moves.append((row + 1, col))
        if row == 1 and (row + 2, col) not in piece_positions:
            possible_moves.append((row + 2, col))
    plotting_yellow_rectangles(possible_moves)

def highlight_possible_moves_knight(position, players_turn_color):
    print('player_turn_color_knight=', players_turn_color)
    image_position.clear()
    image_position.append(position)
    possible_moves = []
    row, col = position
    # possible_moves = [
    #     (row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1),
    #     (row + 1, col + 2), (row + 1, col - 2), (row - 1, col + 2), (row - 1, col - 2)
    # ]
    # possible_moves = [(r, c) for r, c in possible_moves if 0 <= r <= 7 and 0 <= c <= 7 and (r, c) not in piece_positions]

    if row < 6:
        if (row+2, col+1) in piece_positions and players_turn_color != piece_positions[(row+2, col+1)][0]:
            defeate_highlighted_pieces.append((row+2, col+1))
            possible_moves.append((row+2, col+1))
        if (row+2, col - 1)  not in piece_positions:
            possible_moves.append((row+2, col+1))

        if (row+2, col+1) in piece_positions and players_turn_color != piece_positions[(row+2, col+1)][0]:
            defeate_highlighted_pieces.append((row+2, col - 1))            
        if (row+2, col - 1)  not in piece_positions:
            possible_moves.append((row+2, col-1))

    if row > 1:
        if (row-2, col+1) in piece_positions and players_turn_color != piece_positions[(row-2, col+1)][0]:
            defeate_highlighted_pieces.append((row-2, col+1)) 
        if (row-2, col+1) not in piece_positions:
            possible_moves.append((row-2, col+1))

        if (row-2, col-1) in piece_positions and players_turn_color != piece_positions[(row-2, col-1)][0]:
            defeate_highlighted_pieces.append((row-2, col-1)) 
        if (row-2, col-1) not in piece_positions:
            possible_moves.append((row-2, col-1))
    if col < 6:
        if (row+1, col+2) in piece_positions and players_turn_color != piece_positions[(row+1, col+2)][0]:
            defeate_highlighted_pieces.append((row+1, col+2))
        if (row+1, col+2) not in piece_positions:
            possible_moves.append((row+1, col+2))

        if (row-1, col+2)  in piece_positions and players_turn_color != piece_positions[(row-1, col+2)][0]:
            defeate_highlighted_pieces.append((row-1, col+2) )
        if (row-1, col+2) not in piece_positions:
            possible_moves.append((row-1, col+2))
    if col > 1:
        if (row+1, col-2)  in piece_positions and players_turn_color != piece_positions[(row+1, col-2)][0]:
            defeate_highlighted_pieces.append((row+1, col-2) )
        if (row+1, col-2) not in piece_positions:
            possible_moves.append((row+1, col-2))

        if (row-1, col-2)  in piece_positions and players_turn_color != piece_positions[(row-1, col-2)][0]:
            defeate_highlighted_pieces.append((row-1, col-2))
        if (row-1, col-2) not in piece_positions:
            possible_moves.append((row-1, col-2)) 
    possible_moves = list(set(possible_moves))
    plotting_yellow_rectangles(possible_moves)
    print('defeate_highlighted_pieces=', defeate_highlighted_pieces)
    outline_possible_defeat_pieces(defeate_highlighted_pieces)




def highlight_possible_moves_black_pawn(position):
    image_position.clear()
    image_position.append(position)
    possible_moves = []
    row, col = position
    if row > 0:
        if (row - 1, col) not in piece_positions:
            possible_moves.append((row - 1, col))
        if row == 6 and (row - 2, col) not in piece_positions:
            possible_moves.append((row - 2, col))
    plotting_yellow_rectangles(possible_moves)

def outline_possible_defeat_pieces(overlay_heightlight_cross_pieces):
    for pos in overlay_heightlight_cross_pieces: 
        if pos in artists:
            artists[pos].set_visible(False)
            artists[pos].remove()
            del artists[pos]
        
        # if pos in piece_positions:
        #     del piece_positions[pos]

        plt.draw()          
        # Get the piece at the given position
        piece = piece_positions[pos]
        img = piece_images[piece]

        # Display the image with reduced brightness at the correct position
        imagebox = OffsetImage(img, zoom=0.51)
        ab = AnnotationBbox(imagebox, (pos[1], pos[0]), frameon=True, bboxprops=dict(edgecolor='red', linewidth=2))
        ax.add_artist(ab)
        artists[pos] = ab

        
    plt.draw()

def remove_defeat_highlightes_from_pieces(defeate_highlighted_pieces):
    for pos in defeate_highlighted_pieces:    
        if pos in artists:
            # Remove the old artist with the red frame
            artists[pos].remove()
            del artists[pos]       
        # Get the piece at the given position
        piece = piece_positions[pos]
        img = piece_images[piece]

        # Display the image at the correct position without any frame
        imagebox = OffsetImage(img, zoom=0.51)
        ab = AnnotationBbox(imagebox, (pos[1], pos[0]), frameon=False)  # Removed bboxprops to eliminate the frame
        ax.add_artist(ab)
        artists[pos] = ab
        plt.draw()

    
    

def highlight_possible_moves_white_rook(position):
    image_position.clear()
    image_position.append(position)
    possible_moves_pre = []
    possible_moves = []
    row, col = position
    # rook can moves front and back
    # rook can moves laft and right
    # rook can hit anyone opposite
        # if color is blach, then highlight will cover + 1 piece
        # if color is white then highlight will stop before white

    for i in range(row + 1, 8): # Moving white rook upward        
        if (i, col) in piece_positions and piece_positions[(i, col)].startswith('w'):
            break
        elif (i, col) in piece_positions and piece_positions[(i, col)].startswith('b'):
            possible_moves.append((i, col))
            defeate_highlighted_pieces.append((i, col))
            break
        else:
            possible_moves.append((i, col))
    if row > 0:
        for i in range(row - 1, -1, -1 ): # Moving white piece downward
            if (i, col) in piece_positions and piece_positions[(i, col)].startswith('w'):
                break
            elif (i, col) in piece_positions and piece_positions[(i, col)].startswith('b'):
                possible_moves.append((i, col))
                defeate_highlighted_pieces.append((i, col))
                break
            else:
                possible_moves.append((i, col))
    for i in range(col + 1, 8): # Moving white rook right
        if (row, i) in piece_positions and piece_positions[(row, i)].startswith('w'):
            break
        elif (row, i) in piece_positions and piece_positions[(row, i)].startswith('b'):
            possible_moves.append((row, i))
            defeate_highlighted_pieces.append((row, i))
            break
        else:
            possible_moves.append((row, i))
    if col > 0:
        for i in range(col -1, -1, -1): # moving rook left
            if (row, i) in piece_positions and piece_positions[(row, i)].startswith('w'):
                break
            elif (row, i) in piece_positions and piece_positions[(row, i)].startswith('b'):
                possible_moves.append((row, i))
                defeate_highlighted_pieces.append((row, i))
                break
            else:
                possible_moves.append((row, i))
        
    plotting_yellow_rectangles(possible_moves)
    outline_possible_defeat_pieces(defeate_highlighted_pieces)
    

def move_piece_to_selected_box(click_position):
    print('You are moving the chess piece now')
    global players_turn_color
    global user_vs_ai_turn
    img_position = image_position[0]
    image_position.clear()
    new_row, new_col = click_position
    old_row, old_col = img_position
    piece = piece_positions[img_position]
    img = piece_images[piece]
    n_frames = 10
    # Hide the artist by setting visibility to False
    artists[img_position].set_visible(False)
    artists[img_position].remove()  # Remove artist from the axis
    del artists[img_position]  # Ensure artist is removed from the dictionary    
    plt.draw()  # Update the plot

    for i in range(n_frames + 1):
        x = old_row + (new_row - old_row) * i / n_frames
        y = old_col + (new_col - old_col) * i / n_frames
        

        # Remove the previous artist at the old position
        if i > 0:
            if img_position in artists:
                # Hide the artist by setting visibility to False
                artists[img_position].set_visible(False)
                artists[img_position].remove()  # Remove artist from the axis
                del artists[img_position]  # Ensure artist is removed from the dictionary
                
                plt.draw()  # Update the plot


        # Draw image at the interpolated position
        imagebox = OffsetImage(img, zoom=0.51)
        ab = AnnotationBbox(imagebox, (y,x), frameon=False)
        ax.add_artist(ab)
        artists[img_position] = ab

        plt.pause(0.05) # to create animation effect

    # Update the piece final position
    piece_positions[click_position] = piece
    del piece_positions[img_position]
    artists[click_position] = artists.pop(img_position)
    if players_turn_color == 'b':
        players_turn_color = 'w'
    else:
        players_turn_color = 'b'
    
    if user_vs_ai_turn == 'user':
        user_vs_ai_turn = 'ai'
    # allowing turn for another player
    check_ai_turn_or_user_turn()



    
def highlight_possible_moves(position):
    
    # Checking which piece is selected
    if piece_positions[position].startswith('w'):
        print("White is selected")
        if piece_positions[position].endswith('p'):
            print('White pawn is selected')
            highlight_possible_moves_white_pawn(position)
        elif piece_positions[position].endswith('r'):
            print('white rook is selected')
            highlight_possible_moves_white_rook(position)
        elif piece_positions[position].endswith('b'):
            print('White bishop is selected')
        elif piece_positions[position].endswith('n'):
            print('White Knight is selected')
            highlight_possible_moves_knight(position, players_turn_color)
        elif piece_positions[position].endswith('q'):
            print('White queen is selected')
        elif piece_positions[position].endswith('k'):
            print('White king is selected')

    else:
        print('Black is selected')
        if piece_positions[position].endswith('p'):
            print('Black pawn is selected')
            highlight_possible_moves_black_pawn(position)
        elif piece_positions[position].endswith('r'):
            print('Black rook is selected')
        elif piece_positions[position].endswith('b'):
            print('Black bishop is selected')
        elif piece_positions[position].endswith('n'):
            print('Black Knight is selected')
        elif piece_positions[position].endswith('q'):
            print('Black queen is selected')
        elif piece_positions[position].endswith('k'):
            print('Black king is selected')

def selecting_the_box_using_click(position):

    # Telling where click is done, i.e. on which piece or empty box
    if position in piece_positions:
        print("cilck was on the piece images")
        highlight_possible_moves()
    else:
        print("Click was done on empty boxes")
def remove_defeated_pieces_from_artist(img_position):
    if img_position in artists:
        artists[img_position].remove()
        del artists[img_position]

    if img_position in piece_positions:
        del piece_positions[img_position]

    plt.draw()
def eveluate_turn_color(click_position):
    # if color is black then next turn would be of white and vice versa
    if piece_positions[click_position].startswith('w'):
        turn_color = 'w'
    else:
        turn_color = 'b'
    return turn_color
def check_player_turn(pos):
    # 1. if player_turn_color black and piece[pos] black then ok
    # 2. if player_turn_color black and piece[pos] white then return None
    # 3. if player_turn_color white and piece[pos] white then ok
    # 4. if player_turn_color white and piece[pos] black then return None
    # 4. if player_turn_color black or white and piece[pos] is empty then ok
    # 4. else return None
    if pos not in piece_positions:
        print('you clicked on empty box______')
        return True
    elif players_turn_color == piece_positions[pos][0]:
        print('players_turn_color_______=', players_turn_color)
        print('piece_positions[pos]_______=', piece_positions[pos][0])
        return True
    else:
        return False

def onclick(event):
    global ai_player_color

    if event.inaxes in [ax_button_white, ax_button_black]:
        print('button clicked')
        return
    
    x, y = event.xdata, event.ydata
    print(x, y)
    if x is None or y is None:
        print(" Click was outside the axes")
    col = int(round(x))
    row = int(round(y))
    click_position = (row, col)

    if ai_player_color == None and piece_positions[click_position].startswith('w'):
        ai_player_color = 'b'
    elif ai_player_color == None and piece_positions[click_position].startswith('b'):
        ai_player_color = 'w'

    # Chacking turn and avoid unnecessary clicking
    check_turn = check_player_turn(click_position)
    if check_turn is False:
        return
        
    if defeate_highlighted_pieces:
        print('defeate_highlighted_pieces=',defeate_highlighted_pieces)
        remove_defeat_highlightes_from_pieces(defeate_highlighted_pieces)
    if defeate_highlighted_pieces and click_position in defeate_highlighted_pieces:
        print('you defeated opponent')
        remove_defeated_pieces_from_artist(click_position)


    if defeate_highlighted_pieces:
        # Clear the list after removing highlights
        defeate_highlighted_pieces.clear()
    # if highlighted moves exists
    if highlighted_boxes: # Clear previous highlights
        print("highlighted_boxes=", highlighted_boxes)
        
        # check the click, if it is inside the highlighted moves or not
        if click_position in highlighted_boxes_coordinates:
            print('you clicked inside highlighted box')
            for highlight in highlighted_boxes:
                highlight.remove()
            highlighted_boxes.clear()
            highlighted_boxes_coordinates.clear()
            # move the piece to the selected box
            move_piece_to_selected_box(click_position)            
        else:
            print('you clicked outside highlighted area')
            for highlight in highlighted_boxes:
                highlight.remove()
            highlighted_boxes.clear()

            # check if it is clicked on piece
            if click_position in piece_positions:
                print('Showing possible highlights')

                # if clicked on piece then show possible moves
                highlight_possible_moves(click_position)            

            # check if it is clicked on empty space
            else:
                print('you clicked on the empty space')

    # check the click, if it is not inside highlighted moves
    else:
        # check if it is clicked on piece
        if click_position in piece_positions:
            print('Showing possible highlights')

            # if clicked on piece then show possible moves
            highlight_possible_moves(click_position)            

        # check if it is clicked on empty space
        else:
            print('you clicked on the empty space')



def on_white_button_click(event):
    global players_turn_color
    players_turn_color = 'w'
    text.set_text(f'Player choosen White')
    remove_buttons_and_text()
def remove_buttons_and_text():
    button_white.ax.remove()
    button_black.ax.remove()
    text.remove()
    plt.draw()
def on_black_button_click(event):
    global players_turn_color
    players_turn_color = 'b'
    text.set_text('Player choosen Black')
    remove_buttons_and_text()

def getting_positions_from_ai():
    # chess_ai = chessAI(piece_positions, piece_images, artists, ax, fig, players_turn_color)
    # chess_ai.simulating_positions_bu_ai()
    # Create list of all possible moves
    # know all the player's positions and their possible moves
    # Target to kill king
    # know where the kning is at present
    # know all the risks
    # know all the possible killings of all the pieces
    # reach target by saving himself
    # know all the routes
    # Finally killing the king
    # make a huge database
    # make a separate file
    pass

def selecting_piece_by_ai():
    print('AI is selecting piece')
    ai_decided_piece_coordinates = (1,1)
    ai_decided_piece_move_coordinates = (3,1)
    chess_ai = chessAI(piece_positions, piece_images, artists, ax, fig, ai_player_color)
    ai_decided_piece_coordinates, ai_decided_piece_move_coordinates = chess_ai.simulating_positions_bu_ai()

    # check if it is clicked on piece
    if ai_decided_piece_coordinates in piece_positions:
        print('Showing possible highlights')

        # if clicked on piece then show possible moves
        highlight_possible_moves(ai_decided_piece_coordinates)
        plt.pause(0.5)
        move_piece_to_selected_box(ai_decided_piece_move_coordinates)

    # check if it is clicked on empty space
    else:
        print('you clicked on the empty space')
    
    # ax.add_patch(plt.Rectangle(ai_decided_coordinates, 1, 1, fill=False, edgecolor='blue', linewidth=3))
    return 

def check_ai_turn_or_user_turn():
    print('check_ai_turn_or_user_turn function called')
    if user_vs_ai_turn == 'ai':
        selecting_piece_by_ai()
    else:
        return






ax, fig, button_white, button_black, text, ax_button_white, ax_button_black = displaying_chessboard()
piece_positions, piece_images, artists = placing_initialImages()


#List to keep the track of Highlighted areas
highlighted_boxes = []
highlighted_boxes_coordinates = []
image_position = []
defeate_highlighted_pieces = []

users_turn = []
ai_turn = []
user_vs_ai_turn = 'user'
players_turn_color = 'beginning'
ai_player_color = None




# Selecting color
button_white.on_clicked(on_white_button_click)
button_black.on_clicked(on_black_button_click)



# connect the click event to the handler
cid = fig.canvas.mpl_connect('button_press_event', onclick)



plt.show()

