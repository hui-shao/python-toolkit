import os


def loop():
    for i in range(1, 21):
        dirname = "04-"+str(i).zfill(2)
        if os.path.exists(dirname):
            print(dirname, "existed")
        else:
            print(dirname)
            os.mkdir(dirname)


if __name__ == "__main__":
    try:
        loop()
        input("Finished. Press Enter to exit.")
    except KeyboardInterrupt:
        print("KeyboardInterruption.")
    except Exception as err_info:
        print("\nError!\n", err_info)
