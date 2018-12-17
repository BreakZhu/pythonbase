USD_VS_RMB = 6.77
mmb_str_valur = input('请输入带符号的金额：')
print('您输入的金额为:', mmb_str_valur)
unit = mmb_str_valur[-3:]
input_value = mmb_str_valur[0:-3]
input_value = eval(input_value)
print(unit)
print(input_value)
if unit == 'RMB':
    usd_value = input_value / USD_VS_RMB
    print("美元金额为 : ",usd_value)
elif unit == 'USD':
    rmb_value = input_value * USD_VS_RMB
    print("人民币金额为 : ", rmb_value)

