import multiprocessing

def process_text(text, output):
    # Розділяємо текст на слова, видаляючи пунктуацію
    words = text.replace('.', '').replace(',', '').split()
    output.put(words)

def main():
    text = """
    Parallel computing is a type of computation in which many calculations or the execution of processes are carried out simultaneously. 
    Large problems can often be divided into smaller ones, which can then be solved at the same time.
    """
    parts = text.split(". ")

    output = multiprocessing.Queue()
    processes = []

    for part in parts:
        proc = multiprocessing.Process(target=process_text, args=(part, output))
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()

    results = []
    while not output.empty():
        results.extend(output.get())

    print("Identified words:", results)

if __name__ == "__main__":
    main()
    # input('Нажміть Enter, щоб вийти...')
