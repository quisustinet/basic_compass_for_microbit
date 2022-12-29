basic.show_icon(IconNames.HAPPY)

def on_forever():
    if input.compass_heading() > 358 or input.compass_heading() < 2:
        basic.show_arrow(ArrowNames.NORTH)
    elif input.compass_heading() > 43 and input.compass_heading() < 47:
        basic.show_arrow(ArrowNames.NORTH_WEST)
    elif input.compass_heading() > 88 and input.compass_heading() < 92:
        basic.show_arrow(ArrowNames.WEST)
    elif input.compass_heading() > 133 and input.compass_heading() < 137:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    elif input.compass_heading() > 178 and input.compass_heading() < 182:
        basic.show_arrow(ArrowNames.SOUTH)
    elif input.compass_heading() > 223 and input.compass_heading() < 227:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    elif input.compass_heading() > 268 and input.compass_heading() < 272:
        basic.show_arrow(ArrowNames.EAST)
    elif input.compass_heading() > 313 and input.compass_heading() < 317:
        basic.show_arrow(ArrowNames.NORTH_EAST)
    else:
        basic.clear_screen()
basic.forever(on_forever)
