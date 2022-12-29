basic.forever(function () {
    if (input.compassHeading() > 358 || input.compassHeading() < 2) {
        basic.showArrow(ArrowNames.North)
    } else if (input.compassHeading() > 43 && input.compassHeading() < 47) {
        basic.showArrow(ArrowNames.NorthWest)
    } else if (input.compassHeading() > 88 && input.compassHeading() < 92) {
        basic.showArrow(ArrowNames.West)
    } else if (input.compassHeading() > 133 && input.compassHeading() < 137) {
        basic.showArrow(ArrowNames.SouthWest)
    } else if (input.compassHeading() > 178 && input.compassHeading() < 182) {
        basic.showArrow(ArrowNames.South)
    } else if (input.compassHeading() > 223 && input.compassHeading() < 227) {
        basic.showArrow(ArrowNames.SouthEast)
    } else if (input.compassHeading() > 268 && input.compassHeading() < 272) {
        basic.showArrow(ArrowNames.East)
    } else if (input.compassHeading() > 313 && input.compassHeading() < 317) {
        basic.showArrow(ArrowNames.NorthEast)
    } else {
        basic.clearScreen()
    }
})
