def update_order():

    chai_type = "Elaichi"

    def kitchen():

        nonlocal chai_type

        chai_type = "Kesar"
        print("in kitchen:", chai_type)

    kitchen()

    print("After kitchen update:", chai_type)


update_order()