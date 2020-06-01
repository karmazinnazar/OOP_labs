class Lab3():
    def __init__(self):
        self.string = 'We say ‘weather’ when we talk about how the weather is today. In some places the weather is the'\
                      ' same all day. In other places there are several kinds of weather in one day. We use ‘climate’' \
                      ' when we talk about the usual weather and temperature of a place. We must record the weather ' \
                      'every day for a long time. Then we know the climate of a place. The climate is very cold in ' \
                      'winter and warm in summer. In winter the animals and birds are white. In summer they change' \
                      ' their colour to brown and grey. The winter is very long (8-9 months). In winter we cannot' \
                      ' see any plants. There is a short summer (about 3 months). It is very beautiful. There are' \
                      ' a lot of flowers and grass. There are no trees'
        self.newlist = sorted(self.string.split("."), key=len)
        print(self.newlist)


a = Lab3()
