import whois
import datetime
import argparse
import requests
from urllib.parse import urlparse
from requests import ConnectionError, Timeout


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--filepath',
        help='Input the filepath to the file'
    )
    return parser.parse_args()


def load_sites_from_file(filepath):
    with open(filepath, 'r') as file_with_url:
        url_list = file_with_url.read().splitlines()
    return url_list


def get_domain_name(url):
    domain_name = urlparse(url).netloc
    return domain_name


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
    except ConnectionError:
        return False, 'ConnectionError'
    except Timeout:
        return False, 'Timeout'
    if response is None:
        return False, None
    status = response.status_code
    if status == 200:
        return True, status
    return False, status


def get_expiration_date(domain_name):
    expiration_date = whois.whois(domain_name).expiration_date
    if isinstance(expiration_date, list):
        return expiration_date[0]
    else:
        return expiration_date


def check_domain_during_date(expiration_date):
    today = datetime.datetime.today()
    during_date = (expiration_date - today).days
    return during_date


def print_url_and_domain(during_date, min_paid_period):
    if during_date <= min_paid_period:
        print('Attention: domain {} has {} days. It is bad'.format(
            domain_name, during_date))
    else:
        print('OK: domain: {0} has {1} paid days'.format(
            domain_name, during_date))


if __name__ == '__main__':
    min_paid_period = 30

    args = get_parser()
    url_list = load_sites_from_file(args.filepath)

    for url in url_list:
        domain_name = get_domain_name(url)
        server_respond_with_200 = is_server_respond_with_200(url)
        expiration_date = get_expiration_date(domain_name)
        domain_during_date = check_domain_during_date(expiration_date)
        print_url_and_domain(domain_during_date, min_paid_period)
