import uagame

def main():
    window = uagame.Window('Remember the Word', 500, 400)
    # display icon
    icon_string = 'UA'
    
    window.set_font_size(50)
    window.set_font_color('red')
    window.set_bg_color('blue')
    icon_width = window.get_string_width(icon_string)
    surface_width = window.get_width()
    x_coord_icon = surface_width - icon_width
    
    icon_height = window.get_font_height()
    surface_height = window.get_height()
    y_coord_icon = surface_height - icon_height
    
    window.draw_string('UA', x_coord_icon, y_coord_icon)
    window.close()
    
main()