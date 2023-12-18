from pprint import pprint

from ultipro.services import bi_data, bi_stream


def execute_and_fetch(client, report_path, delimiter=','):
    context = bi_data.log_on_with_token(client)
    pprint(context)
    print("report path: " + report_path)
    k = bi_data.execute_report(client, context, report_path, delimiter=delimiter)
    pprint(k)
    r = bi_stream.retrieve_report(client, k)
    pprint(r)
    return r['body']['ReportStream'].decode('utf-8')
