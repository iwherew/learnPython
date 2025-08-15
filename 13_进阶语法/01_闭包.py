def account_create(amount = 0):
    def atm(num, save = True):
        nonlocal amount
        if save:
            amount += num
        else:
            amount -= num
        print(amount)
    return atm

fn = account_create(1000)
fn(100)
fn(500)
fn(800, False)
