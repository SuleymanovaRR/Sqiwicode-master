from pyqiwiapi import QiwiApi

qiwi_login = '<login>'
qiwi_password = '<password>'
qiwi = QiwiApi(qiwi_login, qiwi_password)
qiwi.get_tgt_ticket()
qiwi.get_st_ticket()
res = qiwi.get_wallet_balance() # Get balance
print(res)

# Also you can use this methods.
print(qiwi.get_payments_stat(
	startDate=input(),
	endDate=input(),
))
print(qiwi.get_payments_history(rows=1, operation="IN"))