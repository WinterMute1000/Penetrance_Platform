import concurrent.futures


def thread_test(test_thread_function, test_objects):
    test_result = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as thread_test_executor:
        test_threads = [thread_test_executor.submit(test_thread_function, test_object)
                        for test_object in test_objects]

        for test_thread in concurrent.futures.as_completed(test_threads):
            test_thread_result = test_thread.result()

            if len(test_thread_result) > 0:
                test_result.append(test_thread_result)

    return test_result
