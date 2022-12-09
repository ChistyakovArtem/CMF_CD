import numpy as np
import pandas as pd


def get_ItraxxMain(df):
    ItraxxMain = df[['Itraxx Main Generic',
                     'ER Itraxx Main Long',
                     'ER Itraxx Main Short']]

    d1 = dict(zip(ItraxxMain['Itraxx Main Generic']['Date'], ItraxxMain['Itraxx Main Generic']['Last Price']))
    d2 = dict(zip(ItraxxMain['ER Itraxx Main Long']['Date'], ItraxxMain['ER Itraxx Main Long']['Last Price']))

    ItraxxMain = ItraxxMain['ER Itraxx Main Short']
    ItraxxMain = ItraxxMain.set_index('Date')
    ItraxxMain['Generic Price'] = ItraxxMain.index.map(d1)
    ItraxxMain['ER Long Price'] = ItraxxMain.index.map(d2)
    ItraxxMain.rename(columns={
        'Last Price': 'ER Short Price'
    }, inplace=True)

    ItraxxMain = ItraxxMain.dropna(axis=0, how='all')

    cols = ItraxxMain.columns[[1, 2, 0]]
    ItraxxMain = ItraxxMain[cols]
    return ItraxxMain


def get_ItraxxXover(df):
    ItraxxXover = df[['Itraxx Xover Generic',
                      'ER Itraxx Xover Long',
                      'ER Itraxx Xover Short']]

    d1 = dict(zip(ItraxxXover['Itraxx Xover Generic']['Date'], ItraxxXover['Itraxx Xover Generic']['Last Price']))
    d2 = dict(zip(ItraxxXover['ER Itraxx Xover Long']['Date'], ItraxxXover['ER Itraxx Xover Long']['Last Price']))

    ItraxxXover = ItraxxXover['ER Itraxx Xover Short']
    ItraxxXover = ItraxxXover.set_index('Date')
    ItraxxXover['Generic Price'] = ItraxxXover.index.map(d1)
    ItraxxXover['ER Long Price'] = ItraxxXover.index.map(d2)
    ItraxxXover.rename(columns={
        'Last Price': 'ER Short Price'
    }, inplace=True)

    ItraxxXover = ItraxxXover.dropna(axis=0, how='all')

    cols = ItraxxXover.columns[[1, 2, 0]]
    ItraxxXover = ItraxxXover[cols]

    return ItraxxXover


def get_CDX_IG(df):
    CDX_IG = df[['CDX IG Generic',
                 'ER CDX IG Long',
                 'ER CDX IG Short']]

    d1 = dict(zip(CDX_IG['CDX IG Generic']['Date'], CDX_IG['CDX IG Generic']['Last Price']))
    d2 = dict(zip(CDX_IG['ER CDX IG Long']['Date'], CDX_IG['ER CDX IG Long']['Last Price']))

    CDX_IG = CDX_IG['ER CDX IG Short']
    CDX_IG = CDX_IG.set_index('Date')
    CDX_IG['Generic Price'] = CDX_IG.index.map(d1)
    CDX_IG['ER Long Price'] = CDX_IG.index.map(d2)
    CDX_IG.rename(columns={
        'Last Price': 'ER Short Price'
    }, inplace=True)

    CDX_IG = CDX_IG.dropna(axis=0, how='all')

    cols = CDX_IG.columns[[1, 2, 0]]
    CDX_IG = CDX_IG[cols]

    return CDX_IG
