from generators import *

KAROACE_THEME = Theme(
    'Karoace',
    Color('#121212', '#585858'),
    Color('#203856', '#62aedc'),
    Color('#005F87', '#0087AF'),
    Color('#3da542', '#a6d378'),
    Color('#800080', '#C25ABD'),
    Color('#7a3842', '#cb6362'),
    Color('#b9b9b9', '#E4E4E4'),
    Color('#e28c00', '#eccd00'),
)

generate_css(KAROACE_THEME)
generate_readme(KAROACE_THEME)
generate_xresources(KAROACE_THEME)