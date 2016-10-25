from urllib.parse import urlsplit


def get_run_results(run, run_results):
    if run.test_type.value == "unittest":
        result = run_results[0]
        data = {'run_status': run.status,
                'result_status': result.status,
                'run_id': run.id,
                'output': result.output,
                'returncode': result.returncode}

    elif run.test_type.value == "output_checking":
        output = []
        status = 'ok'

        for result in run_results:
            if result.output != 'OK':
                status = 'not_ok'

            output.append(result.output)

        data = {'run_status': run.status,
                'result_status': status,
                'run_id': run.id,
                'output': output,
                'returncode': 0}  # TODO

    return data


def get_base_url(uri):
    return "{0.scheme}://{0.netloc}".format(urlsplit(uri))
