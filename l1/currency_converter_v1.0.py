rmb_str_valur = input('请输入人民币金额：')
print('您输入的金额为:', rmb_str_valur)
rmb_value = eval(rmb_str_valur)
usd_vs_rmb = 6.77
usd_value=rmb_value / usd_vs_rmb
print('美元金额为:', usd_value)
a1 = 34
a2=str(34)
print(a1+eval(a2))