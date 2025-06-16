import scipy.stats as stats
before=[52,47,58,43,50,46,49,53,48,51]
after=[56,50,60,45,54,48,53,56,51,55]
t_stat,p_val=stats.ttest_rel(before,after)
print("t value:",t_stat)
if t_stat<0:
    pvalue_onetail=p_val/2
else:
    pvalue_onetail=1-(p_val/2)
if pvalue_onetail<0.05:
    print("The training improves speed.")
else:
    print("the training has no effect")
    
