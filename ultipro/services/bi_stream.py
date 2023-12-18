import backoff  # Helps handle intermittent 405 errors from server
import requests
import ultipro.helpers
from ultipro.helpers import backoff_hdlr
from zeep import Client as ZeepClient
from zeep import Plugin

endpoint = 'BiStreamingService'


@backoff.on_exception(backoff.expo, requests.exceptions.HTTPError, max_tries=8, on_backoff=backoff_hdlr)
@backoff.on_predicate(backoff.fibo, lambda x: x['header']['Status'] == 'Working', on_backoff=backoff_hdlr)
def retrieve_report(client, report_key):
    zeep_client = ZeepClient(f"{client.base_url}{endpoint}")
    return zeep_client.service.RetrieveReport(_soapheaders={'ReportKey': report_key})
