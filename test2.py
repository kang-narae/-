import FinanceDataReader as fdr

df = fdr.DataReader('068270', '1992-01-01', '2019-10-31')
print(df)

