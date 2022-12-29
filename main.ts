basic.showIcon(IconNames.Happy)
basic.forever(function on_forever() {
    if (input.compassHeading() > 358 || input.compassHeading() < 2) {
        basic.showArrow(ArrowNames.North)
    } else if (input.compassHeading() > 178 && input.compassHeading() < 182) {
        basic.showArrow(ArrowNames.South)
    } else if (input.compassHeading() > 88 && input.compassHeading() < 92) {
        basic.showArrow(ArrowNames.West)
    } else if (input.compassHeading() > 268 && input.compassHeading() < 272) {
        basic.showArrow(ArrowNames.East)
    } else {
        basic.clearScreen()
    }
    
})
