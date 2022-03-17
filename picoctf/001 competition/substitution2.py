key = "UHQKRNWLFIYJBTODCZVAXEGSMP"
abc = "abcdefghijklmnopqrstuvwxyz" #97 -22

# msg ="""UHQKRNWLFIYJBTODCZVAXEGSMP 

# Lrzrxdot Jrwzutk uzovr, gfal u wzuer utk vauarjm ufz, utk hzoxwla br alr hrrajr
# nzob u wjuvv quvr ft glfql fa guv rtqjovrk. Fa guv u hruxafnxj vquzuhurxv, utk, ua
# alua afbr, xtytogt ao tuaxzujfvav—on qoxzvr u wzrua dzfpr ft u vqfrtafnfq dofta
# on efrg. Alrzr grzr ago zoxtk hjuqy vdoav truz otr rsazrbfam on alr huqy, utk u
# jotw otr truz alr oalrz. Alr vqujrv grzr rsqrrkftwjm luzk utk wjovvm, gfal ujj alr
# uddruzutqr on hxztfvlrk wojk. Alr grfwla on alr ftvrqa guv erzm zrbuzyuhjr, utk,
# auyftw ujj alftwv ftao qotvfkrzuafot, F qoxjk luzkjm hjubr Ixdfarz noz lfv odftfot
# zrvdrqaftw fa.

# Alr njuw fv: dfqoQAN{5XH5717X710T_3E0JX710T_7H755H1U}"""

#zbx kcfd nh: snpuPZK

msg ="""PZKh (hbutz kut pfszatx zbx kcfd) ftx f zjsx uk puqsazxt hxpatnzj puqsxznznul. Pulzxhzflzh ftx stxhxlzxi gnzb f hxz uk pbfccxldxh gbnpb zxhz zbxnt ptxfznynzj, zxpblnpfc (fli duudcnld) hencch, fli stuvcxq-hucynld fvncnzj. Pbfccxldxh ahafccj puyxt f laqvxt uk pfzxdutnxh, fli gbxl hucyxi, xfpb jnxcih f hztnld (pfccxi f kcfd) gbnpb nh havqnzzxi zu fl ulcnlx hputnld hxtynpx. PZKh ftx f dtxfz gfj zu cxftl f gnix fttfj uk puqsazxt hxpatnzj hencch nl f hfkx, cxdfc xlyntulqxlz, fli ftx buhzxi fli scfjxi vj qflj hxpatnzj dtuash ftuali zbx gutci kut kal fli stfpznpx. Kut zbnh stuvcxq, zbx kcfd nh: snpuPZK{KT3WA3LPJ_4774PE5_4T3_P001_X57444FP}"""

decoded = ""



for letter in msg:
    if letter.upper() in key:
        idx = key.find(letter.upper())
        print(abc[idx], end="")
        continue

    print(letter, end="")