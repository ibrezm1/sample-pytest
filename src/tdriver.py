from src.utils import mockthis

def testthis():
    ret = mockthis("val")
    print(ret)
    return (ret)

def main():
    testthis()

if __name__ == "__main__":
    main()              # pragma: no cover