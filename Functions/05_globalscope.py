chai_type = "Plain Chai"


def front_desk():

    def kitchen():

        global chai_type

        chai_type = "Irani Chai"

    kitchen()


front_desk()

print("Final global chai:", chai_type)