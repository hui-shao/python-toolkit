from pip import main
import requests
import os
import sys
import time


base_url = "https://www.test.com/1149/0/1644422122/210427/"
hea = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
err_list = []

if __name__ == "__main__":
    os.chdir(sys.path[0])
    for i in range(0, 1455):
        print(f"Current: {i}", end=" ")

        # Generate url and filename
        url = f"{base_url}{str(i)}.ts"
        filename = f"{str(i).zfill(5)}.ts"

        try:
            res = requests.get(url, headers=hea, timeout=300)
        except Exception:
            print("Fail 1 \n")
            err_list.append(url)
            continue
        if not res or res.status_code != 200:
            print("Fail 2 \n")
            err_list.append(url)
            continue
        else:
            print(res.status_code)
            with open(f"./{filename}", "wb") as f:
                f.write(res.content)
            time.sleep(2)

    if not err_list:
        with open("./err_url.txt", "w") as f:
            for err_url in err_list:
                f.write(err_url + "\n")

    print("End.")
