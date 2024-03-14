class Color:
    def __init__(self, color, color_alt):
        self.color = color
        self.color_alt = color_alt

class Theme:
    def __init__(self, name:str, black:Color, blue:Color, cyan:Color, green:Color, magenta:Color, red:Color, white:Color, yellow:Color):
        self.name = name

        self.black = black
        self.blue = blue
        self.cyan = cyan
        self.green = green
        self.magenta = magenta
        self.red = red
        self.white = white
        self.yellow = yellow


def generate_css(theme:Theme, filename='styles.css'):
    with open(filename, 'w+') as f:
        f.write(f'/*\n  {theme.name} color theme \n*/\n')
        f.write(':root {')

        f.write('\n'.join(f'''
  --{attribute}: {value.color};
  --{attribute}_alt: {value.color_alt};'''
        for attribute, value in vars(theme).items() if type(value) is Color))

        f.write('\n}')

def generate_readme(theme:Theme, filename='README.md'):
    colors = []
    for attribute, value in vars(theme).items():
        if type(value) is Color:
            colors.append((attribute, value.color))
            colors.append((attribute+'_alt', value.color_alt))

    with open(filename, 'w+') as f:
        f.write(f'# {theme.name} theme\n\n')
        f.write('## Colors\n\n')
        f.write('| | '+' | '.join(color for color, _ in colors)+' |\n')
        f.write('| '+' | '.join('-' for _ in range(len(colors)+1))+' |\n')
        f.write(
            ' |\n'.join(
                f'| **{bg_color_name}** | '+
                ' | '.join(
                    f'<span style="background-color:{bg_color}; color:{color}">{color}</span>'
                    for _, color in colors
                ) for bg_color_name, bg_color in colors
            )+' |\n'
        )

def generate_xresources(theme:Theme, filename='.Xresources'):
    attributes = vars(theme)
    
    with open(filename, 'w+') as f:
        f.write(f'! {theme.name} color theme\n\n')
        f.write('! special\n')
        f.write(f'*.background: {theme.black.color}\n')
        f.write(f'*.foreground: {theme.white.color_alt}\n')
        
        f.write('\n'.join(f'''
! {color}           
*.color{i}: {attributes[color].color}
*.color{i+8}: {attributes[color].color_alt}'''
        for i, color in enumerate(['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])))