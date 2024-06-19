import threading
import time
import requests


def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1)


def calculate_sum(data: list[int], start: int, end: int, result: list[int]):
    partial_sum = sum(data[start:end])
    result.append(partial_sum)


def main_threading():
    data = list(range(1000000))
    num_threads = 4
    chunk_size = len(data) // num_threads

    result = []
    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(data)
        thread = threading.Thread(target=calculate_sum, args=(data, start, end, result))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    total_sum = sum(result)
    print("Total sum:", total_sum)


def fetch_and_count_words(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        words_count = len(content.split())
        print(f"Words count from {url}: {words_count}")


if __name__ == "__main__":
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters, daemon=True)  ### daemon=True

    # thread1.start()
    # thread2.start()

    #thread1.join()
    #thread2.join()
    print("Done!")


    #main_threading()



    # Stworzyć program, który równolegle pobiera i przetwarza dane z kilku stron internetowych.
    urls = [
        "https://example.com",
        "https://www.python.org",
        "https://www.wikipedia.org"
    ]
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_and_count_words, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Koniec liczenia")





