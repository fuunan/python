def dogandcat(filename):
    try:
        with open(filename) as f:
            names=f.readlines()
            for name in names:
                print(name.rstrip())
    except FileNotFoundError:
        pass


filenames=['dogs','cats','pigs']
for filename in filenames:
    dogandcat(filename)