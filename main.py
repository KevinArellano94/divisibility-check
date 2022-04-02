

def main():
    print(devisibility_check(9))
    print(devisibility_check(10))

def devisibility_check(z):
    if (z % 5) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    main()