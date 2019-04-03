from bs4 import BeautifulSoup
import csv
import os
import json


def write_csv(data, name='example'):
    with open(name + '.csv', 'a', encoding='cp1251') as f:
        writer = csv.writer(f, dialect='excel', delimiter=';')
        writer.writerow([data['header'], data['ad'], data['reg']])
    #     reader = csv.reader(f)
    #     row_count = sum(1 for _ in reader)  # fileObject is your csv.reader
    # return row_count


def get_html_data(html, name='example'):
    soup = BeautifulSoup(html, 'lxml')

    data = soup.findAll('div', class_='b-competitors-banners-list__banner-container')
    for d in data:
        header = d.find('div', class_='b-banner-preview__links-wrap').find('span', class_='b-banner-preview__template')
        header = header.text if header else d.find('a').text
        ad = d.find('div', class_='b-banner-preview__body').text
        reg = d.find('div', class_='b-group-regions__names-popup i-bem')
        reg = reg.get('data-bem') if reg else None
        reg = json.loads(reg) if reg else None
        reg = reg['b-group-regions__names-popup']['names'] if reg else d.find('div', class_='b-group-regions__names').text
        print(f'header = {header}, ad = {ad}, reg = {reg}')
        write_csv({'header': header, 'ad': ad, 'reg': reg}, name=name)


def main():
    html_files = []
    csv_files = []
    for file in os.listdir():
        if file.endswith(".html"):
            html_files.append(file[:-5])
        elif file.endswith('.csv'):
            csv_files.append(file[:-4])
    inwork = set(html_files) - set(csv_files)
    # print(f'html: {html_files}')
    # print(f'csv: {csv_files}')
    # print(f'inwork: {inwork}')
    for file in inwork:
        with open(file + '.html') as f:
            get_html_data(f.read(), file)


if __name__ == '__main__':
    main()
