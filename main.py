basic.show_icon(IconNames.HAPPY)

def on_forever():
    if input.compass_heading() > 358 or input.compass_heading() < 2:
        basic.show_arrow(ArrowNames.NORTH)
    elif input.compass_heading() > 178 and input.compass_heading() < 182:
        basic.show_arrow(ArrowNames.SOUTH)
    elif input.compass_heading() > 88 and input.compass_heading() < 92:
        basic.show_arrow(ArrowNames.WEST)
    elif input.compass_heading() > 268 and input.compass_heading() < 272:
        basic.show_arrow(ArrowNames.EAST)
    else:
        basic.clear_screen()
basic.forever(on_forever)
