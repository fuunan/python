favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
names=['jen','edward','tom','lily','joe','jerry']
for name in names:
    if name  in favorite_languages.keys():
        print(f"{name.title()},thank you for your paticipatiion.")
    else:
        print(f"{name.title()},please paticipate in the investigation as soon as possible.")