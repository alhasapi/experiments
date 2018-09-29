import sys
import os

ZSHRC      = "/home/moktar/.zshrc"
T_LOC      = "/tmp/.zshrc"
REPLACE_ME = "cp %s %s"
THEMES     = "/home/moktar/.oh-my-zsh/themes"

def load_theme_list():
    extract_name = lambda z: z.split(".")[0]
    p_themes = os.popen("ls " + THEMES).read().split("\n")
    return map(extract_name, p_themes)

def build_config_file(theme):
    new_content = open(ZSHRC).read().split("\n")
    new_content[7] = new_content[7].split("=")[0] + "=" + theme
    return "\n".join(new_content)

def write_config_file(where, theme):
    with open(where, "w") as config:
        new_conf_content = build_config_file(theme)
        config.write(new_conf_content)

def set_theme(theme):
    write_config_file(T_LOC, theme)
    os.system(REPLACE_ME %( T_LOC, ZSHRC ))

def test_all_themes():
    themes = list(load_theme_list())
    def computation(theme):
        print("Testing " + theme)
        set_theme(theme)
        os.system("zsh")
    list(map(computation, themes))

if __name__ == "__main__":
    args_size = len(sys.argv)
    if args_size < 2:
        print("%s theme" %sys.argv[0])
    elif '-a' in sys.argv:
        test_all_themes()
    else:
        set_theme(sys.argv)
        os.system("zsh")
