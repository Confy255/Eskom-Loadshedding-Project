if n%2 == 0:
    hlf_evn1 = int(n/2)
    upper_hlf_evn = x[hlf_evn1:]
    n_upper_hlf_evn = len(upper_hlf_evn)
    if n_upper_hlf_evn%2 == 0:
        t = int((n_upper_hlf_evn/2)-1)
        Q3 = (upper_hlf_evn[t] + upper_hlf_evn[t+1])/2
    else:
        i = int((n_upper_hlf_evn+1)/2)
        Q3 = upper_hlf_evn[i-1]
else:
    hlf_odd1 = int((n+1)/2)
    upper_hlf_odd = x[hlf_odd1:]
    n_upper_hlf_odd = len(upper_hlf_odd) 
    if n_upper_hlf_odd%2 == 0:
        e = int((n_upper_hlf_odd/2)-1)
        Q3 = (upper_hlf_odd[e] + upper_hlf_odd[e+1])/2
    else:
        o = int((n_upper_hlf_odd+1)/2)
        Q3 = upper_hlf_odd[o-1]
    break