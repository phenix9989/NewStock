# -*-coding:utf-8 -*-
from StockConfig import  *
import os
import numpy as np
import json
from StockFilterWrapper import filtrate_stop_trade

@filtrate_stop_trade
def get_stock(name):
    """
    :param name: pool_name
    :return: list<Stock>
    """
    print('get_stock({})'.format(name))
    l_stock_list = []
    if not os.path.exists('{}/{}'.format(path_stock, name)):
        return []
    with open('{}/{}'.format(path_stock, name), 'r', encoding='utf-8') as f:
        for stock in f:
            if not stock.startswith('#'):
                stock = stock.strip('\n').split(',')
                if stock != '':
                    l_stock_list.append(Stock(stock[0], stock[1]))
    return l_stock_list


def save_stock(stock_pool_name, stock_list, root=path_track, message=None):
    path = '{root}/{name}'.format(root=root, name=stock_pool_name)
    with open(path, mode='w', encoding='utf-8') as f:
        if message is not None:
            f.write('#' + message)
        for stock in stock_list:
            f.write("{},{}\n".format(stock.stock_code, stock.stock_name))


def get_kline(stock_code, kline_type):
    """
    :param stock_code:
    :param kline_type:
    :return:  nparray<date, open, close, high, low, volume>
    """
    path = '{root}/{type}/{code}'.format(root=path_kline, type=kline_type, code=stock_code)
    with open(path, mode='r', encoding='utf-8') as f:
        return np.array(json.loads(f.readline()))


def save_kline(stock_code, kline_type, kline):
    """
    :param stock_code:
    :param kline_type:
    :param kline:  nparray<date, open, close, high, low, volume>
    :return:
    """
    path = '{root}/{type}/{code}'.format(root=path_kline, type=kline_type, code=stock_code)
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(kline.tolist().__repr__())


if __name__ == '__main__':
    a = get_kline('000001', kline_type_day)
    print(a)
    save_kline('000001', kline_type_day, a)


